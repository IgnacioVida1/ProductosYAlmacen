from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from config.database import get_db
from controllers.ProductoController import ProductoController
from pydantic import BaseModel
from typing import List, Optional

router = APIRouter(prefix="/productos", tags=["productos"])

# Schemas de Pydantic
class ProductoCreate(BaseModel):
    nombre: str
    descripcion: Optional[str] = None
    peso: Optional[float] = None
    volumen: Optional[float] = None
    sku: str
    precio: float

class ProductoUpdate(BaseModel):
    nombre: Optional[str] = None
    descripcion: Optional[str] = None
    peso: Optional[float] = None
    volumen: Optional[float] = None
    precio: Optional[float] = None

class ProductoResponse(BaseModel):
    id_producto: int
    nombre: str
    descripcion: Optional[str]
    peso: Optional[float]
    volumen: Optional[float]
    sku: str
    precio: float

    class Config:
        from_attributes = True

@router.post("/", response_model=ProductoResponse, status_code=status.HTTP_201_CREATED)
def crear_producto(producto: ProductoCreate, db: Session = Depends(get_db)):
    """Crear un nuevo producto"""
    controller = ProductoController(db)
    try:
        nuevo_producto = controller.crear_producto(
            nombre=producto.nombre,
            descripcion=producto.descripcion,
            peso=producto.peso,
            volumen=producto.volumen,
            sku=producto.sku,
            precio=producto.precio
        )
        return nuevo_producto
    except Exception as e:
        raise HTTPException(status_code=400, detail=f"Error al crear producto: {str(e)}")

@router.put("/{id_producto}", response_model=ProductoResponse)
def actualizar_producto(id_producto: int, producto: ProductoUpdate, db: Session = Depends(get_db)):
    """Actualizar un producto existente"""
    controller = ProductoController(db)
    try:
        producto_actualizado = controller.actualizar_producto(
            id_producto=id_producto,
            **producto.model_dump(exclude_unset=True)
        )
        if not producto_actualizado:
            raise HTTPException(status_code=404, detail="Producto no encontrado")
        return producto_actualizado
    except Exception as e:
        raise HTTPException(status_code=400, detail=f"Error al actualizar producto: {str(e)}")

@router.delete("/{id_producto}")
def eliminar_producto(id_producto: int, db: Session = Depends(get_db)):
    """Eliminar un producto"""
    controller = ProductoController(db)
    try:
        if controller.eliminar_producto(id_producto):
            return {"message": "Producto eliminado exitosamente"}
        else:
            raise HTTPException(status_code=404, detail="Producto no encontrado")
    except Exception as e:
        raise HTTPException(status_code=400, detail=f"Error al eliminar producto: {str(e)}")

@router.get("/{id_producto}", response_model=ProductoResponse)
def consultar_producto(id_producto: int, db: Session = Depends(get_db)):
    """Consultar un producto por ID"""
    controller = ProductoController(db)
    producto = controller.consultar_producto(id_producto)
    if not producto:
        raise HTTPException(status_code=404, detail="Producto no encontrado")
    return producto

@router.get("/", response_model=List[ProductoResponse])
def consultar_todos_productos(db: Session = Depends(get_db)):
    """Consultar todos los productos"""
    controller = ProductoController(db)
    return controller.consultar_todos_productos()

@router.get("/sku/{sku}", response_model=ProductoResponse)
def buscar_producto_por_sku(sku: str, db: Session = Depends(get_db)):
    """Buscar producto por SKU"""
    controller = ProductoController(db)
    producto = controller.buscar_producto_por_sku(sku)
    if not producto:
        raise HTTPException(status_code=404, detail="Producto con ese SKU no encontrado")
    return producto