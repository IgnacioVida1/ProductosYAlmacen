from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from config.database import get_db
from controllers.AlmacenController import AlmacenController
from pydantic import BaseModel
from typing import List, Optional

router = APIRouter(prefix="/almacenes", tags=["almacenes"])

# Schemas de Pydantic
class AlmacenCreate(BaseModel):
    id_agenteAliado: Optional[int] = None
    nombre: str
    ubicacion: str
    capacidad: int
    tipo: str

class AlmacenUpdate(BaseModel):
    id_agenteAliado: Optional[int] = None
    nombre: Optional[str] = None
    ubicacion: Optional[str] = None
    capacidad: Optional[int] = None
    tipo: Optional[str] = None

class AlmacenResponse(BaseModel):
    id_almacen: int
    id_agenteAliado: Optional[int]
    nombre: str
    ubicacion: str
    capacidad: int
    tipo: str

    class Config:
        from_attributes = True

@router.post("/", response_model=AlmacenResponse, status_code=status.HTTP_201_CREATED)
def registrar_almacen(almacen: AlmacenCreate, db: Session = Depends(get_db)):
    """Registrar un nuevo almacén"""
    controller = AlmacenController(db)
    try:
        nuevo_almacen = controller.registrar_almacen(
            id_agenteAliado=almacen.id_agenteAliado,
            nombre=almacen.nombre,
            ubicacion=almacen.ubicacion,
            capacidad=almacen.capacidad,
            tipo=almacen.tipo
        )
        return nuevo_almacen
    except Exception as e:
        raise HTTPException(status_code=400, detail=f"Error al crear almacén: {str(e)}")

@router.put("/{id_almacen}", response_model=AlmacenResponse)
def actualizar_almacen(id_almacen: int, almacen: AlmacenUpdate, db: Session = Depends(get_db)):
    """Actualizar un almacén existente"""
    controller = AlmacenController(db)
    try:
        almacen_actualizado = controller.actualizar_almacen(
            id_almacen=id_almacen,
            **almacen.model_dump(exclude_unset=True)
        )
        if not almacen_actualizado:
            raise HTTPException(status_code=404, detail="Almacén no encontrado")
        return almacen_actualizado
    except Exception as e:
        raise HTTPException(status_code=400, detail=f"Error al actualizar almacén: {str(e)}")

@router.get("/{id_almacen}", response_model=AlmacenResponse)
def consultar_almacen(id_almacen: int, db: Session = Depends(get_db)):
    """Consultar un almacén por ID"""
    controller = AlmacenController(db)
    almacen = controller.consultar_almacen(id_almacen)
    if not almacen:
        raise HTTPException(status_code=404, detail="Almacén no encontrado")
    return almacen

@router.get("/", response_model=List[AlmacenResponse])
def consultar_todos_almacenes(db: Session = Depends(get_db)):
    """Consultar todos los almacenes"""
    controller = AlmacenController(db)
    return controller.consultar_todos_almacenes()

@router.get("/{id_almacen}/stock")
def consultar_stock(id_almacen: int, db: Session = Depends(get_db)):
    """Consultar stock de un almacén"""
    controller = AlmacenController(db)
    try:
        stock = controller.consultar_stock(id_almacen)
        return {
            "id_almacen": id_almacen,
            "productos": [
                {
                    "id_inventario": inventario.id_inventario,
                    "id_producto": inventario.id_producto,
                    "nombre_producto": producto.nombre,
                    "sku": producto.sku,
                    "stock_disponible": inventario.stock_disponible,
                    "stock_reservado": inventario.stock_reservado,
                    "ultima_actualizacion": inventario.ultima_actualizacion
                }
                for inventario, producto in stock
            ]
        }
    except Exception as e:
        raise HTTPException(status_code=400, detail=f"Error al consultar stock: {str(e)}")