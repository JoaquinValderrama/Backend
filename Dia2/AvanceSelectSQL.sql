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