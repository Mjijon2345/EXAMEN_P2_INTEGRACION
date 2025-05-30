from pydantic import BaseModel

class Solicitud(BaseModel):
    id: int
    tipo: str
    estudiante: str

class Estado(BaseModel):
    id: int
    estado: str
