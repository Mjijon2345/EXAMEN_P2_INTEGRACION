from fastapi import FastAPI, HTTPException, Security
from fastapi.security import HTTPBearer, HTTPAuthorizationCredentials
from app.models import Solicitud, Estado
from app.db import solicitudes
from app.auth import verificar_token
from app.soap_client import simular_servicio_certificacion

app = FastAPI()

# Definimos el esquema de seguridad Bearer
security = HTTPBearer()

@app.post("/solicitudes")
def crear_solicitud(
    solicitud: Solicitud,
    credentials: HTTPAuthorizationCredentials = Security(security)
):
    token = credentials.credentials  # Extrae el token sin "Bearer"
    user = verificar_token(token)
    if not user:
        raise HTTPException(status_code=401, detail="Token inválido")

    solicitudes[solicitud.id] = solicitud
    estado = simular_servicio_certificacion(solicitud.id)
    return Estado(id=solicitud.id, estado=estado)

@app.get("/solicitudes/{id}")
def obtener_solicitud(
    id: int,
    credentials: HTTPAuthorizationCredentials = Security(security)
):
    token = credentials.credentials
    user = verificar_token(token)
    if not user:
        raise HTTPException(status_code=401, detail="Token inválido")

    solicitud = solicitudes.get(id)
    if not solicitud:
        raise HTTPException(status_code=404, detail="Solicitud no encontrada")

    estado = simular_servicio_certificacion(solicitud.id)
    return Estado(id=solicitud.id, estado=estado)
