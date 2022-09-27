# -*- coding: utf-8 -*-
import config
import sys

#def listingUser(**k):
    #return config.DB.select('users', **k)
    #print **k
    #return config.DB.select('usuarios', **k)

def listingUser(**k):
    """
        Determina si el usuario y contraseña coinciden.
    """
    #return config.DB.query("SELECT cliente_id AS clienteId, privilege_id FROM usuarios WHERE usuario=$name and pass=$passwd", **k)
    return config.DB.query("SELECT cliente_id AS clienteId, privilege_id, id FROM usuarios WHERE usuario=$i.username and passwd=$i.password", **k)


def lastentry(idUser):
    """
        Crea una entrada en la tabla "usuarios" indicando la fecha y hora
        del ultimo ingreso del usuario.
    """
    from web.db import sqlquote
    try:
        config.DB.query("UPDATE usuarios SET last_entry=now() WHERE id=" + sqlquote(idUser));
    except:
        pass


def listingPrivilege(**k):
    """
        Determina a que subaplicación se debe reenviar el usuario.

        Usage:
        >>> from db import listingPrivilege
        >>> privilegeId=1
        >>> listingPrivilege(vars=locals())
            0.0 (1): SELECT descrip FROM privileges WHERE id=1
            u'/user'
        >>>
    """
    result = config.DB.query("SELECT descrip FROM privileges WHERE id=$privilegeId", **k)
    return "".join(["/%s" % v for v in result[0].values()])


def getNameClient(**k):
    """
        Obtine el nombre del cliente

        usage:
            >>> from db import getNameClient
            >>> clienteId = 1
            >>>
            >>> getNameClient(vars=locals())
             0.0 (1): SELECT nombre1, nombre2, apellido1, apellido2 FROM clientes WHERE id=1
             <Storage {'nombre2': u'alonso', 'apellido2': u'hoyos', 'apellido1': u'toro', 'nombre1': u'jorge'}>
            >>> r = getNameClient(vars=locals())
             0.0 (2): SELECT nombre1, nombre2, apellido1, apellido2 FROM clientes WHERE id=1
            >>> r.nombre1
             u'jorge'
            >>>
    """
    result = config.DB.query("SELECT nombre1, nombre2, apellido1, apellido2 FROM clientes WHERE id=$clienteId", **k)
    #return "".join(["%s " % v for v in result[0].values()])
    #return result[0].values()
    return result[0]

#def getCompany(**k):
#    """
#        Obtiene la empresa según el cliente de la sesión.
#
#        usage:
#        >>> from db import getCompany
#        >>> clienteId = 1
#        >>>
#        >>> getCompany(vars=locals())
#        0.0 (1):
#        SELECT c.id, c.name, c.document, c.ciudad, c.direccion, c.email, c.sitio_web
#        FROM clientes_empresa ce, companies c
#        WHERE ce.empresa_id = c.id AND ce.cliente_id=1
#        <Storage {'ciudad': u'17001', 'name': u'dev microsystem', 'id': 1, 'sitio_web': u'www.devmicrosystem.com',
#         'document': u'900375522-7', 'email': u'info@devmicrosystem.com', 'direccion': u'Cra 11 15-15'}>
#        >>> c = getCompany(vars=locals())
#        >>> c.name
#        u'dev microsystem'
#        >>>
#    """
#    result = config.DB.query("""
#            SELECT c.id, c.name, c.document, c.ciudad, c.direccion, c.email, c.sitio_web
#            FROM clientes_empresa ce, companies c
#            WHERE ce.empresa_id = c.id AND ce.cliente_id=$clienteId""", **k)
#    return result[0]

