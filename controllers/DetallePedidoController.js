const DetallePedido = require('../models/DetallePedido');

exports.agregarDetalle = async (req, res, next) => {
    try {
        const detalle_nuevo = new DetallePedido({...req.body, id_pedido: req.params.id});
        await detalle_nuevo.save();
        res.status(201).json(detalle_nuevo);
    } catch (err) {
        next(err);
    }
};

exports.actualizarDetalle = async (req, res, next) => {
    try {
        const detalle = await DetallePedido.findByIdAndUpdate(req.params.id, req.body, {new: true});
        if (!detalle) {
            return res.status(404).json({error: 'Detalle del pedido no encontrado'});
        }
        res.json(detalle);
    } catch (err) {
        next(err);
    }
};

exports.consultarDetalleId = async (req, res, next) => {
    try {
        const detalle = await DetallePedido.findById(req.params.id, {__v: false});
        if (!detalle) {
            return res.status(404).json({error: 'Detalle del pedido no encontrado'});
        }
        res.json(detalle);
    } catch (err) {
        next(err);
    }
};

exports.consultarDetalles = async (req, res, next) => {
    try {
        const detalles = await DetallePedido.find({}, {__v: false});
        res.json(detalles);
    } catch (err) {
        next(err);
    }
};

exports.borrarPedido = async (req, res, next) => {
    try {
        const detalle = await DetallePedido.findByIdAndDelete(req.params.id, {__v: false});
        if (!detalle) {
            return res.status(404).json({error: 'Detalle del pedido no encontrado'});
        }
        res.json({message: 'Detalle del pedido eliminado'});
    } catch (err) {
        next(err);
    }
};
