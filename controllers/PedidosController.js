const Pedido = require('../models/Pedido');

exports.crearPedido = async (req, res, next) => {
    try {
        const pedido_nuevo = new Pedido(req.body);
        await pedido_nuevo.save();
        res.status(201).json(pedido_nuevo);
    } catch (err) {
        next(err);
    }
};

exports.actualizarPedido = async (req, res, next) => {
    try {
        const pedido = await Pedido.findByIdAndUpdate(req.params.id, req.body, {new: true});
        if (!pedido) {
            return res.status(404).json({error: 'Pedido no encontrado'});
        }
        res.json(pedido);
    } catch (err) {
        next(err);
    }
};

exports.consultarPedidoId = async (req, res, next) => {
    try {
        const pedido = await Pedido.findById(req.params.id, {__v: false});
        if (!pedido) {
            return res.status(404).json({error: 'Pedido no encontrado'});
        }
        res.json(pedido);
    } catch (err) {
        next(err);
    }
};

exports.consultarPedidos = async (req, res, next) => {
    try {
        const pedidos = await Pedido.find({}, {__v: false});
        res.json(pedidos);
    } catch (err) {
        next(err);
    }
};

exports.borrarPedido = async (req, res, next) => {
    try {
        const pedido = await Pedido.findByIdAndDelete(req.params.id, {__v: false});
        if (!pedido) {
            return res.status(404).json({error: 'Pedido no encontrado'});
        }
        res.json({message: 'Pedido eliminado'});
    } catch (err) {
        next(err);
    }
};
