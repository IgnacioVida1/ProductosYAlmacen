const PruebaEntrega = require('../models/PruebaEntrega.js');
const Pedido = require('../models/Pedido.js');

const generarOTP = () => Math.floor(100000 + Math.random() * 900000).toString();

exports.registrarEntrega = async (req, res, next) => {
    try {
        const otp = generarOTP();
        const prueba = await PruebaEntrega.create({
            id_pedido: req.params.id,
            foto_entrega: req.body.foto_entrega,
            firma_cliente: req.body.firma_cliente,
            otp_codigo: otp
        });
        res.status(201).json(prueba);
    } catch (err) {
        next(err);
    }
};

exports.validarEntrega = async (req, res, next) => {
    try {
        const { otp } = req.body;
        const { id } = req.params;
        const prueba = await PruebaEntrega.findById(id);
        if (!prueba) { return res.status(404).json({error: 'Prueba de entrega no encontrada'}); }
        if (prueba.otp_codigo !== otp) { return res.status(400).json({error: 'OTP incorrecto'}); }
        const pedido = await Pedido.findByIdAndUpdate(
            prueba.id_pedido,
            { estado: "entregado" },
            { new: true } // devuelve el documento actualizado
        );
        if (!pedido) { return res.status(404).json({error: 'Pedido no encontrado'}); }
        res.json({message: 'Pedido marcado como entregado'});
    } catch (err) {
        next(err);
    }
};

