from fastapi import APIRouter, HTTPException, Depends
from sqlalchemy.orm import Session
import crud.crud_servicios, config.db, schemas.schema_servicios, models.model_servicios

router = APIRouter()

# Dependencia DB
def get_db():
    db = config.db.SessionLocal()
    try:
        yield db
    finally:
        db.close()

# GET - Listar todos los servicios
@router.get("/servicios", response_model=list[schemas.schema_servicios.Servicio])
def get_servicios(db: Session = Depends(get_db)):
    servicios = crud.crud_servicios.get_servicios(db)
    if not servicios:
        raise HTTPException(status_code=404, detail="No se encontraron servicios")
    return servicios
