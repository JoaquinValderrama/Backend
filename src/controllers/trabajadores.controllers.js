import {trabajadoresRequestDTO,cambiarPasswordRequestDTO, loginRequestDTO} from "../dtos/trabajadores.dto.js"
import CryptoJS from "crypto-js"
import bcryptjs from "bcryptjs"
import { PrismaConnector } from "../prisma.js"
import { validarCorreo,cambioPassword } from "../utils/correos.js"
import jwt from 'jsonwebtoken'

export const postRegistro = async(req,res) =>{
    try {
        const {password, ...data} = trabajadoresRequestDTO(req.body)
        const password_encriptada= bcryptjs.hashSync(password,10)

        const resultado = await PrismaConnector.trabajador.create({data: {...data,password:password_encriptada}})

        const horaActual = new Date()
       const token =  CryptoJS.AES.encrypt(JSON.stringify({
            id: resultado.id,
            caducidad: new Date(horaActual.getFullYear(),horaActual.getMonth(),horaActual.getDate(),horaActual.getHours()+2),
            
        }),
        process.env.LLAVE_ENCRIPTACION
        ).toString();

        await validarCorreo({
            destinatario:resultado.email,
            nombre: resultado.nombre,
            token,
        });

        return res.json({
            message: "Usuario registrado exitosamente",
            resultado
        })

    } catch (error) {
        return res.status(400).json({
            message: "Error al crear el usuario",
            result : error.message
        })
    }
}

export const validarTrabajador = async(req,res) =>{
    const {token} = req.body;
    try {
    
        const data = CryptoJS.AES.decrypt(token,process.env.LLAVE_ENCRIPTACION).toString(CryptoJS.enc.Utf8)
        console.log(data)

        if (!data){
            throw new Error("TOKEN NO VALIDO")
        }

        const infoToken = JSON.parse(data)
        console.log(infoToken)

        if(infoToken.caducidad < new Date()){
            throw new Error("LA TOKEN YA VENCIÓ")
        }
        const trabajador = await PrismaConnector.trabajador.findUniqueOrThrow({
            where: {id: infoToken.id},
        })

        if (trabajador.validado){
            throw new Error("Usuario ya fue validado")
        }
        await PrismaConnector.trabajador.update({
            data:{validado:true},
            where:{id:infoToken.id}
        })
        return res.json({
            message: "Trabajador validado exitosamente",
            result: null,
        })    
    } catch (error) {
        return res.status(400).json({
            message: "ERROR, AL VALIDAR LA TOKEN",
            result: error.message
        })
    }
    
}


export const cambiarPassword = async(req,res) =>{
    try {
        const data = cambiarPasswordRequestDTO(req.body)
       const trabajador =  await PrismaConnector.trabajador.findUniqueOrThrow({
            where:{email:data.email}
        });

        if(bcryptjs.compareSync(data.antiguaPassword, trabajador.password)){
            const nuevaPassword = bcryptjs.hashSync(data.nuevaPassword)
            await PrismaConnector.trabajador.update({
                data: {
                    password:nuevaPassword,
                },
                where : {
                    email:data.email
                }
            })
            await cambioPassword({destinatario: trabajador.email,nombre:trabajador.nombre})
            return res.json({
                message:"Contraseña actualizada exitosamente",
                result: null
            })
        }else{
            throw new Error ('La contraseña es incorrecta')
        }
    } catch (error) {
        return res.json({
            message: "Error al actualizar la password",
            result: error.message
        })
    }
}

export const login = async (req, res) => {
    const { body } = req;
    try {
      const data = loginRequestDTO(body);
  
      const trabajador = await PrismaConnector.trabajador.findUniqueOrThrow({
        where: { email: data.email },
      });
  
      if (bcryptjs.compareSync(data.password, trabajador.password)) {
        console.log("si es la password");
        const token = jwt.sign(
          {
            id: trabajador.id,
            message: "Mensaje oculto",
          },
          process.env.JWT_SECRET,
          { expiresIn: "2h" }
          // expiresIn: un numero sera segundos, si es un numero con comillas sera ms, '1 day', '10h', '50d', '1y'
        );
  
        return res.json({
          message: "Bienvenido",
          result: token,
        });
      } else {
        console.log("contraseña incorrecta");
  
        throw new Error("Password invalida");
      }
    } catch (error) {
      return res.status(400).json({
        message: "Error al hacer el login",
        result: error.message,
      });
    }
  };

export const perfil = async (req,res) =>{
    console.log(req.user)

    const {password,...result} = req.user;
    return res.json({
        message: null,
        result 
    })
  }