def getCompany(**k):
    """
        Obtiene la empresa según el cliente de la sesión.

        usage:
        >>> from db import getCompany
        >>> clienteId = 1
        >>>
        >>> getCompany(vars=locals())
        0.0 (1):
        <Storage {'cargo': u'gerente', 'regimen': u'Regimen comun', 'name': u'dev microsystem',
        't_docu': u'NIT       ', 'direccion': u'Cra 11 15-15', 'ciudad': u'Manizales', 'id': 1,
        'sitio_web': u'www.devmicrosystem.com', 'document': u'900375522-7',
        'email': u'info@devmicrosystem.com', 't_companie': u'SAS       '}>
        >>> c = getCompany(vars=locals())
        >>> c.name
        u'dev microsystem'
        >>>
    """
    result = config.DB.query("""
            SELECT c.id, c.name, c.document, m.descrip AS ciudad, c.direccion, c.email,
            c.sitio_web, ce.cargo_empresa AS cargo, sc.descrip AS t_companie,
            r.descrip AS regimen, td.descrip AS t_docu
            FROM companies c
            LEFT OUTER JOIN municipio AS m ON (c.ciudad=m.codigo)
            LEFT OUTER JOIN clientes_empresa AS ce ON (ce.empresa_id=c.id)
            LEFT OUTER JOIN sociedades_comerciales AS sc ON (sc.id=c.type_company_id)
            LEFT OUTER JOIN regimen AS r ON (r.id=c.regimen_id)
            LEFT OUTER JOIN type_document AS td ON (td.id=c.type_docu_id)
            WHERE ce.cliente_id=$clienteId""", **k)
    return result[0]

#def listingDropdown(table, vars="id,name", order="id ASC"):
def listingDropdown(table, vars="id,name", order=None):
    """
        Obtiene una lista para los form.Dropdown().

        Usage:
        >>> from db import listingDropdown
        >>> r = listingDropdown('type_document')
            0.0 (4): SELECT id,name FROM type_document ORDER BY id ASC
        >>> r
        [(1, u'C\xe9dula de Ciudadan\xeda'), (2, u'N\xfamero de Identificaci\xf3n Tributaria'),
        (3, u'Registro \xdanico Tributario'), (4, u'Tarjeta de Identidad'), (5, u'C\xe9dula de Extranjer\xeda')]
        >>>
        >>> r = listingDropdown('type_gps', "codigo,descrip", "codigo ASC")
            0.0 (4): SELECT codigo,descrip FROM type_gps ORDER BY codigo ASC
        >>> r
        [(1, u'Antares'), (2, u'Skypatrol'), (3, u'HunterPro')]
        >>>
    """
    #result = config.DB.select
    #result = config.DB.select('type_document', what="id,name")
    #result = config.DB.select('type_document', what="id,name", order="id DESC") # order="id ASC"
    # result = config.DB.select('type_document', what="id,name", order="id ASC")

    #result = config.DB.select(table, what=vars, order)
    result = config.DB.select(table, what=vars, order=order)
    return [tuple(i.values()) for i in result.list()]

def listingGPS():
    """
        Realiza un select de todos los GPS en las tablas public.gps y public.type_gps.

        Usage:
        >>> from db import listingGPS
        >>> a = listingGPS()
        >>> for i in a.list():
        ...     print i.name
        ...
        GPS0001
        GPS0004
        ANT051
        ANT056
        ANT099
        >>>
    """
    return config.DB.query("""SELECT g.id, g.name, g.fecha_creacion, t.descrip,
            g.active FROM gps g INNER JOIN  type_gps t ON g.type = t.codigo;""")

def listUsuarios():
    """
        Realiza un select de todos los Usuarios.

        Usage:
        >>> from db import listUsuarios
        >>> a = listUsuarios()
        >>>
        >>> for i in a.list():
            ...     print i
            ...
            <Storage {'usuario': u'jorge', 'passwd': u'123456', \
            'fecha_caduca': datetime.datetime(2013, 8, 16, 19, 6, 12, 471588, tzinfo=psycopg2.tz.FixedOffsetTimezone(offset=1140, name=None)),\
            'fecha_crea': datetime.datetime(2012, 8, 9, 19, 6, 12, 471588, tzinfo=psycopg2.tz.FixedOffsetTimezone(offset=1140, name=None)), \
            'cliente': u'11814584', 'activo': True, 'descrip': u'user', 'id': 1}>
    """
    return config.DB.query("""
            SELECT u.id, u.usuario, u.passwd, p.descrip, c.documento AS cliente,
            u.fecha_crea, u.fecha_caduca, u.activo
            FROM usuarios u
            INNER JOIN  privileges p ON u.privilege_id=p.id
            INNER JOIN clientes c ON u.cliente_id=c.id;
            """)

