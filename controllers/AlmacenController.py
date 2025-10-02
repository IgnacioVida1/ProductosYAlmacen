from sqlalchemy.orm import Session
from clases import Almacen
from typing import List, Optional

class AlmacenController:
    def __init__(self, db: Session):
        self.db = db
    
    def registrar_almacen(self, id_agenteAliado: Optional[int], 
                         nombre: str, ubicacion: str, capacidad: int, tipo: str) -> Almacen:
        """Registrar un nuevo almacén"""
        try:
            nuevo_almacen = Almacen(
                id_agenteAliado=id_agenteAliado,
                nombre=nombre,
                ubicacion=ubicacion,
                capacidad=capacidad,
                tipo=tipo
            )
            self.db.add(nuevo_almacen)
            self.db.commit()
            self.db.refresh(nuevo_almacen)
            return nuevo_almacen
        except Exception as e:
            self.db.rollback()
            raise e
    
    def actualizar_almacen(self, id_almacen: int, **kwargs) -> Optional[Almacen]:
        """Actualizar un almacén existente"""
        try:
            almacen = self.db.query(Almacen).filter(Almacen.id_almacen == id_almacen).first()
            if not almacen:
                return None
            
            for key, value in kwargs.items():
                if hasattr(almacen, key) and value is not None:
                    setattr(almacen, key, value)
            
            self.db.commit()
            self.db.refresh(almacen)
            return almacen
        except Exception as e:
            self.db.rollback()
            raise e
    
    def consultar_almacen(self, id_almacen: int) -> Optional[Almacen]:
        """Consultar un almacén por ID"""
        return self.db.query(Almacen).filter(Almacen.id_almacen == id_almacen).first()
    
    def consultar_todos_almacenes(self) -> List[Almacen]:
        """Consultar todos los almacenes"""
        return self.db.query(Almacen).all()
    
    def consultar_stock(self, id_almacen: int) -> List:
        """Consultar stock de un almacén (con inventario)"""
        from clases import Inventario, Producto
        return (self.db.query(Inventario, Producto)
                .join(Producto, Inventario.id_producto == Producto.id_producto)
                .filter(Inventario.id_almacen == id_almacen)
                .all())