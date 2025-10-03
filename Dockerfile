FROM node:20-alpine

# Directorio de la app
WORKDIR /usr/src/app

# Copiar archivos de dependencias
COPY package*.json ./

# Instalar dependencias de producción
RUN npm ci --only=production

# Copiar el resto del código
COPY . .

# Exponer el puerto
EXPOSE 8002

# Comando de inicio (usa el script "start" del package.json)
CMD ["node", "index.js"]
