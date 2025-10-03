# Usamos la versión oficial de Node.js
FROM node:20-alpine

# Creamos directorio de trabajo
WORKDIR /usr/src/app

# Copiamos package.json y package-lock.json para instalar dependencias
COPY Backend/package*.json ./

# Instalamos dependencias
RUN npm install --production

# Copiamos el resto del código
COPY Backend/. .

# Instalar dotenv para que Node.js lea el .env
RUN npm install dotenv --production

# Exponemos el puerto en el que corre la app
EXPOSE 8002

# Comando para iniciar la app
CMD ["npm", "start"]
