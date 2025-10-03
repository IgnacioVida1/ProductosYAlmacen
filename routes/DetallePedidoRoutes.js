const express = require("express");
const router = express.Router();
const DetalleController = require("../controllers/DetallePedidoController");

router.post("/", DetalleController.agregarDetalle);
router.put("/:id", DetalleController.actualizarDetalle);
router.get("/:id", DetalleController.consultarPedidoId);
router.get("/", DetalleController.consultarPedidos);
router.delete("/:id", DetalleController.borrarPedido);

module.exports = router;