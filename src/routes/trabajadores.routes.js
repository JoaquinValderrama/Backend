import {Router} from "express"
import {postRegistro} from "../controllers/trabajadores.controllers.js"

export const trabajadoresRouter = Router()

trabajadoresRouter.post("/registro", postRegistro)