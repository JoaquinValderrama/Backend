-- SQL => STRUCTURED QUERY LANGUAGE (Lenguaje de Consultas Estructurados)
-- REGISTRO => Conjunto de datos
-- Dato => Un valor que por si solo no da una buena referencia 
-- Las BD estan compuestas por una o varias tablas y cada tabla puede contener uno o varios registros

CREATE DATABASE prueba;

-- Sirve para indicar en que BD vamos a trabajar :D
USE prueba;

CREATE TABLE productos(
	-- Obligatoriamente para crear una tabla debemos crear al menos una columna 
    -- Solamente se puede usar una vez el auto incrementado por tabla 
    id INT auto_increment PRIMARY KEY,
    nombre VARCHAR(50),
    fecha_Vencimiento DATE
);