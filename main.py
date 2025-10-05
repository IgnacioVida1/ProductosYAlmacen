from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from config.database import create_tables, test_connection
from routes import ProductoRoutes, AlmacenRoutes, InventarioRoutes
import uvicorn

# Crear la aplicación FastAPI
app = FastAPI(
    title="Microservicio Productos y Almacenes",
    description="API para gestión de productos, almacenes e inventario",
    version="1.0.0",
    docs_url="/docs",
    redoc_url="/redoc"
)

# Configurar CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Incluir las rutas
app.include_router(ProductoRoutes.router, prefix="/api/v1")
app.include_router(AlmacenRoutes.router, prefix="/api/v1")
app.include_router(InventarioRoutes.router, prefix="/api/v1")

@app.on_event("startup")
async def startup_event():
    """Eventos que se ejecutan al iniciar la aplicación"""
    print("🚀 Iniciando Microservicio Productos y Almacenes...")
    
    # Verificar conexión a la base de datos
    print("🔗 Verificando conexión a MySQL...")
    if test_connection():
        print("Conexión a MySQL exitosa")
        
        # Crear tablas si no existen
        print("🛠️ Creando tablas en la base de datos...")
        try:
            create_tables()
            print("Tablas creadas/verificadas exitosamente")
        except Exception as e:
            print(f"Error al crear tablas: {e}")
    else:
        print("Error de conexión a MySQL")

@app.get("/")
async def root():
    """Endpoint raíz"""
    return {
        "message": "Microservicio Productos y Almacenes",
        "version": "1.0.0",
        "status": "running",
        "endpoints": {
            "docs": "/docs",
            "redoc": "/redoc",
            "productos": "/api/v1/productos",
            "almacenes": "/api/v1/almacenes",
            "inventario": "/api/v1/inventario"
        }
    }

@app.get("/health")
async def health_check():
    """Endpoint de verificación de salud"""
    try:
        db_status = test_connection()
        return {
            "status": "healthy" if db_status else "unhealthy",
            "database": "connected" if db_status else "disconnected",
            "service": "productos-almacenes"
        }
    except Exception as e:
        raise HTTPException(status_code=503, detail=f"Service unhealthy: {str(e)}")

if __name__ == "__main__":
    uvicorn.run(
        "main:app",
        host="0.0.0.0",
        port=8000,
        reload=True,
        log_level="info"
    )