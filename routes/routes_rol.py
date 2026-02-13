from fastapi import APIRouter, HTTPException, Depends
from sqlalchemy.orm import Session
import crud.crud_rol, config.db, schemas.schema_rol, models.model_rol

router = APIRouter()

# Dependencia para obtener la sesión de la base de datos
def get_db():
    db = config.db.SessionLocal()
    try:
        yield db
    finally:
        db.close()

# GET - Obtener todos los roles
@router.get("/roles", response_model=list[schemas.schema_rol.Rol])
def get_roles(db: Session = Depends(get_db)):
    roles = crud.crud_rol.get_roles(db)
    if not roles:
        raise HTTPException(status_code=404, detail="No se encontraron roles")
    return roles
