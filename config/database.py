from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base
import os
from dotenv import load_dotenv

# Cargar variables de entorno
load_dotenv()

# Configuración de la base de datos MySQL
DATABASE_URL = os.getenv(
    "DATABASE_URL", 
    "mysql+pymysql://root:password@localhost:3306/productos_almacenes"
)

# Crear engine de SQLAlchemy
engine = create_engine(
    DATABASE_URL,
    echo=True,  
    pool_pre_ping=True,  
    pool_recycle=300,  
)

# Crear SessionLocal para manejar sesiones de BD
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Base para los modelos
Base = declarative_base()

# Dependencia para obtener la sesión de BD
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

# Función para crear las tablas
def create_tables():
    from clases import Base
    Base.metadata.create_all(bind=engine)
    print("Tablas creadas exitosamente")

# Función para verificar conexión
def test_connection():
    try:
        with engine.connect() as connection:
            print("Conexión a MySQL exitosa")
            return True
    except Exception as e:
        print(f"Error de conexión: {e}")
        return False