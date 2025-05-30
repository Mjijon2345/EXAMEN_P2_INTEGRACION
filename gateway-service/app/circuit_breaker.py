import time

# Estado del circuito
failure_count = 0
last_failure_time = 0
CIRCUIT_OPEN = False

# Configuración
MAX_FAILURES = 3
COOLDOWN_TIME = 30  # segundos

def should_allow_request():
    global CIRCUIT_OPEN, last_failure_time

    if CIRCUIT_OPEN:
        if time.time() - last_failure_time > COOLDOWN_TIME:
            CIRCUIT_OPEN = False
            return True  # Reintentamos
        else:
            return False
    return True

def report_failure():
    global failure_count, CIRCUIT_OPEN, last_failure_time
    failure_count += 1
    if failure_count >= MAX_FAILURES:
        CIRCUIT_OPEN = True
        last_failure_time = time.time()

def reset_circuit():
    global failure_count, CIRCUIT_OPEN
    failure_count = 0
    CIRCUIT_OPEN = False
