Plataforma de Servicios Estudiantiles
Este proyecto implementa una arquitectura basada en microservicios para una plataforma académica que permite a los estudiantes generar solicitudes de certificados, los cuales son procesados por un sistema externo. Incluye autenticación con JWT, un API Gateway, y medidas básicas de control como Rate Limiting y Circuit Breaking.

ESTRUCTURA 
plataforma-servicios-estudiantiles/
├── solicitud-service/           # Servicio REST para solicitudes
├── gateway-service/             # API Gateway con seguridad, rate limiter y circuit breaker
├── informe/                     # Informe final en PDF
└── README.md                    # Este archivo

Servicios Incluidos
1. solicitud-service
Framework: FastAPI

Funcionalidad:

Crear solicitud con autenticación JWT.

Obtener estado de una solicitud simulando respuesta SOAP.

Seguridad:

Verificación de token JWT en cada endpoint.

2. gateway-service
Funciona como API Gateway.

Redirecciona peticiones hacia solicitud-service.

Implementa:

Autenticación con HTTPBearer

Rate Limiting (máx 5 peticiones por IP cada 60 segundos)

Circuit Breaking (si el servicio objetivo falla muchas veces seguidas)

AUTENTICACION
Authorization: Bearer <TOKEN>

from jose import jwt

SECRET_KEY = "clave-secreta"
ALGORITHM = "HS256"
token = jwt.encode({"user": "fabiana"}, SECRET_KEY, algorithm=ALGORITHM)
print(token)

Ir a la documentación Swagger:

Solicitud Service → http://127.0.0.1:8000/docs

Gateway → http://127.0.0.1:8010/docs

Realizar pruebas de:

POST /api/solicitudes

GET /api/solicitudes/{id}

Consulta el informe completo del proyecto en:

/informe/Informe_Plataforma_Servicios_Estudiantiles.pdf

Incluye:

Arquitectura

Capturas de pruebas

Diagramas de flujo

Justificación técnica

Análisis de monitoreo y trazabilidad

📝 Autores
Mateo Jijón

 Requisitos
Python 3.11

FastAPI

Uvicorn

jose

httpx

DEPENDENCIAS

pip install -r requirements.txt


