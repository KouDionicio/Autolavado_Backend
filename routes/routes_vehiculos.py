from fastapi import APIRouter, HTTPException, Depends
from sqlalchemy.orm import Session 
import crud.crud_vehiculos, config.db, schemas.schema_vehiculos, models.model_vehiculos

router = APIRouter()

# Dependencia DB
def get_db():
    db = config.db.SessionLocal()
    try:
        yield db
    finally:
        db.close()

# GET - Listar todos los vehículos
@router.get("/vehiculos", response_model=list[schemas.schema_vehiculos.Vehiculo])
def get_vehiculos(db: Session = Depends(get_db)):
    vehiculos = crud.crud_vehiculos.get_vehiculos(db)
    if not vehiculos:
        raise HTTPException(status_code=404, detail="No se encontraron vehículos")
    return vehiculos