def listingAllClient():
    """
        Query que abstrae todos los Clientes.
        Usage:
        >>> from db import listingAllClient
        >>> a = listingAllClient()
        >>> for i in a:
        ...     print i
        ...
        <Storage {'nombre1': u'jorge', 'genero': u'Masculino', 'tipo': u'C\xe9dula de Ciudadan\xeda',
        'nombre2': u'alonso', 'fecha_naci': datetime.date(1982, 11, 2),
        'direccion': u'Cra 11 # 15-15 APT 601 BL 2B', 'apellido2': u'hoyos', 'apellido1': u'toro',
        'id': 1, 'email': u'jolthgs@gmail.com', 'municipio': u'Manizales', 'documento': u'11814584'}>
    """
    return config.DB.query("""
            SELECT c.id, c.documento, td.descrip AS tipo,
            c.nombre1, c.nombre2, c.apellido1, c.apellido2,
            c.fecha_naci, s.descrip AS genero,
            c.direccion, m.descrip AS municipio, c.email
            FROM clientes AS c
            LEFT OUTER JOIN type_document AS td ON (c.tipo_docu=td.id)
            LEFT OUTER JOIN sexo AS s ON (c.sexo_id=s.id)
            LEFT OUTER JOIN municipio AS m ON (c.ciudad=m.codigo);
            """)

def listingPhones(id):
    """
        usage:
        >>> from db import listingPhones
        >>> a = listingPhones(15)
        0.01 (1): SELECT p.phone, tp.name
                    FROM phones_all pa, phones p, type_phone tp
                    WHERE pa.phone_id=p.id AND tp.id=p.type AND pa.client_id=15
        >>> for i in a:
        ...     print i
        ...
        <Storage {'phone': u'7844983', 'name': u'fijo'}>
        <Storage {'phone': u'3126783452', 'name': u'celular'}>
        >>>
    """
    from web.db import sqlquote
    result = config.DB.query("""SELECT p.phone, tp.name
            FROM phones_all pa, phones p, type_phone tp
            WHERE pa.phone_id=p.id AND tp.id=p.type AND pa.client_id=""" + sqlquote(id))
    return [tuple(i.values()) for i in result.list()]

def listingClients(id):
    """
        Lista los clientes propietarios de un vehiculo.
        usage:
        >>> from db import listingClients
        >>> a = listingClients(5) # id del vehiculo
        >>>
        >>> for i in a:
        ...     print i
        ...
        (u'jorge,alonso,toro,hoyos', u'11814584')
        >>>
    """
    from web.db import sqlquote

    result = config.DB.query("""
            SELECT (c.nombre1 || ',' || COALESCE(c.nombre2, '') || ',' || c.apellido1 || ',' || COALESCE(c.apellido2,'')) AS nombre,
            c.documento
            FROM clientes_vehiculos cv, clientes c
            WHERE cv.cliente_id=c.id AND cv.vehiculo_id=""" + sqlquote(id))
    return [tuple(i.values()) for i in result.list()]

def listingAllVehicle():
    """
        Query que abstrae todos los vehículos.

        Usage:
        >>> from db import listingAllVehicle
        >>> a = listingAllVehicle()
        >>> for i in a:
        ...     for k,v in i.items():
        ...             print "%s=%s" % (k,v),
        ...
        servicio=None carroceria=Aspersora cilindraje=1.1 color=None
        ejes=1 combustible=Etanol clase=Motocarro marca=Hino placa=ttq000
        modelo=1964 linea=None name=ANT003 servicio=None carroceria=None
        cilindraje=None color=None ejes=None combustible=None clase=None
        marca=Renault placa=rjm270 modelo=2012 linea=None name=ANT049
        servicio=None carroceria=None cilindraje=None color=None ejes=None
        combustible=None clase=None marca=Jac placa=sta345 modelo=2008
        linea=None name=ANT098
        >>>
    """
    return config.DB.query("""
            SELECT v.id, v.placa, g.name, m.descrip AS marca, v.modelo,
            v.cilindraje, v.ejes, l.descrip AS linea,
            c.descrip AS clase, ca.descrip AS carroceria, co.descrip AS color,
            cb.descrip AS combustible, sv.descrip AS servicio
            FROM vehiculos AS v
            LEFT OUTER JOIN gps AS g ON (v.gps_id=g.id)
            LEFT OUTER JOIN marcas_vehiculo AS m ON (v.marca_id=m.id)
            LEFT OUTER JOIN liena_vehiculo AS l ON (v.linea_id=l.id)
            LEFT OUTER JOIN clase_vehiculo AS c ON (v.clase_id=c.id)
            LEFT OUTER JOIN carrocerias AS ca ON (v.carroceria_id=ca.id)
            LEFT OUTER JOIN colores AS co ON (v.color_id=co.id)
            LEFT OUTER JOIN combustibles AS cb ON (v.combustible_id=cb.id)
            LEFT OUTER JOIN servicio_vehiculo AS sv ON (v.servicio_id=sv.id);
            """)

