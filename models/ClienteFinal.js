const mongoose = require('mongoose');

const ClienteFinalSchema = new mongoose.Schema({
    nombre: {type: String, required: true},
    email: {type: String, required: true, unique: true},
    telefono: {type: String, required: true},
    direccion: {type: String, required: true}
}, {timestamps: true});

module.exports = mongoose.model('ClienteFinal', ClienteFinalSchema);
