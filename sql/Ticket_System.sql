
---------------------- Roles, Groups, Agents:


-- Create table Role
CREATE TABLE roles (
	id SERIAL,
	type VARCHAR(31) NOT NULL,
	description	VARCHAR(150) NOT NULL
);
ALTER TABLE roles ADD CONSTRAINT role_pk PRIMARY KEY (id);

INSERT INTO roles (type, description) VALUES ('ro', 'Acceso de sólo lectura a los tickets en este grupo/cola.');
INSERT INTO roles (type, description) VALUES ('mover_a', 'Permiso para mover tickets a este grupo/cola');
INSERT INTO roles (type, description) VALUES ('crear', 'Permiso para crear tickets en este grupo/cola');
INSERT INTO roles (type, description) VALUES ('prioridad', 'Permiso para cambiar la prioridad del ticket en este grupo/cola');
INSERT INTO roles (type, description) VALUES ('rw', 'Acceso completo de lectura y escritura a los tickets en este grupo/cola.');


-- Create table Groups
CREATE TABLE groups (
	id SERIAL,
	name VARCHAR(51) NOT NULL,
	description	VARCHAR(150) NOT NULL
);
ALTER TABLE groups ADD CONSTRAINT group_pk PRIMARY KEY (id);

INSERT INTO groups (name, description) VALUES ('admin', 'Grupo de todos los administradores');
INSERT INTO groups (name, description) VALUES ('stats', 'Grupo para acceso a las estadísticas');
INSERT INTO groups (name, description) VALUES ('users', 'Grupo de acceso predeterminado');


-- Create table Groups_Roles
CREATE TABLE groups_roles (
	id_group INTEGER,
	id_role INTEGER,
	UNIQUE (id_group, id_role)
);
ALTER TABLE groups_roles ADD CONSTRAINT id_role_fk FOREIGN KEY (id_role) 
REFERENCES roles(id) MATCH FULL ON DELETE CASCADE ON UPDATE CASCADE;
ALTER TABLE groups_roles ADD CONSTRAINT id_group_fk FOREIGN KEY (id_group) 
REFERENCES groups(id) MATCH FULL ON DELETE CASCADE ON UPDATE CASCADE;


-- Create table Agents
CREATE TABLE agents (
	id SERIAL,
	first_name VARCHAR(150) NOT NULL,
	last_name VARCHAR(150) NOT NULL,
	username VARCHAR(31) NOT NULL,
	password VARCHAR(31) NOT NULL,
	email VARCHAR(100) NOT NULL,
);
ALTER TABLE agents ADD CONSTRAINT agent_pk PRIMARY KEY (id);


-- Create table Agents_Groups
CREATE TABLE agents_groups (
	id_agent INTEGER,
	id_group INTEGER,
	UNIQUE (id_group, id_agent)
);
ALTER TABLE agents_groups ADD CONSTRAINT id_group_fk FOREIGN KEY (id_group) 
REFERENCES groups(id) MATCH FULL ON DELETE CASCADE ON UPDATE CASCADE;
ALTER TABLE agents_groups ADD CONSTRAINT id_agent_fk FOREIGN KEY (id_agent) 
REFERENCES agents(id) MATCH FULL ON DELETE CASCADE ON UPDATE CASCADE;






---------------------- Categories, Queues, Responses:


-- Una respuesta es un texto predeterminado que ayuda a los agentes para que escriban las respuestas más rápidas a los clientes. 
-- Atención: No te olvides de añadir nuevas respuestas a las colas.
CREATE TABLE responses (
	id SERIAL,
	name VARCHAR(100) NOT NULL,
	response TEXT NOT NULL,
	comment VARCHAR(150),
	created TIMESTAMP with time zone,
	amended TIMESTAMP with time zone,
	UNIQUE (name)
);
ALTER TABLE responses ADD CONSTRAINT response_pk PRIMARY KEY (id);

INSERT INTO responses (name, response, comment, created, amended) VALUES (
'respuesta estandar del sistema',
'Buen día apreciado $.cliente.name

',
'Respuesta Estandar',
now(), now());


-- Saludo:
CREATE TABLE salutations (
	id SERIAL,
	name VARCHAR(100) NOT NULL,
	salutation TEXT NOT NULL,
	comment VARCHAR(150),
	created TIMESTAMP with time zone,
	amended TIMESTAMP with time zone,
	UNIQUE (name)
);
ALTER TABLE salutations ADD CONSTRAINT salutation_pk PRIMARY KEY (id);

INSERT INTO salutations (name, salutation, comment, created, amended) VALUES (
'saludo estandar del sistema',
'Buen día apreciado $cliente.name,

Gracias por su solicitud.',
'Saludo Estandar',
now(), now());


-- firmas:
CREATE TABLE signatures (
	id SERIAL,
	name VARCHAR(100) NOT NULL,
	signature TEXT NOT NULL,
	comment VARCHAR(150),
	created TIMESTAMP with time zone,
	amended TIMESTAMP with time zone,
	UNIQUE (name)

);
ALTER TABLE signatures ADD CONSTRAINT signature_pk PRIMARY KEY (id);

INSERT INTO signatures (name, signature, comment, created, amended) VALUES (
'firma estandar del sistema',
'Se te ha generado un ticket: 
$agent.name
--
Area de $categories
www.website.com',
'Firma Estandar',
now(), now());



-- :


