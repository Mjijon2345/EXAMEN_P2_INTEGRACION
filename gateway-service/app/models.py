from pydantic import BaseModel

class Solicitud(BaseModel):
    id: int
    tipo: str
    estudiante: str