def unmanagedEventListAdmin():
    """
        Query que obtiene todos los eventos no gestionados por el administrador.
        usage:
        >>> from db import unmanagedEventListAdmin
        >>> a = unmanagedEventListAdmin()
        >>> for i in a:
        ...     for k,v in i.items():
        ...             print "%s=%s" % (k,v),
        ...
        vehicle_id=4 name=Panico id=46 user_state=False fecha=2012-08-28 11:56:54.638781-05:00 placa=ttq000
        position_id=149 admin_state=False gps_name=ANT003 ubicacion=Carrera 6 # 16-2 a 16-100, Pereira, Risaralda, Colombia
        gps_id=10 coord_state=False vehicle_id=4 name=Ignicion OFF id=45 user_state=False fecha=2012-08-28 11:56:51.360497-05:00
        placa=ttq000 position_id=148 admin_state=False gps_name=ANT003
        ubicacion=Carrera 6 # 16-2 a 16-100, Pereira, Risaralda, Colombia gps_id=10 coord_state=False
    """
    return config.DB.query("""
            SELECT e.id, te.name, e.fecha, e.type AS tipo_event,
            e.gps_id, g.name AS gps_name,
            v.placa, v.id AS vehicle_id,
            e.admin_state, e.user_state, e.coord_state,
            e.positions_gps_id AS position_id, p.ubicacion, p.position
            from eventos e
            LEFT OUTER JOIN type_event AS te ON e.type=te.codigo
            LEFT OUTER JOIN vehiculos AS v ON e.gps_id=v.gps_id
            LEFT OUTER JOIN gps AS g ON e.gps_id=g.id
            LEFT OUTER JOIN positions_gps AS p ON p.id=e.positions_gps_id
            WHERE e.admin_state='f' ORDER BY e.id DESC;
            """)

def generalView():
    """
        Usage:
        >>> from db import generalView
        >>> a = generalView()
        0.0 (2): SELECT l.position, v.placa, g.name, l.fecha,
                 l.velocidad, l.altura, l.satelites, l.ubicacion, vs.motor
                 FROM vehiculos v, last_positions_gps l, gps g, vehicle_state vs
                 WHERE v.gps_id=g.id AND g.id=l.gps_id AND vs.vehicle_id=v.id;
        >>> a.list()
        [<Storage {'name': u'SKP042', 'velocidad': 0.0,
         'fecha': datetime.datetime(2013, 3, 12, 23, 57, 34, tzinfo=psycopg2.tz.FixedOffsetTimezone(offset=1140, name=None)),
         'satelites': None, 'placa': u'vlf571', 'motor': False, 'ubicacion': None, 'position': '(5.027412,-75.4504445)', 'altura': None}>,
         ....]
        >>> a = generalView()
        >>> for i in a:
        ...     print i.placa
        ...
        ttq000
        rjm270
        >>>
    """
    #return config.DB.query("""SELECT l.position, v.placa, g.name, l.fecha,
    #        l.velocidad, l.altura, l.satelites, l.ubicacion
    #        FROM vehiculos v, last_positions_gps l, gps g
    #        WHERE v.gps_id=g.id AND g.id=l.gps_id""")
    return config.DB.query("""SELECT l.position, v.placa, g.name, l.fecha,
                    l.velocidad, l.altura, l.satelites, l.ubicacion, vs.motor, v.active
                    FROM vehiculos v, last_positions_gps l, gps g, vehicle_state vs
                    WHERE v.gps_id=g.id AND g.id=l.gps_id AND vs.vehicle_id=v.id;""")

