# Microservicio 2 — Logística y Transporte (Spring Boot + PostgreSQL)

Resumen del proyecto, cómo construir y ejecutar.

## Construir y ejecutar

1. `mvn clean package` (o `./mvnw clean package`)
2. `docker-compose up --build`
3. Swagger: http://localhost:8081/swagger-ui.html

## Endpoints
- POST /api/agentes
- GET /api/agentes/{id}
- PUT /api/agentes/{id}/almacen/{idAlmacen}
- PUT /api/agentes/{id}/conductor/{idConductor}
- POST /api/vehiculos
- GET /api/vehiculos/{id}
- PUT /api/vehiculos/{id}/asignarConductor/{idConductor}
- POST /api/conductores
- GET /api/conductores/{id}
- GET /api/conductores/disponibles
