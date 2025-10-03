# ---------- Stage 1: build ----------
FROM maven:3.9.9-eclipse-temurin-17 AS build
WORKDIR /app

# Copiamos el pom.xml y las dependencias primero (mejora la caché)
COPY pom.xml .
COPY src ./src

# Compilamos y empaquetamos (salta los tests)
RUN mvn clean package -DskipTests

# ---------- Stage 2: runtime ----------
FROM eclipse-temurin:17-jdk-jammy
WORKDIR /app

# Copiamos el JAR desde la etapa de build
COPY --from=build /app/target/*.jar app.jar

# Exponemos el puerto de la aplicación
EXPOSE 8001

# Comando de inicio
ENTRYPOINT ["java", "-jar", "app.jar"]
