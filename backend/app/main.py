from fastapi import FastAPI
from app.db.base import Base
from app.db.engine import engine

app = FastAPI(title="Sistema de Inventario 2025")

Base.metadata.create_all(bind=engine)

@app.get("/")
def root():
    return {"message": "Bienvenido al Sistema de Inventario 2025"}
