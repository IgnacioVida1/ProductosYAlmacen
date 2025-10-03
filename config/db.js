const mongoose = require('mongoose');

mongo_url = `mongodb://${process.env.DB_HOST}:${process.env.DB_PORT}/${process.env.DB_NAME}`

const connectDB = async () => {
  try {
    await mongoose.connect(mongo_url, {
      dbName: process.env.DB_NAME,
    });
    console.log("✅ Conectado a MongoDB");
  } catch (err) {
    console.error("❌ Error al conectar a MongoDB:", err.message);
    process.exit(1);
  }
};

module.exports = connectDB;