def show_avl():
    """view all the avl functionals"""
    return config.DB.query("""SELECT l.position, v.placa, g.name, g.aka,
                    g.active as gps_active, l.fecha, l.velocidad, l.altura,
                    l.satelites, l.ubicacion, vs.motor, v.active FROM
                    vehiculos v, last_positions_gps l, gps g, vehicle_state vs
                    WHERE v.gps_id=g.id AND g.id=l.gps_id AND
                    vs.vehicle_id=v.id ORDER BY fecha DESC;""")

def countEvent():
    """
        Retorna el numero de eventos sin gestionar.
        Usage:
        >>> from db import countEvent
        >>> a = countEvent()

    """
    return config.DB.query("""SELECT count(*) FROM eventos WHERE admin_state <> 't';""")

def insertPhone(storage, **sequence_id):
    """
            >>> from db import insertPhone
            >>> telefonos = {'fijo':'44444444', 'celular':u'', 'pbx':u'', 'fax':u''}
            >>> insertPhone(telefonos, client_id=1)
            0.0 (1): SELECT id FROM type_phone WHERE name='fijo'
            typePhone_id: 2
            0.0 (2): SELECT c.relname FROM pg_class c WHERE c.relkind = 'S'
            0.0 (3): INSERT INTO phones (phone, type) VALUES (44444444, 2); SELECT currval('phones_id_seq')
            seqPhone_id: 4
            0.0 (4): INSERT INTO phones_all (phone_id, client_id) VALUES (4L, 1)
            >>>
    """
    from web.db import sqlquote

    for name in storage:
        if storage[name]:
            try:
                typePhone_id = (config.DB.select('type_phone', what="id", where="name=" + sqlquote(name)))[0].id
                #print "typePhone_id:", typePhone_id
                # Insert public.phones
                seqPhone_id = config.DB.insert('phones', phone=storage[name], type=typePhone_id)
                #print "seqPhone_id:", seqPhone_id
                # Insert puiblic.phones_all
                seqPhone_all = config.DB.insert('phones_all', phone_id=seqPhone_id, **sequence_id)
                #print "seqPhone_all", seqPhone_all
            except:
                print "Error en insertPhone:"
                print sys.exc_info()

############### USER

def countEventClient(client_id):
    """
        Retorna el numero de eventos sin gestionar.
        Usage:
        >>> from db import countEventClient
        >>> client_id=1
        >>> a = countEventClient(client_id)
        0.0 (1): SELECT count(*)
                 FROM clientes_vehiculos cv, vehiculos v, gps g, eventos e
                 WHERE cv.vehiculo_id=v.id AND v.gps_id=g.id AND g.id=e.gps_id
                 AND user_state <> 't' AND cv.cliente_id=1
        >>> for i in a:
        ...     print i
        ...
        <Storage {'count': 42L}>
        >>>

    """
    from web.db import sqlquote
    #return config.DB.query("""SELECT count(*) FROM eventos WHERE admin_state <> 't';""")
    return config.DB.query("""SELECT count(*)
            FROM clientes_vehiculos cv, vehiculos v, gps g, eventos e
            WHERE cv.vehiculo_id=v.id AND v.gps_id=g.id AND g.id=e.gps_id
            AND user_state <> 't' AND cv.cliente_id=""" + sqlquote(client_id))

def listingVehicleClient(client_id):
    """
       Retorna los vehiculos del cliente.
       Usage:
       >>> from db import listingVehicleClient
       >>> client_id = 1
       >>>
       >>> a = listingVehicleClient(client_id)
       0.01 (1): SELECT v.id, lp.gps_id, v.placa,
                   lp.velocidad, lp.fecha, vs.motor, lp.ubicacion
                   FROM vehiculos v
                   INNER JOIN clientes_vehiculos AS cv ON (cv.vehiculo_id = v.id)
                   INNER JOIN last_positions_gps AS lp ON (lp.gps_id = v.gps_id)
                   LEFT OUTER JOIN vehicle_state AS vs ON (vs.vehicle_id = v.id)
                   WHERE cv.cliente_id=1
       >>> for i in a:
       ...     print i
       ...
       <Storage {'placa': u'rjm270', 'motor': False, 'velocidad': 1.0,
       'ubicacion': u'Calle 20 # 6-1 a 6-99, Pereira, Risaralda, Colombia',
       'fecha': datetime.datetime(2012, 9, 26, 13, 36, 40, 450917, tzinfo=psycopg2.tz.FixedOffsetTimezone(offset=1140, name=None)),
       'gps_id': 44, 'id': 5}>
       <Storage {'placa': u'ttq000', 'motor': False, 'velocidad': 1.0,
       'ubicacion': u'Carrera 6 # 16-2 a 16-100, Pereira, Risaralda, Colombia',
       'fecha': datetime.datetime(2012, 10, 6, 11, 24, 25, 411826, tzinfo=psycopg2.tz.FixedOffsetTimezone(offset=1140, name=None)),
       'gps_id': 10, 'id': 4}>
       >>>
    """
    from web.db import sqlquote
    return config.DB.query("""SELECT v.id, lp.gps_id, v.placa, lp.odometer, vs.horometer,
            lp.velocidad, lp.fecha, vs.motor, lp.ubicacion, lp.position, v.active
            FROM vehiculos v
            INNER JOIN clientes_vehiculos AS cv ON (cv.vehiculo_id = v.id)
            INNER JOIN last_positions_gps AS lp ON (lp.gps_id = v.gps_id)
            LEFT OUTER JOIN vehicle_state AS vs ON (vs.vehicle_id = v.id)
            WHERE cv.cliente_id=""" + sqlquote(client_id))

