const mongoose = require('mongoose');

const PruebaEntregaSchema = new mongoose.Schema({
    id_pedido: {type: mongoose.Schema.Types.ObjectId, ref: 'Pedido', required: true},
    foto_entrega: {type: String, required: true},
    firma_cliente: {type: String, required: true},
    otp_codigo: {type: String, required: true}
}, {timestamps: true});

module.exports = mongoose.model('PruebaEntrega', PruebaEntregaSchema);
