from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
import os
from dotenv import load_dotenv

# Cargar variables de entorno
load_dotenv()

# URL base de datos (SQLite)
SQLALCHEMY_DATABASE_URL = os.getenv("DATABASE_URL", "sqlite:///./app.db")


# Motor base de datos
engine = create_engine(
    SQLALCHEMY_DATABASE_URL,
    connect_args={"check_same_thread": False} # Solo para SQLite
)

# Sesión base de datos
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Base Modelos
Base = declarative_base()

# Dependencia para obtener sesión DB
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()