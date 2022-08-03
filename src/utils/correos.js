import nodemailer from "nodemailer";

const cliente = nodemailer.createTransport({
    host:'smtp.gmail.com',
    port:587,
    auth:{
        user: process.env.EMAIL,
        pass: process.env.EMAIL_PASSWORD
    }
})

export const validarCorreo = async ({destinatario,nombre,token}) =>{
    
    try {
        const resultado = await cliente.sendMail({
            from:process.env.EMAIL,
            to: destinatario,
            subject: 'Valida tu correo para la APP de backend',
            text:  `hola ${nombre} por favor valida tu correo haciendo click en el siguiente enlace: http://mifront.com?token=${token}`
        })

        console.log(resultado)
    } catch (error) {
        console.log(error.message)
    }
    
   
}

export const cambioPassword = async({destinatario,nombre}) =>{
    try {
        await cliente.sendMail({
            from:process.env.EMAIL,
            to: destinatario,
            subject:'Cambio de Contraseña',
            html: `
                <h1>Cambio de PASSWORD</h1>
                <p>Hola ${nombre}, le notificamos que tu password ha sido cambiada, si no fuiste tu reinicia tu contraseña, caso contrario has caso omiso a este mensaje</p>
                </br>
                <h3>Atentamente,</h3>
                </br>
                <h3>El equipo de backend</h3>
                 `
        })
    } catch (error) {
        
    }
}