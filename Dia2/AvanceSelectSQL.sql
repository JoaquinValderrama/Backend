 CREATE DATABASE vacunaciones;
 
 USE vacunaciones;
 
 CREATE TABLE vacunas(
	id int AUTO_INCREMENT PRIMARY KEY,
    nombre VARCHAR (100) UNIQUE NOT NULL,
    procedencia VARCHAR(20) NOT NULL,
    lote CHAR(6)
 );
 
 
 INSERT INTO vacunas (id, nombre, procedencia,lote) VALUES
					 (DEFAULT,'PFIZER','EEUU','123abc'),
                     (DEFAULT,'SPUTNIK','RUSA','3d3afg'),
                     (DEFAULT,'ASTRAZENECA','CHINA','5d8jh5'),
                     (DEFAULT,'JHONSON & JHONSON','EEUU','n8gg84'),
					 (DEFAULT,'CINOPHARM','CHINA','4ifrt5');
					
                    
SELECT * FROM vacunas WHERE id  = 3;
SELECT * FROM vacunas WHERE procedencia = 'CHINA';
SELECT * FROM vacunas WHERE nombre  LIKE '% %';
SELECT * FROM vacunas WHERE nombre LIKE '_I_O%';


CREATE TABLE vacunatorios(
-- Columnas propias de la tabla 
	id INT PRIMARY KEY,
    direccion VARCHAR(100),
    numero INT NOT NULL,
    atencion_preferencial BOOLEAN NOT NULL DEFAULT TRUE,
    latitud FLOAT (4,2),  -- la declaracion del punto flotante en los tipos de datos FLOAT no servira :o 
    longitud FLOAT (4,2),
    
-- las columnas que van a cumplir como relaciones, es una buena practica usar el sgte formato(nombre_de_la_tabla_columna)
	vacuna_id INT,
    
-- RELACIONES
 FOREIGN KEY(vacuna_id) REFERENCES vacunas(id)
);

ALTER TABLE vacunatorios DROP COLUMN id;
ALTER TABLE vacunatorios ADD COLUMN id INT AUTO_INCREMENT PRIMARY KEY FIRST;
INSERT INTO vacunatorios (id,direccion, numero,atencion_preferencial,latitud,longitud,vacuna_id)VALUES
						 (DEFAULT,'Calle los Palitos',123,TRUE,10.53,14.70,1),
                         (DEFAULT,'Av. Girasol',1213,FALSE,12.53,19.70,1),
                         (DEFAULT,'Hosp. General',111,DEFAULT,12.49,80.15,2),
                         (DEFAULT,'Posta Cerro 8 Colores',1394,DEFAULT,10.53,14.60,3),
                         (DEFAULT,'Estadio Los Aguateros',123,TRUE,10.53,14.70,4),
                         (DEFAULT,'Plaza de Armas',456,TRUE,13.23,44.65,5);
                         

-- Devolver las direcciones y sus numeros que tengan atencion preferencial
SELECT direccion, numero FROM vacunatorios WHERE atencion_preferencial  = TRUE;

-- Devolver las direcciones que se encuentren entre lat >20.0 y long < 20.00
SELECT direccion FROM vacunatorios WHERE latitud >20.00 AND longitud <20.00;

-- Devolver las direcciones que sean pfizer (1) y que tengan atencion preferencial
SELECT direccion FROM vacunatorios WHERE vacuna_id = 1 AND atencion_preferencial = TRUE;

-- Devolver las direcciones cuya vacuna no sea pfizer (1) (diferente que != )  o que tenga atencion preferencial 
SELECT direccion FROM vacunatorios WHERE vacuna_id !=1 OR atencion_preferencial = TRUE;
