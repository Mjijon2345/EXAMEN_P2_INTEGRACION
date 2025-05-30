import time
from fastapi import HTTPException

# Diccionario para guardar conteos por IP
requests_counter = {}

# Configuración: máx 5 solicitudes por 60 segundos
RATE_LIMIT = 5
WINDOW_SIZE = 60  # segundos

def check_rate_limit(client_ip: str):
    current_time = time.time()
    if client_ip not in requests_counter:
        requests_counter[client_ip] = []

    # Filtra solicitudes antiguas
    requests = [t for t in requests_counter[client_ip] if current_time - t < WINDOW_SIZE]
    requests.append(current_time)
    requests_counter[client_ip] = requests

    if len(requests) > RATE_LIMIT:
        raise HTTPException(status_code=429, detail="Rate limit exceeded")
