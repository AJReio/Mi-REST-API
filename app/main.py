from fastapi import FastAPI
from app.database.database import engine, Base
from app.models.models import User, Post
from app.routes import auth

# Crear tablas en la base de datos
Base.metadata.create_all(bind=engine)

# Crear app FastAPI 
app =FastAPI(
    title="Mi API",
    description="API con modelos y esquemas implementados.",
    version="1.0.0",
    docs_url="/docs",
    redoc_url="/redoc"
)

# Incluir routers
app.include_router(auth.router)

# Ruta principal
@app.get("/")
def read_root():
    return {
        "message": "API con autentificación JWT funcionando.",
        "endpoints_publicos":[
            "GET / - Esta página.",
            "GET /health - Estado del sistema.",
            "POST /auth/register - Registrar usuario.",
            "POST /auth/login - Iniciar sesión."
        ]
}

# Ruta de salud
@app.get("/health")
def health_check():
    return {"status": "healthy",
            "components": {
                "database": "SQLite con SQLAlchemy.",
                "models": "User y Post.",
                "schemas": "Pydantic configurado.",
                "authentication": "JWT con bcrypt"
            }}

# Ruta de información
@app.get("/info")
def get_info():
    return {"name": "Mi API", "verson": "1.0.0"}