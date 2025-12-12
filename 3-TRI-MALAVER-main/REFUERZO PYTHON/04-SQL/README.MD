CREATE DATABASE base_data_michaelM;

//2

\c base_data_Mendieta;
SELECT current_database();
\conninfo

//3

CREATE TABLE clientes (
id SERIAL PRIMARY KEY,
nombre VARCHAR(100) NOT NULL,
email VARCHAR(150) UNIQUE,
telefono VARCHAR(15),
fecha_registro DATE DEFAULT CURRENT_DATE,
activo BOOLEANÂ DEFAULTÂ TRUE
);

//4

INSERT INTO clientes (nombre, email, telefono, fecha_registro, activo)
VALUES ('Juan PÃ©rez', 'juan.perez@email.com', '555-0123', '2024-01-15', TRUE);
INSERT INTO clientes (nombre, email)
VALUES ('MarÃ­a GarcÃ­a', 'maria.garcia@email.com');
INSERT INTO clientes (nombre, email, telefono) VALUES
('Carlos LÃ³pez', 'carlos@email.com', '555-0124'),
('Ana MartÃ­nez', 'ana@email.com', '555-0125'),
('Luis RodrÃ­guez', 'luis@email.com',Â '555-0126');

//5

SELECT * FROM clientes;
SELECT nombre, email FROM clientes;
SELECT nombre, telefono FROM clientes WHERE activo = TRUE;
SELECT COUNT(*) FROM clientes;
SELECT nombre, email FROM clientes ORDER BY nombre;
SELECT * FROM clientesÂ LIMITÂ 3;

//6

SELECT * FROM clientes WHERE nombre = 'Juan PÃ©rez';
SELECT * FROM clientes WHERE nombre LIKE '%GarcÃ­a%';
SELECT * FROM clientes WHERE fecha_registro = '2024-01-15';
SELECT * FROM clientes WHERE fecha_registro > '2024-01-01';
SELECT * FROM clientes WHERE activo = TRUE AND fecha_registro > '2024-01-01';
SELECT * FROM clientes WHERE nombre LIKE '%Juan%' OR nombre LIKE '%MarÃ­a%';
SELECT * FROM clientes WHERE nombre IN ('Juan PÃ©rez', 'MarÃ­a GarcÃ­a', 'Carlos LÃ³pez');
SELECT * FROM clientes WHERE nombre NOTÂ LIKEÂ '%LÃ³pez%';

