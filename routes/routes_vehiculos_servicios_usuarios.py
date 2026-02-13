from fastapi import APIRouter, HTTPException, Depends
from sqlalchemy.orm import Session 
import crud.crud_vehiculos_servicios_usuarios, config.db, schemas.schema_vehiculos_servicios_usuarios, models.model_vehiculos_servicios_usuarios

router = APIRouter()

# Dependencia DB
def get_db():
    db = config.db.SessionLocal()
    try:
        yield db
    finally:
        db.close()

# GET - Listar todos los registros
@router.get("/vehiculos-servicios-usuarios", response_model=list[schemas.schema_vehiculos_servicios_usuarios.VehiculoServicioUsuario])
def get_vehiculos_servicios_usuarios(db: Session = Depends(get_db)):
    registros = crud.crud_vehiculos_servicios_usuarios.get_all(db)
    if not registros:
        raise HTTPException(status_code=404, detail="No se encontraron registros")
    return registros