def eventsClient(client_id):
    """
        Retorna el numero de eventos sin gestionar.
        Usage:
        >>> from db import eventsClient
        >>> client_id=1
        >>> a = eventsClient(client_id)
        >>> for i in a:
        ...     print i
        ...
        <Storage {'name': u'ANT003', 'event_id': 63,
        'fecha': datetime.datetime(2012, 10, 8, 10, 19, 42, 544484, tzinfo=psycopg2.tz.FixedOffsetTimezone(offset=1140, name=None)),
        'placa': u'ttq000', 'vehi_id': 4, 'position_id': 185, 'descrip': u'Se Ha Encendico el Vehiculo',
        'ubicacion': u'Carrera 6 # 16-2 a 16-100, Pereira, Risaralda, Colombia', 'position': '(4.81534,-75.69189)', 'gps_id': 10}>
        >>>
    """
    from web.db import sqlquote
    return config.DB.query("""SELECT v.id AS vehi_id, v.placa, g.id AS gps_id, g.name, p.position, p.ubicacion, p.fecha,
            e.id AS event_id, p.id AS position_id, te.descrip
            FROM clientes_vehiculos cv, vehiculos v, gps g, eventos e, positions_gps p, type_event te
            WHERE cv.vehiculo_id=v.id AND v.gps_id=g.id AND g.id=e.gps_id
            AND p.id=e.positions_gps_id AND e.type=te.codigo
            AND user_state <> 't' AND v.active <> 'f' AND cv.cliente_id=""" + sqlquote(client_id))

def reportday(vehiculo_id, fecha):
    """
        Genera un reporte de las posiciones de un vehiculo para un
        día detreminado.
        Usage:
        >>> from db import reportday
        >>> v_id=5
        >>> f='27-08-2012'
        >>> a = reportday(v_id, f)
        0.0 (1): SELECT v.id, v.gps_id, v.placa,
                    p.velocidad, p.fecha, p.ubicacion, p.position
                    FROM vehiculos v
                    INNER JOIN positions_gps AS p ON (p.gps_id=v.gps_id)
                    WHERE v.id=5 and fecha between '27-08-2012 00:00:00' and '27-08-2012 23:59:60'
        >>>
        >>> for i in a:
        ...     print i
        ...
        <Storage {'placa': u'rjm270', 'velocidad': 1.0, 'ubicacion': u'N\xf3vita, Choco, Colombia', 'position': '(4.81534,-76.69489)',
         'fecha': datetime.datetime(2012, 8, 27, 17, 12, 37, 304536, tzinfo=psycopg2.tz.FixedOffsetTimezone(offset=1140, name=None)), 'gps_id': 44, 'id': 5}>
        <Storage {'placa': u'rjm270', 'velocidad': 1.0, 'ubicacion': u'Calle 20 # 6-1 a 6-99, Pereira, Risaralda, Colombia', 'position': '(4.81534,-75.69489)',
         'fecha': datetime.datetime(2012, 8, 27, 17, 13, 41, 51873, tzinfo=psycopg2.tz.FixedOffsetTimezone(offset=1140, name=None)), 'gps_id': 44, 'id': 5}>
         ...
        >>>
    """
    from web.db import sqlquote
    start_date = fecha + ' 00:00:00'
    end_date = fecha + ' 23:59:59'
    return config.DB.query("""SELECT v.id, v.gps_id, v.placa,
            p.velocidad, p.fecha, p.ubicacion, p.position
            FROM vehiculos v
            INNER JOIN positions_gps AS p ON (p.gps_id=v.gps_id)
            WHERE v.id=""" + sqlquote(vehiculo_id) +
            """ and fecha between """ + sqlquote(start_date) + """ and """ + sqlquote(end_date))


