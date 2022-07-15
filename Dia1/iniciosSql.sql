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

-- DML Data Manipualtion Languaje (Lenguaje de Manipulacion de Datos)
-- Con esto extraigo, inserto, actualizo y elimino la informacion de la bd
-- INSERT (Insertar nueva informacion)
-- Para las fechas en BD se usa el ISO 8601(YYY-MM-DD HH:MM:SS)

INSERT INTO productos (id, nombre, fecha_Vencimiento) VALUES(DEFAULT , 'Aguaymanto','2002-05-31');
INSERT INTO productos(id, nombre, fecha_Vencimiento) VALUES(DEFAULT, 'Cebolla','2022-05-30'),(DEFAULT,'Limon','2022-04-23');

-- Select
-- Al momento de insertar registros y si estamos manejando el autoincrementador y al momento de realizar el registro de un producto este fallase, el incrementador igual incrementa
SELECT nombre, fecha_Vencimiento FROM productos;
SELECT * FROM productos;
SELECT fecha_Vencimiento AS 'Fecha de Vencimiento' FROM productos;

-- Con la clausula de condicion WHERE indicaremos filtro para los resultados, esta es la mejor forma de hacer busquedas y es recomendable hacerlas a nivel de BD
SELECT * FROM productos WHERE nombre= 'Cebolla';

-- AND => Todas las condiciones tienen que ser verdaderas
SELECT * FROM productos WHERE nombre='Cebolla' AND id =1;
-- OR => Cualquiera de las condiciones tiene que ser verdadera
SELECT * FROM productos WHERE nombre='Cebolla' OR id=1;
SELECT * FROM productos WHERE nombre='Cebolla' OR id=1 OR id=7 AND nombre= 'Limon';
SELECT * FROM productos WHERE nombre LIKE 'Agua%';
SELECT * FROM productos WHERE nombre LIKE '___a%';

-- UPDATE 
UPDATE productos SET nombre = 'Cebolla China' WHERE nombre= 'Cebolla';

-- Desactivar el modo seguro que lo que hace es que ahora podemos hacer actualizaciones sin la necesidad de tener la condicion a una columna UNIQUE o que sea una KEY
-- No se recomienda desactivarlo porque podria llevar a hacer modificaciones masivas sin la posibilidad de deshacer esos cambios 
SET SQL_SAFE_UPDATES = false;


-- -------------------------------------------------------------------------------------------------------------------------------
-- DDL Data Definition Languaje (Lenguaje de Definicion de Datos)
-- Definir la estructura que vamos a manejar en la bd(crear, modificar y eliminar tablas o BD)

