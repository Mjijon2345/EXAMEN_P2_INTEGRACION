def simular_servicio_certificacion(solicitud_id: int):
    estados = ["procesado", "en revisión", "rechazado"]
    return estados[solicitud_id % 3]