def allevent(vehiculo_id, fecha):
    from web.db import sqlquote
    start_datetime = fecha + ' 00:00:00'
    end_datetime = fecha + ' 23:59:59'

    return config.DB.query("""SELECT v.placa, p.velocidad,
        p.fecha, p.position, p.ubicacion, p.altura as alt,
        p.grados as curse, e.id AS event_id, te.name
        FROM vehiculos v
        LEFT JOIN positions_gps AS p ON (p.gps_id=v.gps_id)
        LEFT JOIN eventos AS e ON (e.positions_gps_id=p.id)
        LEFT JOIN type_event AS te ON (te.codigo=e.type)
        WHERE v.id=""" + sqlquote(vehiculo_id) + """ AND
        p.fecha between """ + sqlquote(start_datetime) + """
        AND """ + sqlquote(end_datetime) + """ ORDER BY p.fecha, e.id""")


# Admin Charts

def gpsCharts():
    """
        Retorna una consulta de los dispositivos creados para los meses y años.
         año  | mes | count
        ------+-----+-------
         2012 |   8 |     2
         2012 |  10 |     3
         2012 |  11 |    12
        (3 filas)

    """
    #return config.DB.query("""select date_part('year', g.fecha_creacion) as year,
    #        date_part('month'::text, g.fecha_creacion) as month, count(g.id)
    #        from gps as g
    #        group by year, month order by (year);""")
    return config.DB.query("""select date_part('year', g.fecha_creacion) as year,
            date_part('month'::text, g.fecha_creacion) as month, count(g.id)
            from gps as g
            group by year, month order by year, month;""")

# Admin "Perfil de Usuario"
def listingClient(idClient):
    """
        Lista todos los datos del Cliente según el id proporcionado.

        Usage:
        >>> from db import listingClient
        >>> u = listingClient(1)
        0.0 (1): SELECT * FROM clientes WHERE id=1
        >>> u
        <Storage {'nombre1': u'jorge', 'nombre2': u'alonso', 'fecha_naci': datetime.date(1982, 11, 2), 'apellido1': u'toro',
        'direccion': u'Cra 11 # 15-15 APT 601 BL 2B', 'apellido2': u'hoyos', 'ciudad': u'17001', 'tipo_docu': 1, 'id': 1,
        'sexo_id': 1, 'email': u'jolthgs@gmail.com', 'documento': u'11814584'}>
        >>>
    """
    from web.db import sqlquote
    #return config.DB.query("""SELECT * FROM usuarios where id="""+ sqlquote(idClient))
    return config.DB.select('clientes', where='id=' + sqlquote(idClient))[0]

