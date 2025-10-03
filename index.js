const express = require("express");
const cors = require("cors");
const morgan = require("morgan");
require("dotenv").config();

const connectDB = require("./config/db");
const errorHandler = require("./middlewares/errorHandler");

// Rutas
const clienteRoutes = require("./routes/ClienteFinalRoutes");
const pedidoRoutes = require("./routes/PedidosRoutes");
const detalleRoutes = require("./routes/DetallePedidoRoutes");
const pruebaRoutes = require("./routes/PruebaEntregaRoutes");

// Inicializar app
const app = express();
const PORT = process.env.PORT || 3000;

// Config
app.use(express.json());
app.use(cors());
app.use(morgan("dev"));

// Conexión a BD
connectDB();

// Endpoints
app.use("/clientes", clienteRoutes);
app.use("/pedidos", pedidoRoutes);
app.use("/detalles", detalleRoutes);
app.use("/pruebas", pruebaRoutes);

app.get("/", (req, res) => {
  res.json({ message: "API funcionando" });
});

// Errores
app.use(errorHandler);

// Iniciar servidor
app.listen(PORT, () => {
  console.log(`Servidor corriendo en http://${procces.env.HOST}:${PORT}, con BD en: ` + process.env.MONGO_URI);
});
