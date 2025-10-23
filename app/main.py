from fastapi import FastAPI


# Crear app FastAPI 
app =FastAPI()

# Ruta principal
@app.get("/")
def read_root():
    return {"message": "Funciona!!"}

# Ruta de salud
@app.get("/health")
def health_check():
    return {"status": "healthy"}

# Ruta de información
@app.get("/info")
def get_info():
    return {"name": "Mi API", "verson": "1.0.0"}