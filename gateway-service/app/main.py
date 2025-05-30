from fastapi import FastAPI, HTTPException, Security, Request
from fastapi.security import HTTPBearer, HTTPAuthorizationCredentials
from app.rate_limiter import check_rate_limit
from app.circuit_breaker import should_allow_request, report_failure, reset_circuit
from pydantic import BaseModel
import httpx

app = FastAPI(
    title="API Gateway",
    description="Gateway para redirigir solicitudes a SolicitudService",
    version="1.0.0"
)

security = HTTPBearer()
SOLICITUD_SERVICE_URL = "http://127.0.0.1:8000"

class Solicitud(BaseModel):
    id: int
    descripcion: str

@app.post("/api/solicitudes")
async def proxy_crear_solicitud(
    solicitud: Solicitud,
    request: Request,
    credentials: HTTPAuthorizationCredentials = Security(security)
):
    check_rate_limit(request.client.host)

    if not should_allow_request():
        raise HTTPException(status_code=503, detail="Servicio temporalmente no disponible (circuit breaker)")

    token = credentials.credentials

    try:
        async with httpx.AsyncClient() as client:
            response = await client.post(
                f"{SOLICITUD_SERVICE_URL}/solicitudes",
                json=solicitud.dict(),
                headers={"Authorization": f"Bearer {token}"}
            )
        reset_circuit()
        return response.json()
    except Exception:
        report_failure()
        raise HTTPException(status_code=504, detail="Falla al contactar al microservicio")

@app.get("/api/solicitudes/{id}")
async def proxy_obtener_solicitud(
    id: int,
    request: Request,
    credentials: HTTPAuthorizationCredentials = Security(security)
):
    check_rate_limit(request.client.host)

    if not should_allow_request():
        raise HTTPException(status_code=503, detail="Servicio temporalmente no disponible (circuit breaker)")

    token = credentials.credentials

    try:
        async with httpx.AsyncClient() as client:
            response = await client.get(
                f"{SOLICITUD_SERVICE_URL}/solicitudes/{id}",
                headers={"Authorization": f"Bearer {token}"}
            )
        reset_circuit()
        return response.json()
    except Exception:
        report_failure()
        raise HTTPException(status_code=504, detail="Falla al contactar al microservicio")
