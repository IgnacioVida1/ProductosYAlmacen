const express = require("express");
const router = express.Router();
const ClienteController = require("../controllers/ClienteFinalController");

router.get("/:id", ClienteController.consultarClienteId);
router.get("/", ClienteController.consultarClientes);
router.post("/", ClienteController.registrarCliente);
router.put("/:id", ClienteController.actualizarCliente);
router.delete("/:id", ClienteController.borrarCliente);

module.exports = router;
