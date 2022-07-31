// forma de usar las librerias con ECMAScript
import express from "express";
import dotenv from "dotenv";

// Buscara el archivo .env y seteara las variables definidas en ese archivo como variables de entorno
dotenv.config()
// forma de usar las librerias con CommonjS
// const express = require("express")

const servidor = express();
const PORT = process.env.PORT; //Esto generalmente es 3000 pero puede ser cualquier valor

servidor.listen(PORT,()=>{
    console.log (`Servidor corriendo exitosamente en el puerto ${PORT}`)
})