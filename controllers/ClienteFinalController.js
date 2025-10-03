const ClienteFinal = require('../models/ClienteFinal');

exports.consultarClienteId = async (req, res, next) => {
    try {
        const cliente = await ClienteFinal.findById(req.params.id, {__v: false});
        if (!cliente) {
            return res.status(404).json({error: 'Cliente final no encontrado'});
        }
        res.json(cliente);
    } catch (err) {
        next(err);
    }
};

exports.consultarClientes = async (req, res, next) => {
    try {
        const clientes = await ClienteFinal.find({}, {__v: false});
        res.json(clientes);
    } catch (err) {
        next(err);
    }
};

exports.registrarCliente = async (req, res, next) => {
    try {
        const cliente_nuevo = new ClienteFinal(req.body);
        await cliente_nuevo.save();
        res.status(201).json(cliente_nuevo);
    } catch (err) {
        next(err);
    }
};

exports.actualizarCliente = async (req, res, next) => {
    try {
        const cliente = await ClienteFinal.findByIdAndUpdate(req.params.id, req.body, {new: true});
        if (!cliente) {
            return res.status(404).json({error: 'Cliente final no encontrado'});
        }
        res.json(cliente);
    } catch (err) {
        next(err);
    }
};

exports.borrarCliente = async (req, res, next) => {
    try {
        const cliente = await ClienteFinal.findByIdAndDelete(req.params.id);
        if (!cliente) {
            return res.status(404).json({error: 'Cliente final no encontrado'});
        }
        res.json({message: 'Cliente final eliminado'});
    } catch (err) {
        next(err);
    }
};
