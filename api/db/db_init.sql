CREATE DATABASE EGCON;

USE EGCON;

CREATE TABLE device (
    id INT NOT NULL AUTO_INCREMENT,
    name VARCHAR(100) NOT NULL,
    code VARCHAR(20) NOT NULL UNIQUE,
    type ENUM('SENSOR', 'ACTUATOR') NOT NULL,
    reference VARCHAR(100) NOT NULL,
    location ENUM('NORTH', 'EAST', 'SOUTH', 'WEST') NOT NULL,
    params VARCHAR(500),
    PRIMARY KEY (id)
);

INSERT INTO device (name, code, type, reference, location) VALUES('Motor abrir almacen de tomates','AATN01','ACTUATOR','Motor GTX1050','NORTH');
INSERT INTO device (name, code, type, reference, location, params) VALUES('Sensor de temperatura de cultivo de tomates','SCT022','SENSOR','AK800','SOUTH', '{"rangoDia":"20-25", "rangoNoche": "15-20"}');