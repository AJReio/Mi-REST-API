from fastapi import FastAPI
from dotenv import load_dotenv
import os


# Variables de entorno
load_dotenv()

# Aplicación FastAPI
app = FastAPI(
    title=os.getenv("APP_NAME", "Mi REST API"),
    description="Rest API simple con FASTAPI",
    version="1.0.0"
)

# Ruta de prueba
@app.get("/info")
async def read_root():
    return {"message": "¡Bienvenido!"}

# Ruta de salud
@app.get("/health")
async def health_check():
    return {"status": "healthy", "version": "1.0.0"}

# Ruta de info
@app.get("/info")
async def get_info():
    return {
        "app_name": "Mi REST API",
        "version": "1.0.0",
        "endpoints": ["/", "/health", "/info", "/docs"]
    } 

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)