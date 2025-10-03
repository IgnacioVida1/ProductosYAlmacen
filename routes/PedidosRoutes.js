const express = require("express");
const router = express.Router();
const PedidosController = require("../controllers/PedidosController");

router.post("/", PedidosController.crearPedido);
router.put("/:id", PedidosController.actualizarPedido);
router.get("/:id", PedidosController.consultarPedidoId);
router.get("/", PedidosController.consultarPedidos);
router.delete("/:id", PedidosController.borrarPedido);

module.exports = router;