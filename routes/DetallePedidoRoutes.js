const express = require("express");
const router = express.Router();
const DetalleController = require("../controllers/DetallePedidoController");

router.post("/", DetalleController.agregarDetalle);
router.put("/:id", DetalleController.actualizarDetalle);
router.get("/:id", DetalleController.consultarDetalleId);
router.get("/", DetalleController.consultarDetalles);
router.delete("/:id", DetalleController.borrarDetalle);

module.exports = router;