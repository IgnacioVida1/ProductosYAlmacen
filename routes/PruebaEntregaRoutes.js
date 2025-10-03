const express = require("express");
const router = express.Router();
const PruebaController = require("../controllers/PruebaEntregaController");

router.post("/", PruebaController.registrarEntrega);
router.patch("/:id/validar", PruebaController.validarEntrega);

module.exports = router;