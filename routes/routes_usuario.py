from fastapi import APIRouter, HTTPException, Depends
from sqlalchemy.orm import Session 
import crud.crud_usuario, config.db, schemas.schema_usuario, models.model_usuario

router = APIRouter()

# Dependencia para la DB
def get_db():
    db = config.db.SessionLocal()
    try:
        yield db
    finally:
        db.close()

# GET - Listar todos los usuarios
@router.get("/usuarios", response_model=list[schemas.schema_usuario.Usuario])
def get_usuarios(db: Session = Depends(get_db)):
    usuarios = crud.crud_usuario.get_usuarios(db)
    if not usuarios:
        raise HTTPException(status_code=404, detail="No se encontraron usuarios")
    return usuarios
