import prisma from "@prisma/client"
import _ from "lodash"
import validator from "validator"

export const trabajadoresRequestDTO = (data) =>{
    const errores = []

    if (_.isNil(data.nombre)){
        errores.push("falta el nombre")
    }

    if (_.isNil(data.apellido)){
        errores.push("falta el apellido")
    }
    if (_.isNil(data.email)){
        errores.push("falta el email")
    }

    if(!_.isNil(data.email) && !validator.isEmail(data.email)){
        errores.push("Email invalido")
    }

    if (_.isNil(data.password)){
        erroes.push("Falta la password")
    }

    if (_.isNil(data.rol)){
        errores.push("Falta el rol")
    }

    // if(!_.isNil(data.rol) || data.rol !== prisma.ROL_TRABAJADOR.GERENTE ||data.rol !== prisma.ROL_TRABAJADOR.OBRERO  || data.rol !== prisma.ROL_TRABAJADOR.PRACTICANTE || data.rol !== prisma.ROL_TRABAJADOR.SUPERVISOR){
    //     errores.push("Rol incorrecto, sus valores son 'Gerente','Obrero','PRACTICANTE','SUPERVISOR'")
    // }
    if(!_.isNil(data.rol)){
        const roles = Object.values(prisma.ROL_TRABAJADOR)

        const filtro = roles.filter((rol) => rol === data.rol)

        if(filtro.length === 0 ){
           let mensaje = "Rol incorrecto, sus valores son: ";
           roles.forEach((rol) => mensaje += `'${rol}' `)

           errores.push(mensaje)
        }
    }

    if (errores.length !==0){
        throw new Error(errores)
    }else {
        return data;
    }
}

export const cambiarPasswordRequestDTO =(data) =>{
    const errores = []
    
    if(_.isNil(data.email)){
        errores.push('falta el email')
    }
    if(_.isNil(data.antiguaPassword)){
        errores.push("falta la antigua Password")
    }
    if(_.isNil(data.nuevaPassword)){
        errores.push("falta la nueva Password")
    }

    if (_.isNil(data.email) && !validator.isEmail(data.email)){
        errores.push("Email invalido")
    }

    if (errores.length !=0){
        throw new Error(errores)
    }else{
        return data;
    }
}

export const loginRequestDTO = (data) =>{

    const errores = []
    
    if(_.isNil(data.email)){
        errores.push('falta el email')
    }

    if(_.isNil(data.password)){
        errores.push('falta el password')
    }

    if(!_.isNil(data.email) && !validator.isEmail(data.email)){
        errores.push('Email Invalido')
    }

    if(errores.length !==0){
        throw new Error(errores)
    }else{
        return data;
    }
}