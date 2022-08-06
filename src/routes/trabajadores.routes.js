import {Router} from "express"
import {postRegistro,validarTrabajador,cambiarPassword,login,perfil} from "../controllers/trabajadores.controllers.js"
import { isGerente, verificarToken } from "../utils/validador.js"

export const trabajadoresRouter = Router()

trabajadoresRouter.post("/registro",verificarToken,isGerente,postRegistro)
trabajadoresRouter.post("/validar-trabajador",validarTrabajador)
trabajadoresRouter.post("/cambiar-password",cambiarPassword)
trabajadoresRouter.post("/login",login)
trabajadoresRouter.get("/me",verificarToken,perfil)