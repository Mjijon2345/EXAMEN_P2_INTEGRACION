from jose import jwt

SECRET_KEY = "clave-secreta"
ALGORITHM = "HS256"

# Datos del usuario ficticio
datos = {"user": "fabiana"}

# Generar el token
token = jwt.encode(datos, SECRET_KEY, algorithm=ALGORITHM)
print("Token JWT generado:")
print(token)
