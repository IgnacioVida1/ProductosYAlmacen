const mongoose = require('mongoose');

const PedidoSchema = new mongoose.Schema({
    id_cliente_final: {type: mongoose.Schema.Types.ObjectId, ref: 'ClienteFinal', required: true},
    estado: {type: String, enum: ['pendiente', 'enviado', 'entregado'], default: 'pendiente'},
    monto_total: {type: Number, required: true},
    direccion_entrega: {type: String, required: true},
    ventana_horaria: {type: String, enum: ['mañana', 'mediodia', 'tarde', 'noche', 'todo el dia', '24 horas'], required: true}
}, {timestamps: true});

module.exports = mongoose.model('Pedido', PedidoSchema);
