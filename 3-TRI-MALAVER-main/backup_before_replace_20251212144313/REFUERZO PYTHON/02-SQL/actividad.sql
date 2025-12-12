Actividad SQL Integrada

1. Crea la base de datos 'empresa_db' y úsala.

2. Crea las tablas:
   - EMPLEADOS(id INT PK, nombre VARCHAR(80), salario DECIMAL(10,2), id_dpto INT)
   - DEPARTAMENTOS(id_dpto INT PK, nombre VARCHAR(80))

3. Inserta datos:
   Departamentos: (1,'Ventas'),(2,'TI'),(3,'Recursos Humanos')
   Empleados:
     (1,'Ana Pérez',2500,1)
     (2,'Carlos Ruiz',3200,2)
     (3,'Laura Gómez',1800,1)
     (4,'Jorge Díaz',2900,3)

4. Consulta empleados con salario > 2000 ordenados desc.

5. Muestra nombre del empleado, nombre del departamento y salario.

6. Actualiza salario de empleados de TI aumentando 10%.

7. Elimina empleados con salario < 2000.

Fin.



-- 1. Crear base de datos
CREATE DATABASE empresa_db;

-- (Después de crearla, en DBeaver haz clic derecho -> Set Active)

-------------------------------------------------------
-- 2. Crear tablas
-------------------------------------------------------

CREATE TABLE DEPARTAMENTOS (
    id_dpto INT PRIMARY KEY,
    nombre VARCHAR(80)
);

CREATE TABLE EMPLEADOS (
    id INT PRIMARY KEY,
    nombre VARCHAR(80),
    salario NUMERIC(10,2),
    id_dpto INT,
    FOREIGN KEY (id_dpto) REFERENCES DEPARTAMENTOS(id_dpto)
);

-------------------------------------------------------
-- 3. Insertar datos
-------------------------------------------------------

INSERT INTO DEPARTAMENTOS (id_dpto, nombre)
VALUES
(1, 'Ventas'),
(2, 'TI'),
(3, 'Recursos Humanos');

INSERT INTO EMPLEADOS (id, nombre, salario, id_dpto)
VALUES
(1, 'Ana Pérez', 2500, 1),
(2, 'Carlos Ruiz', 3200, 2),
(3, 'Laura Gómez', 1800, 1),
(4, 'Jorge Díaz', 2900, 3);

-------------------------------------------------------
-- 4. Consulta: empleados con salario > 2000 ordenados desc
-------------------------------------------------------

SELECT *
FROM EMPLEADOS
WHERE salario > 2000
ORDER BY salario DESC;

-------------------------------------------------------
-- 5. Consulta: nombre del empleado, nombre del departamento y salario
-------------------------------------------------------

SELECT e.nombre AS empleado,
       d.nombre AS departamento,
       e.salario
FROM EMPLEADOS e
JOIN DEPARTAMENTOS d ON e.id_dpto = d.id_dpto;

-------------------------------------------------------
-- 6. Aumento del 10% a empleados del departamento TI
-------------------------------------------------------

UPDATE EMPLEADOS
SET salario = salario * 1.10
WHERE id_dpto = 2;

-------------------------------------------------------
-- 7. Eliminar empleados con salario < 2000
-------------------------------------------------------

DELETE FROM EMPLEADOS
WHERE salario < 2000;
