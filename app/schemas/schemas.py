from pydantic import BaseModel, EmailStr, Field
from datetime import datetime
from typing import Optional, List

# Esquema para usuarios

# Base
class UserBase(BaseModel):
    email: EmailStr
    username: str = Field(..., min_length=3, max_length=50)
    full_name: Optional[str] = Field(None, max_length=100)

# Registro
class UserCreate(UserBase):
    password= str = Field(..., min_length=6)

# Actualizar
class UserUpdate(BaseModel):
    email: Optional[EmailStr] = None
    username: Optional[str] = Field(None, min_length=3, max_length=50)
    full_name: Optional[str] = Field(None, max_length=100)
    password: Optional[str] = Field(None, min_length=6)


# Respuestas a post
class UserResponse(UserBase):
    id: int
    is_active: bool
    created_at: datetime

    class Config:
        from_attributes = True  # Permite la creación desde ORM

# ----------
#Esquema para posts

#Base
class PostBase(BaseModel):
    title: str = Field(..., min_length=1, max_length=200)
    content: str = Field(..., min_length=1)
    is_published: bool = True

# Crear post
class PostCreate(PostBase):
    pass

# Editar post
class PostUpdate(BaseModel):
    title: Optional[str] = Field(None, min_length=1, max_length=200)
    content: Optional[dtr] = Field(None, min_length=1)
    is_published: Optional[bool] = None

# Responder post
class PostResponse(PostBase):
    id: int
    author_id: int
    created_at: datetime
    updated_at: Optional[datetime] = None

    class config:
        from_attributes = True

# Post con información del autor
class PostWithAutor(PostResponse):
    author: UserResponse

#----------
# Esquemas para autorización

# Respuesta de token JWT
class Token(BaseModel):
    access_token: str
    token_type: str

# Datos dentro del token
class TokenData(BaseModel):
    username: Optional[str] = None

#----------
# Esquemas comunes

# Mensajes simples
class Message(BaseModel):
    message: str

# Health check
class HealthCheck(BaseModel):
    status: str
    version: str
    timestamp: datetime




