
CREATE TABLE level_of_management (
    id
    type
);
INSERT INTO level_of_management (id, name) VALUES (1, 'call');
INSERT INTO level_of_management (id, name) VALUES (2, 'reset sms');
INSERT INTO level_of_management (id, name) VALUES (3, 'reset gprs');
INSERT INTO level_of_management (id, name) VALUES (4, 'call costumer');


/* esta se puede dejar como las NOTES */
CREATE TABLE respond_management (
    id serial
    id.support_management
    id.level_of_management

);


CREATE TABLE support_management (
    id serial;
    start_datetime
	last_datetime datetime now not null;
    fk id.position_gps /* en este esta gps_id.positions_gps */
	fk id.types_of_management /* hasta que gestion se le hizo */
	funcionando = true or false;
);

CREATE TABLE ticket_queue (
	id serial;
	name ;
)
INSERT INTO ticket_queue () VALUES ('minitoreo');

CREATE TABLE sub_ticket_row (
	fk id.ticket_row
	name varchar(20);
);


/* Solo se crea ticket cunaod la gestion no funcionan. ejemplo: taller, revision, etc*/
/* también se crea un ticket para los eventos de pánico el cual debe terner la posicion_gps*/
/* crear tickets para: cartera, desinstalación, revisión, etc. todo lo inimaginable */
CREATE TABLE tickets (
    id SERIAL PRIMARY KEY,
    state BOOLEAN DEFAULT TRUE,

    fk id.support_management /* no puede ser fk por que se deben crear tickets para otro tipo de gestión eje: revisiones futuras, desinstalaciones, etc*/
    reminders datetime,
);

CREATE TABLE notes_tk (
	id.tickets /* se pueden terner varias notes para el mimsmo ticket */
);

CREATE TABLE calendar_tk (
	id.tickets	/* se pueden terner varios calendar_tk para el mimsmo ticket */
);

CREATE TABLE sopport_queues (
);


/*
- se debe crear un calendario o fecha que recuerde cuando un soporte.
- que se sepa si las unidades están sin GPS
- se debe tener toda la información de la SIM (numero.)
- se deben reportar los sitios de parqueo de los vehículo.
- sistema pare verificar zonas de cobertura.
- SMS resolucion de ticket
- los tickets si debe ser cerrados maanualmente.
*/


