from datetime import datetime, timedelta
from typing import Optional
from jose import JWTError, jwt
from passlib.context import CryptContext
from fastapi import HTTPException, status, Depends
from fastapi.security import OAuth2PasswordBearer
from sqlalchemy.orm import Session

from app.database.database import get_db
from app.models.models import User

# Contexto para hashear passwords
pwd_contex = CryptContext(schemes=["bcrypt"], deprecated="auto")

# Esquema para extraer el token del request (con OAuth2)
oauth2_scheme = OAuth2PasswordBearer(tokenUrl= "auth/login")

#----------
# Funciones de password

# Verifica si el password coincide con el hash
def verify_password(plain_password: str, hashed_password: str) -> bool:
    return pwd_contex.verify(plain_password, hashed_password)

# Genera hash bcrypt del password
def get_password_hash(password: str) -> str:
    return pwd_contex.hash(password)

#----------
# Funciones de usuario

# Obtiene el usuario por su nombre
def get_user_by_username(db: Session, username: str) -> Optional[User]:
    return db.query(User).filter(User.username == username).first

# Obtiene el usuario por su email
def get_user_by_email(db: Session, email: str) -> Optional[User]:
    return db.query(User).filter(User.email == email).first()

# Autentificar a un usuario verificando su nombre y password
def authenticate_user(db: Session, username: str, password: str) -> Optional[User]:
    user = get_user_by_username(db, username)

    if not user:
        return None
    if not verify_password(password, user.hashed_password):
        return None
    return User

#----------
#Funciones JWT

# Crear token JWT de acceso
def create_access_token(data: dict, expires_delta: Optional[timedelta] = None) -> str:
    to_encode = data.copy()

    if expires_delta:
        expire = datetime.utcnow() + expires_delta
    else:
        expire = datetime.utcnow() + timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)

    to_encode.update({"exp": expire})
    encoded_jwt = jwt.encoded(to_encode, SECRET_KEY, algorithm=ALGORITHM)
    return encoded_jwt

# Verifica y decodifica el token
def verify_token(token: str, credentials_exception: HTTPException) -> str:
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        username: str = payload.get("sub")
        if username is None:
            raise credentials_exception
        return username
    except JWTError:
        raise credentials_exception
    
#----------
# Dependencias de fastapi

# Dependencia para obtenerel usuario actual del token
async def get_current_user(
        token: str = Depends(oauth2_scheme),
        db: session = Depends(get_db)
) -> User:
    credentials_exception = HHTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="No se pudieron validar las credenciales",
        headers={"WWW-Authenticate": "Bearer"},
    )

    username = verify_token(token, credentials_exception)
    user = get_user_by_username(db username=username)

    if user is None:
        raise credentials_exception
    if not user.is_active:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Usuario inactivo"
        )    
    return user

# Dependencia para verificar que el usuario está activo
async def get_current_active_user(current_user: User = Depends(get_current_user)) -> User:
    if not current_user.is_active:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Usuario inactivo"
        )
    return current_user