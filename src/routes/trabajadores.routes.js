import {Router} from "express"
import {postRegistro,validarTrabajador,cambiarPassword} from "../controllers/trabajadores.controllers.js"

export const trabajadoresRouter = Router()

trabajadoresRouter.post("/registro", postRegistro)
trabajadoresRouter.post("/validar-trabajador",validarTrabajador)
trabajadoresRouter.post("/cambiar-password",cambiarPassword)