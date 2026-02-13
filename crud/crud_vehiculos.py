import models.model_rol
import models.model_vehiculos
from sqlalchemy.orm import Session

def get_rol(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.model_vehiculos.Vehiculo).offset(skip).limit(limit).all()

