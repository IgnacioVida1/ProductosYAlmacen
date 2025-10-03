const mongoose = require('mongoose');

const DetallePedidoSchema = new mongoose.Schema({
    id_pedido: {type: mongoose.Schema.Types.ObjectId, ref: 'Pedido', required: true},
    id_producto: {type: String, required: true},
    cantidad: {type: Number, required: true},
    precio_unitario: {type: Number, required: true}
}, {timestamps: true});

module.exports = mongoose.model('DetallePedido', DetallePedidoSchema);