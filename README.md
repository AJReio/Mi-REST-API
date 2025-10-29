- Descripción General
API RESTful desarrollada con FastAPI que proporciona un sistema de autenticación JWT y gestión de usuarios y posts. Diseñada con arquitectura modular y mejores prácticas de seguridad.

----------

- Tabla de Contenidos
Stack Tecnológico
Dependencias y Versiones
Instalación y Configuración
Arquitectura del Proyecto
Endpoints de la API
Modelos de Datos
Sistema de Autenticación
Desarrollo y Despliegue

----------

- Stack Tecnológico
Backend
FastAPI 0.104.1 - Framework web moderno y rápido para APIs
Python 3.8+ - Lenguaje de programación
Uvicorn 0.24.0 - Servidor ASGI de alto rendimiento

Base de Datos
SQLAlchemy 2.0.23 - ORM para Python
SQLite - Base de datos relacional (desarrollo)
Alembic 1.12.1 - Sistema de migraciones de base de datos

Autenticación & Seguridad
Python-JOSE 3.3.0 - Implementación JWT (JSON Web Tokens)
Passlib[bcrypt] 1.7.4 - Hash seguro de contraseñas
OAuth2 - Flujo estándar de autenticación

Validación & Serialización
Pydantic 2.5.0 - Validación de datos y esquemas type-safe
Python-multipart 0.0.6 - Soporte para form-data y uploads
Python-dotenv 1.0.0 - Gestión de variables de entorno

----------

- Dependencias y Versiones
Dependencias Principales (requirements.txt)
txt
fastapi==0.104.1           # Framework web principal
uvicorn==0.24.0            # Servidor ASGI
python-dotenv==1.0.0       # Variables de entorno
sqlalchemy==2.0.23         # ORM y gestión de base de datos
alembic==1.12.1            # Migraciones de BD
pydantic==2.5.0            # Validación de datos
python-jose[cryptography]==3.3.0  # Tokens JWT
passlib[bcrypt]==1.7.4     # Hash de contraseñas
python-multipart==0.0.6    # Soporte para form-data

Propósito de Cada Dependencia
Dependencia
Versión
Propósit

FastAPI
0.104.1
Framework web principal con documentación automática

Uvicorn
0.24.0
Servidor para ejecutar la aplicación FastAPI

SQLAlchemy
2.0.23
ORM para interactuar con la base de datos

Pydantic
2.5.0
Validación de datos y serialización

Python-JOSE
3.3.0
Generación y verificación de tokens JWT

Passlib[bcrypt]
1.7.4
Hash seguro de contraseñas

Alembic
1.12.1
Sistema de migraciones para esquemas de BD

Python-dotenv
1.0.0
Carga de variables de entorno desde archivo .env

Python-multipart
0.0.6
Soporte para formularios y uploads de archivos

----------

- Instalación y Configuración
Prerrequisitos
Python 3.8 o superior
pip (gestor de paquetes de Python)
Git (opcional, para control de versiones)
Proceso de Instalación Paso a Paso


1. Clonar o Descargar el Proyecto
bash
# Si tienes el código en Git
git clone <url-del-repositorio>
cd mi_api_funcional
# O crear la estructura manualmente
mkdir mi_api_funcional
cd mi_api_funcional


2. Crear Entorno Virtual
bash
# Windows
python -m venv venv
venv\Scripts\activate
# Linux/Mac 
python3 -m venv venv
source venv/bin/activate


3. Instalar Dependencias
bash
pip install -r requirements.txt


4. Configurar Variables de Entorno
Crear archivo .env en la raíz del proyecto:
env
DATABASE_URL=sqlite:///./app.db
SECRET_KEY=tu-clave-secreta-super-segura-aqui-cambiar-en-produccion
ALGORITHM=HS256
ACCESS_TOKEN_EXPIRE_MINUTES=30


5. Inicializar Base de Datos
La base de datos se crea automáticamente al ejecutar la aplicación por primera vez.


6. Ejecutar la Aplicación
bash
# Desarrollo (con recarga automática)
uvicorn app.main:app --reload --host 0.0.0.0 --port 8000
# Producción
uvicorn app.main:app --host 0.0.0.0 --port 8000

----------

Verificar la Instalación
1. Acceder a la documentación interactiva:
Swagger UI: http://localhost:8000/docs
ReDoc: http://localhost:8000/redoc


2. Probar endpoints básicos:
GET http://localhost:8000/ - Página principal
GET http://localhost:8000/health - Estado del sistema

----------