# Lista un vehículo
def listVehicle(idVehicle):
    """
        Lista todos los datos de un vehículo.

        usage:
        >>> from db import listVehicle
        >>>
        >>> id = 9
        >>> v = listVehicle(id)
        0.01 (2): SELECT v.placa, g.name, m.descrip AS marca, v.modelo,
                    v.cilindraje, v.ejes, l.descrip AS linea,
                    c.descrip AS clase, ca.descrip AS carroceria, co.descrip AS color,
                    cb.descrip AS combustible, sv.descrip AS servicio
                    FROM vehiculos AS v
                    LEFT OUTER JOIN gps AS g ON (v.gps_id=g.id)
                    LEFT OUTER JOIN marcas_vehiculo AS m ON (v.marca_id=m.id)
                    LEFT OUTER JOIN liena_vehiculo AS l ON (v.linea_id=l.id)
                    LEFT OUTER JOIN clase_vehiculo AS c ON (v.clase_id=c.id)
                    LEFT OUTER JOIN carrocerias AS ca ON (v.carroceria_id=ca.id)
                    LEFT OUTER JOIN colores AS co ON (v.color_id=co.id)
                    LEFT OUTER JOIN combustibles AS cb ON (v.combustible_id=cb.id)
                    LEFT OUTER JOIN servicio_vehiculo AS sv ON (v.servicio_id=sv.id)
                    WHERE v.id=9
        <Storage {'servicio': None, 'carroceria': u'Estacas', 'cilindraje': 5.1929999999999996,
        'color': None, 'ejes': 2, 'combustible': u'Diesel', 'clase': u'Cami\xf3n',
        'marca': u'Chevrolet', 'placa': u'stp326', 'modelo': 2012, 'linea': None, 'name': u'SKP002'}>
        >>> v.placa
        u'stp326'
        >>>
    """
    from web.db import sqlquote

    return config.DB.query("""SELECT v.placa, g.name, m.descrip AS marca, v.modelo,
            v.cilindraje, v.ejes, l.descrip AS linea,
            c.descrip AS clase, ca.descrip AS carroceria, co.descrip AS color,
            cb.descrip AS combustible, sv.descrip AS servicio
            FROM vehiculos AS v
            LEFT OUTER JOIN gps AS g ON (v.gps_id=g.id)
            LEFT OUTER JOIN marcas_vehiculo AS m ON (v.marca_id=m.id)
            LEFT OUTER JOIN liena_vehiculo AS l ON (v.linea_id=l.id)
            LEFT OUTER JOIN clase_vehiculo AS c ON (v.clase_id=c.id)
            LEFT OUTER JOIN carrocerias AS ca ON (v.carroceria_id=ca.id)
            LEFT OUTER JOIN colores AS co ON (v.color_id=co.id)
            LEFT OUTER JOIN combustibles AS cb ON (v.combustible_id=cb.id)
            LEFT OUTER JOIN servicio_vehiculo AS sv ON (v.servicio_id=sv.id)
            WHERE v.id=""" + sqlquote(idVehicle))[0]


###############  controlmonitoring


def check_plate(plate=None):
    """Check if vehicle exists.

    >>> from db import check_plate
    >>> check_plate('TK303')
    0.01 (1): select exists (select 1 from vehiculos where
                            placa=lower('TK303'))
    True
    """
    from web.db import sqlquote
    res = config.DB.query("""select exists (select 1 from vehiculos where
                           placa=lower('%s'))""" % plate)
    return res[0]["exists"]

def vehicle_reports(plate, started=None, endend=None):
    """get history of the reports for vehícle.

    >>> from db import vehicle_reports
    >>>
    >>> f = vehicle_reports('TK303')
    0.51 (1): SELECT p.id, v.placa, p.velocidad, p.fecha, p.position,
        p.ubicacion, p.altura, p.grados, e.id AS event_id, te.name
        FROM vehiculos v
        LEFT JOIN positions_gps AS p ON (p.gps_id=v.gps_id)
        LEFT JOIN eventos AS e ON (e.positions_gps_id=p.id)
        LEFT JOIN type_event AS te ON (te.codigo=e.type)
        WHERE v.placa=lower('TK303') AND p.fecha between '2022-09-27'
            and '2022-09-27 23:59:59' ORDER BY p.fecha, e.id
    >>>
    >>> for r in f:
    ...     print(r)

    """
    import datetime

    today = datetime.date.today()
    query = """SELECT p.id, v.placa, p.velocidad, p.fecha, p.position,
    p.ubicacion, p.altura, p.grados, e.id AS event_id, te.name
    FROM vehiculos v
    LEFT JOIN positions_gps AS p ON (p.gps_id=v.gps_id)
    LEFT JOIN eventos AS e ON (e.positions_gps_id=p.id)
    LEFT JOIN type_event AS te ON (te.codigo=e.type)
    WHERE v.placa=lower('{plate}')""".format(plate=plate)

    started = today.strftime("%Y-%m-%d") if started is None else started
    endend = today.strftime("%Y-%m-%d 23:59:59") if endend is None\
            else "{} 23:59:59".format(endend)

    try:
        query="""{query} AND p.fecha between '{started}'
        and '{endend}' ORDER BY p.fecha, e.id""".format(
                                                    query=query,
                                                    started=started,
                                                    endend=endend)
        return config.DB.query(query)
    except EOFError as e:
        raise e
