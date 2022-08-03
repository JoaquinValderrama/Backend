import _  from 'lodash'

export const departamentoRequestDTO = (body) =>{
    const errores =[];

    if(_.isNil(body.nombre)){
        errores.push("falta el nombre")
    }

    if(errores.length!== 0){
        throw new Error(errores)
    }else{
        return body;
    }
}