- Arquitectura del Proyecto
text
mi_api_funcional/
├── app/
│   ├── auth/
│   │   ├── auth.py              # Lógica de autenticación JWT
│   │   └── __pycache__/
│   ├── database/
│   │   ├── database.py          # Configuración DB y sesiones
│   │   └── __pycache__/
│   ├── models/
│   │   ├── models.py            # Modelos SQLAlchemy (User, Post)
│   │   └── __pycache__/
│   ├── routes/
│   │   ├── auth.py              # Endpoints de autenticación
│   │   └── __pycache__/
│   ├── schemas/
│   │   ├── schemas.py           # Esquemas Pydantic
│   │   └── __pycache__/
│   ├── utils/                   # Utilidades comunes
│   ├── __pycache__/
│   ├── main.py                  # Aplicación FastAPI principal
│   └── __init__.py
├── tests/                       # Tests automatizados
├── venv/                        # Entorno virtual (no versionar)
├── .env                         # Variables de entorno
├── app.db                       # Base de datos SQLite
├── requirements.txt             # Dependencias del proyecto
└── README.md                    # Esta documentación

----------

- Sistema de Autenticación
Flujo JWT Implementado

1. Registro → Valida datos únicos, hashea password, crea usuario

2. Login → Verifica credenciales, genera JWT token con expiración

3. Acceso → Middleware valida token en requests protegidas

4. Protección → Verificación de usuario activo y permisos
Configuración de Seguridad


python
# En app/auth/auth.py
SECRET_KEY = "clave-secreta"  # Cambiar en producción
ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRE_MINUTES = 30

-----------

- Endpoints de la API

Endpoints Públicos
Método
Endpoint
Descripción
Body Request


GET
/
Información general
-

GET
/health
Estado del sistema
-

GET
/info
Info de la API
-

POST
/auth/register
Registrar usuario
UserCreate

POST
/auth/login
Login y obtener token
OAuth2PasswordRequestForm

----------

Endpoints Protegidos
Método
Endpoint
Descripción
Autenticación


GET
/auth/me
Info usuario actual
JWT Bearer

----------

- Modelos de Datos

Usuario (User)
python
class User(Base):
    __tablename__ = "users"
    id = Column(Integer, primary_key=True, index=True)
    email = Column(String, unique=True, index=True, nullable=False)
    username = Column(String, unique=True, index=True, nullable=False)
    hashed_password = Column(String, nullable=False)
    full_name = Column(String)
    is_active = Column(Boolean, default=True)
    created_at = Column(DateTime(timezone=True), server_default=func.now())

Post (Post)
python
class Post(Base):
    __tablename__ = "posts"
    id = Column(Integer, primary_key=True, index=True)
    title = Column(String, index=True, nullable=False)
    content = Column(Text, nullable=False)
    author_id = Column(Integer, nullable=False)
    is_published = Column(Boolean, default=True)
    created_at = Column(DateTime(timezone=True), server_default=func.now())
    updated_at = Column(DateTime(timezone=True), onupdate=func.now())

----------
    
- Comandos Útiles
  
Desarrollo
bash
# Ejecutar en modo desarrollo
uvicorn app.main:app --reload

# Ejecutar en puerto específico
uvicorn app.main:app --reload --port 8080

# Ejecutar en red local
uvicorn app.main:app --reload --host 0.0.0.0

Base de Datos
bash
# Crear migraciones (cuando añadas modelos)
alembic revision --autogenerate -m "Descripción del cambio"

# Aplicar migraciones
alembic upgrade head

Dependencias
bash
# Congelar dependencias actuales
pip freeze > requirements.txt

# Instalar en nuevo entorno
pip install -r requirements.txt


- Próximos Pasos y Mejoras
Para Producción
Configurar PostgreSQL o MySQL
Usar variables de entorno reales para secrets
Implementar HTTPS
Configurar CORS para frontend
Añadir rate limiting
Configurar logging estructurado
Funcionalidades Adicionales
Endpoints CRUD completos para posts
Sistema de roles y permisos
Refresh tokens
Upload de archivos
Email de verificación
Recuperación de contraseña
Desarrollo
Tests automatizados
CI/CD pipeline
Dockerización
Monitoring y métricas

Notas para el Desarrollador
Esta API está diseñada como base sólida para proyectos más complejos. La arquitectura modular permite fácil extensión añadiendo nuevos modelos, esquemas y routers.
Características clave listas para producción:
✅ Autenticación JWT segura
✅ Validación de datos robusta
✅ ORM con SQLAlchemy 2.0
✅ Documentación automática
✅ Manejo de errores apropiado
✅ Estructura escalable
