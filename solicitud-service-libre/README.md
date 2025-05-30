# SolicitudService

Microservicio REST para solicitudes académicas de estudiantes.

## Endpoints

- POST `/solicitudes`: Crea una nueva solicitud.
- GET `/solicitudes/{id}`: Consulta el estado de una solicitud.

## Requisitos

- Python 3.10+
- FastAPI, Uvicorn, python-jose

## Cómo ejecutar

```bash
pip install -r requirements.txt
uvicorn app.main:app --reload
