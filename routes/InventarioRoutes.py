from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from config.database import get_db
from controllers.InventarioController import InventarioController
from pydantic import BaseModel
from typing import List, Optional
from datetime import datetime

router = APIRouter(prefix="/inventario", tags=["inventario"])

# Schemas de Pydantic
class InventarioCreate(BaseModel):
    id_almacen: int
    id_producto: int
    stock_disponible: int = 0
    stock_reservado: int = 0

class InventarioUpdate(BaseModel):
    stock_disponible: Optional[int] = None
    stock_reservado: Optional[int] = None

class ReservaRequest(BaseModel):
    cantidad: int

class InventarioResponse(BaseModel):
    id_inventario: int
    id_almacen: int
    id_producto: int
    stock_disponible: int
    stock_reservado: int
    ultima_actualizacion: Optional[datetime]

    class Config:
        from_attributes = True

@router.post("/", response_model=InventarioResponse, status_code=status.HTTP_201_CREATED)
def crear_inventario(inventario: InventarioCreate, db: Session = Depends(get_db)):
    """Crear un nuevo registro de inventario"""
    controller = InventarioController(db)
    try:
        nuevo_inventario = controller.crear_inventario(
            id_almacen=inventario.id_almacen,
            id_producto=inventario.id_producto,
            stock_disponible=inventario.stock_disponible,
            stock_reservado=inventario.stock_reservado
        )
        return nuevo_inventario
    except Exception as e:
        raise HTTPException(status_code=400, detail=f"Error al crear inventario: {str(e)}")

@router.put("/{id_inventario}/stock", response_model=InventarioResponse)
def actualizar_stock(id_inventario: int, update_data: InventarioUpdate, db: Session = Depends(get_db)):
    """Actualizar stock de un inventario"""
    controller = InventarioController(db)
    try:
        inventario_actualizado = controller.actualizar_stock(
            id_inventario=id_inventario,
            stock_disponible=update_data.stock_disponible,
            stock_reservado=update_data.stock_reservado
        )
        if not inventario_actualizado:
            raise HTTPException(status_code=404, detail="Inventario no encontrado")
        return inventario_actualizado
    except Exception as e:
        raise HTTPException(status_code=400, detail=f"Error al actualizar stock: {str(e)}")

@router.post("/{id_inventario}/reservar")
def reservar_producto(id_inventario: int, reserva: ReservaRequest, db: Session = Depends(get_db)):
    """Reservar producto (mover stock disponible a reservado)"""
    controller = InventarioController(db)
    try:
        if controller.reservar_producto(id_inventario, reserva.cantidad):
            return {"message": f"Se reservaron {reserva.cantidad} unidades exitosamente"}
        else:
            raise HTTPException(status_code=400, detail="No hay suficiente stock disponible o inventario no encontrado")
    except Exception as e:
        raise HTTPException(status_code=400, detail=f"Error al reservar producto: {str(e)}")

@router.post("/{id_inventario}/liberar")
def liberar_reserva(id_inventario: int, liberacion: ReservaRequest, db: Session = Depends(get_db)):
    """Liberar reserva (mover stock reservado a disponible)"""
    controller = InventarioController(db)
    try:
        if controller.liberar_reserva(id_inventario, liberacion.cantidad):
            return {"message": f"Se liberaron {liberacion.cantidad} unidades exitosamente"}
        else:
            raise HTTPException(status_code=400, detail="No hay suficiente stock reservado o inventario no encontrado")
    except Exception as e:
        raise HTTPException(status_code=400, detail=f"Error al liberar reserva: {str(e)}")

@router.get("/{id_inventario}", response_model=InventarioResponse)
def consultar_inventario(id_inventario: int, db: Session = Depends(get_db)):
    """Consultar inventario por ID"""
    controller = InventarioController(db)
    inventario = controller.consultar_inventario(id_inventario)
    if not inventario:
        raise HTTPException(status_code=404, detail="Inventario no encontrado")
    return inventario

@router.get("/almacen/{id_almacen}", response_model=List[InventarioResponse])
def consultar_inventario_por_almacen(id_almacen: int, db: Session = Depends(get_db)):
    """Consultar inventario de un almacén"""
    controller = InventarioController(db)
    return controller.consultar_inventario_por_almacen(id_almacen)

@router.get("/producto/{id_producto}", response_model=List[InventarioResponse])
def consultar_inventario_por_producto(id_producto: int, db: Session = Depends(get_db)):
    """Consultar inventario de un producto en todos los almacenes"""
    controller = InventarioController(db)
    return controller.consultar_inventario_por_producto(id_producto)

@router.get("/producto/{id_producto}/total")
def consultar_stock_total_producto(id_producto: int, db: Session = Depends(get_db)):
    """Consultar stock total de un producto en todos los almacenes"""
    controller = InventarioController(db)
    return controller.consultar_stock_total_producto(id_producto)