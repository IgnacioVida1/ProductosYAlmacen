from sqlalchemy.orm import Session
from clases import Inventario, Producto, Almacen
from typing import List, Optional
from datetime import datetime

class InventarioController:
    def __init__(self, db: Session):
        self.db = db
    
    def actualizar_stock(self, id_inventario: int, stock_disponible: int, 
                        stock_reservado: int = None) -> Optional[Inventario]:
        """Actualizar stock de un inventario"""
        try:
            inventario = self.db.query(Inventario).filter(Inventario.id_inventario == id_inventario).first()
            if not inventario:
                return None
            
            inventario.stock_disponible = stock_disponible
            if stock_reservado is not None:
                inventario.stock_reservado = stock_reservado
            inventario.ultima_actualizacion = datetime.now()
            
            self.db.commit()
            self.db.refresh(inventario)
            return inventario
        except Exception as e:
            self.db.rollback()
            raise e
    
    def reservar_producto(self, id_inventario: int, cantidad: int) -> bool:
        """Reservar producto (mover stock disponible a reservado)"""
        try:
            inventario = self.db.query(Inventario).filter(Inventario.id_inventario == id_inventario).first()
            if not inventario:
                return False
            
            if inventario.stock_disponible < cantidad:
                return False
            
            inventario.stock_disponible -= cantidad
            inventario.stock_reservado += cantidad
            inventario.ultima_actualizacion = datetime.now()
            
            self.db.commit()
            return True
        except Exception as e:
            self.db.rollback()
            raise e
    
    def liberar_reserva(self, id_inventario: int, cantidad: int) -> bool:
        """Liberar reserva (mover stock reservado a disponible)"""
        try:
            inventario = self.db.query(Inventario).filter(Inventario.id_inventario == id_inventario).first()
            if not inventario:
                return False
            
            if inventario.stock_reservado < cantidad:
                return False
            
            inventario.stock_reservado -= cantidad
            inventario.stock_disponible += cantidad
            inventario.ultima_actualizacion = datetime.now()
            
            self.db.commit()
            return True
        except Exception as e:
            self.db.rollback()
            raise e
    
    def crear_inventario(self, id_almacen: int, id_producto: int, 
                        stock_disponible: int = 0, stock_reservado: int = 0) -> Inventario:
        """Crear un nuevo registro de inventario"""
        try:
            nuevo_inventario = Inventario(
                id_almacen=id_almacen,
                id_producto=id_producto,
                stock_disponible=stock_disponible,
                stock_reservado=stock_reservado
            )
            self.db.add(nuevo_inventario)
            self.db.commit()
            self.db.refresh(nuevo_inventario)
            return nuevo_inventario
        except Exception as e:
            self.db.rollback()
            raise e
    
    def consultar_inventario(self, id_inventario: int) -> Optional[Inventario]:
        """Consultar inventario por ID"""
        return self.db.query(Inventario).filter(Inventario.id_inventario == id_inventario).first()
    
    def consultar_inventario_por_almacen(self, id_almacen: int) -> List[Inventario]:
        """Consultar inventario de un almacén"""
        return self.db.query(Inventario).filter(Inventario.id_almacen == id_almacen).all()
    
    def consultar_inventario_por_producto(self, id_producto: int) -> List[Inventario]:
        """Consultar inventario de un producto en todos los almacenes"""
        return self.db.query(Inventario).filter(Inventario.id_producto == id_producto).all()
    
    def consultar_stock_total_producto(self, id_producto: int) -> dict:
        """Consultar stock total de un producto en todos los almacenes"""
        inventarios = self.consultar_inventario_por_producto(id_producto)
        total_disponible = sum(inv.stock_disponible for inv in inventarios)
        total_reservado = sum(inv.stock_reservado for inv in inventarios)
        
        return {
            "id_producto": id_producto,
            "stock_total_disponible": total_disponible,
            "stock_total_reservado": total_reservado,
            "stock_por_almacen": [
                {
                    "id_almacen": inv.id_almacen,
                    "stock_disponible": inv.stock_disponible,
                    "stock_reservado": inv.stock_reservado
                } for inv in inventarios
            ]
        }