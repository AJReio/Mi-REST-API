from fastapi import FastAPI
from app.database.database import engine, Base
from app.models.models import User, Post

# Crear tablas en la base de datos
Base.metadata.create_all(bind=engine)

# Crear app FastAPI 
app =FastAPI(
    title="Mi API",
    description="API con modelos y esquemas implementados.",
    version="1.0.0"
)

# Ruta principal
@app.get("/")
def read_root():
    return {"message": "Funciona, ready to commit.",
            "status": "Modelos y esquemas configurados",
            "endpoints": [
                "/health - Estado del sistema",
                "/docs - Documentación interactiva"
            ]
}

# Ruta de salud
@app.get("/health")
def health_check():
    return {"status": "healthy",
            "components": {
                "batabase": "SQLite con SQLAlchemy.",
                "models": "User y Post.",
                "schemas": "Pydantic configurado."
            }}

# Ruta de información
@app.get("/info")
def get_info():
    return {"name": "Mi API", "verson": "1.0.0"}