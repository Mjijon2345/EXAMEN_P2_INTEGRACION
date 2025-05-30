from jose import jwt, JWTError

SECRET_KEY = "clave-secreta"
ALGORITHM = "HS256"

def verificar_token(token: str):
    try:
        # Si viene como "Bearer <token>", lo limpiamos:
        if token.startswith("Bearer "):
            token = token.replace("Bearer ", "")
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        return payload
    except JWTError:
        return None
