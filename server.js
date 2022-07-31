// forma de usar las librerias con ECMAScript
import express from "express";
import dotenv from "dotenv";

// Buscara el archivo .env y seteara las variables definidas en ese archivo como variables de entorno
dotenv.config()
// forma de usar las librerias con CommonjS
// const express = require("express")

const servidor = express();
const PORT = process.env.PORT; //Esto generalmente es 3000 pero puede ser cualquier valor
// indicamos que nuestro servidor podra aceptar y entender la informacion enviada en formato JSON
servidor.use(express.json())

const categories =[{
    name: "Zapatos",
    description : "Zapatos para hombres,mujeres y niños"
}]
servidor.get("/",(req,res)=>{
    res.status(200).json({
        message: "Bienvenido a mi primera API",
    });
})

servidor.route("/categories").get((req,res)=>{
    return res.status(200).json({categories});
})
.post((req,res)=>{
    const category = req.body

    // agregara la nueva categoria al listado de categorias
    categories.push(category)

    return res.status(201).json({
        message: "Category created Successfully",
        content: category
    })
})

servidor.route("/categories/:id").get((req,res)=>{
    console.log(req.params)
    const {id} = req.params

    if(categories[id] !==undefined){
        return res.json({
            message: "La categoria es",
            content: categories[id]
        })
    }else{
        return res.status(400).json({
            messge : "La categoria no existe",
            content:null
        })
    }
    return res.json({
        message: "La categoria es"
    })
})
servidor.listen(PORT,()=>{
    console.log (`Servidor corriendo exitosamente en el puerto ${PORT}`)
})