import prisma, { PrismaClient } from "@prisma/client"

const {prismaClient} = prisma;

// creamos la instancia para conectarnos a la BD desde express
export const PrismaConnector = new PrismaClient()

