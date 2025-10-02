from sqlalchemy import Column, Integer, String, Float, ForeignKey, DateTime
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.sql import func

Base = declarative_base()


class Producto(Base):
    __tablename__ = "Producto"

    id_producto = Column(Integer, primary_key=True, index=True)
    nombre = Column(String(100), nullable=False)
    descripcion = Column(String(255))
    peso = Column(Float)
    volumen = Column(Float)
    sku = Column(String(50), unique=True, nullable=False)
    precio = Column(Float, nullable=False)

class Almacen(Base):
    __tablename__ = "Almacen"

    id_almacen = Column(Integer, primary_key=True, index=True)
    id_agenteAliado = Column(Integer, nullable=True)
    nombre = Column(String(100), nullable=False)
    ubicacion = Column(String(150), nullable=False)
    capacidad = Column(Integer, nullable=False)
    tipo = Column(String(50), nullable=False)

class Inventario(Base):
    __tablename__ = "Inventario"

    id_inventario = Column(Integer, primary_key=True, index=True)
    id_almacen = Column(Integer, ForeignKey("Almacen.id_almacen"), nullable=False)
    id_producto = Column(Integer, ForeignKey("Producto.id_producto"), nullable=False)
    stock_disponible = Column(Integer, nullable=False, default=0)
    stock_reservado = Column(Integer, nullable=False, default=0)
    ultima_actualizacion = Column(DateTime, default=func.now(), onupdate=func.now())