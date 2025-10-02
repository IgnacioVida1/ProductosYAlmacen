from sqlalchemy.orm import Session
from clases import Producto
from typing import List, Optional

class ProductoController:
    def __init__(self, db: Session):
        self.db = db
    
    def crear_producto(self, nombre: str, descripcion: str, 
                      peso: float, volumen: float, sku: str, precio: float) -> Producto:
        """Crear un nuevo producto"""
        try:
            nuevo_producto = Producto(
                nombre=nombre,
                descripcion=descripcion,
                peso=peso,
                volumen=volumen,
                sku=sku,
                precio=precio
            )
            self.db.add(nuevo_producto)
            self.db.commit()
            self.db.refresh(nuevo_producto)
            return nuevo_producto
        except Exception as e:
            self.db.rollback()
            raise e
    
    def actualizar_producto(self, id_producto: int, **kwargs) -> Optional[Producto]:
        """Actualizar un producto existente"""
        try:
            producto = self.db.query(Producto).filter(Producto.id_producto == id_producto).first()
            if not producto:
                return None
            
            for key, value in kwargs.items():
                if hasattr(producto, key) and value is not None:
                    setattr(producto, key, value)
            
            self.db.commit()
            self.db.refresh(producto)
            return producto
        except Exception as e:
            self.db.rollback()
            raise e
    
    def eliminar_producto(self, id_producto: int) -> bool:
        """Eliminar un producto"""
        try:
            producto = self.db.query(Producto).filter(Producto.id_producto == id_producto).first()
            if not producto:
                return False
            
            self.db.delete(producto)
            self.db.commit()
            return True
        except Exception as e:
            self.db.rollback()
            raise e
    
    def consultar_producto(self, id_producto: int) -> Optional[Producto]:
        """Consultar un producto por ID"""
        return self.db.query(Producto).filter(Producto.id_producto == id_producto).first()
    
    def consultar_todos_productos(self) -> List[Producto]:
        """Consultar todos los productos"""
        return self.db.query(Producto).all()
    
    def buscar_producto_por_sku(self, sku: str) -> Optional[Producto]:
        """Buscar producto por SKU"""
        return self.db.query(Producto).filter(Producto.sku == sku).first()