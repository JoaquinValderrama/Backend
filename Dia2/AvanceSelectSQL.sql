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
INSERT INTO vacunatorios (id, direccion, numero , atencion_preferencial,latitud,longitud,vacuna_id)VALUES (DEFAULT , 'Calle s/n' , 123 ,FALSE, 10.00,10.00, NULL);


-- JOINS 

SELECT * FROM vacunas INNER JOIN vacunatorios ON vacunas.id = vacunatorios.vacuna_id;

-- lEFT JOIN 
-- Traera todo lo de la izquierda y si es que hay alguna coincidencia con lo de la derecha 
SELECT * FROM vacunas LEFT JOIN vacunatorios ON vacunas.id = vacunatorios.vacuna_id;

-- RIGHT JOIN 
-- Traera todo lo de la derecha y si es que hay alguna coincidencia con lo de la izquierda
SELECT * FROM vacunas RIGHT JOIN vacunatorios ON vacunas.id = vacunatorios.vacuna_id;


CREATE TABLE campanias (
id INT PRIMARY KEY AUTO_INCREMENT,
nombre VARCHAR(100),
fecha DATE,
descripcion TEXT -- Es como el varchar (dependiendo de cuantos caracteres guardemos, separa el espacio de memoria pero no tiene limite)
);

CREATE TABLE vacunatorios_campanias(
id INT PRIMARY KEY AUTO_INCREMENT,
vacunatorio_id INT NOT NULL,
campania_id INT NOT NULL,

-- CREACION DE RELACIONES
FOREIGN KEY (vacunatorio_id) REFERENCES vacunatorios(id),
FOREIGN KEY (campania_id) REFERENCES campanias(id)
);

INSERT INTO campanias (id, nombre, fecha, descripcion) VALUES
					  (DEFAULT, 'Pongo el Hombro', '2022-01-01' , 'Campaña de vacunacion para personas adultas'),
                      (DEFAULT, 'Vacuna Warma', '2022-03-10' , 'Campaña de vacunacion niños menores de 18 años'),
                      (DEFAULT, 'Mayorcitos', '2022-11-04' , 'Campaña de vacunacion para personas mayores a 65 años');
                      

INSERT INTO vacunatorios_campanias(id, vacunatorio_id,campania_id) VALUES
								  (DEFAULT,1,1),
                                  (DEFAULT,2,1),
                                  (DEFAULT,3,1),
                                  (DEFAULT,2,2),
                                  (DEFAULT,1,2),
                                  (DEFAULT,3,3),
                                  (DEFAULT,4,3),
                                  (DEFAULT,5,3);
                                  
		
-- Desde la campaña hacia el vacunatorio campaña
SELECT * FROM campanias as C INNER JOIN vacunatorios_campanias as VC ON C.id = VC.campania_id;
