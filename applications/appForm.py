# -*- coding: utf-8 -*-
from web import form
from db import listingDropdown


# Formulario addgps:
formGps = form.Form(
    form.Textbox("name",
        form.notnull,
        form.Validator('El nombre para el Dispositivo con el formato: [ANT|SKP]001', lambda x: len(x)>5),
        form.Validator('No es un Dispositivo valido. Debe usar [ANT|SKP...] como nombre', lambda x: [d for d in ('HUT', 'SKP', 'ANT') if d==x[:3]]),
        class_="input", description="Nombre", maxlength="10"),
    form.Dropdown('type', [(0, 'Seleccione un Tipo')] + listingDropdown('type_gps', "codigo,descrip", "codigo ASC"),
        form.Validator('Debe seleccionar un dispositivo', lambda x: int(x) > 0) , description="Tipo GPS", class_="chzn-select"),
    form.Textbox("number_sim", class_="input", description="numero de la SIM",
                 maxlength="15"),
    form.Checkbox('active', value='activo', checked=True, description="Activo")
)

# Formulario assignclient:
formAssignclient = form.Form(
    #form.Dropdown('cliente_id', [(0, 'Seleccione un Cliente')] + listingDropdown('clientes', "id,documento", "id ASC"),
    #    form.Validator('Debe seleccionar un dispositivo', lambda x: int(x) > 0) , description="Cliente", class_="chzn-select"),
    form.Dropdown('cliente_id', [(0, 'Seleccione un Cliente')],
        form.Validator('Debe seleccionar un cliente', lambda x: int(x) > 0) , description="Cliente", class_="chzn-select"),
    #form.Dropdown('vehiculo_id', [(0, 'Seleccione un Vehículo')] + listingDropdown('vehiculos', "id,placa", "id ASC"),
    #    form.Validator('Debe seleccionar un dispositivo', lambda x: int(x) > 0) , description="Vehículo", class_="chzn-select"),
    form.Dropdown('vehiculo_id', [(0, 'Seleccione un Vehículo')],
        form.Validator('Debe seleccionar un vehículo', lambda x: int(x) > 0) , description="Vehículo", class_="chzn-select"),
)

# Formulario adduser:
formUser = form.Form(
    form.Dropdown('cliente_id', [(0, 'Seleccione un Cliente')],
        form.Validator('Debe seleccionar un Cliente', lambda x: int(x) > 0), description="Cliente", class_="chzn-select"),
    #form.Dropdown('cliente_id', [(0, 'Seleccione un Cliente')] + listingDropdown('clientes', "id,documento", "id DESC"),
    #    form.Validator('Debe seleccionar un Cliente', lambda x: int(x) > 0), description="Cliente", class_="chzn-select"),
    form.Textbox("usuario",
        form.notnull,
        #form.Validator('El nombre para el Dispositivo con el formato: [ANT|SKP]001', lambda x: len(x)>5),
        #form.Validator('No es un Dispositivo valido. Debe usar [ANT|SKP...] como nombre', lambda x: [d for d in ('HUT', 'SKP', 'ANT') if d==x[:3]]),
        class_="input", description="Nombre", maxlength="30"),
    form.Password('passwd', form.notnull, class_="input", description="Contraseña", maxlength="50"),
    form.Password('passwd_again', form.notnull, class_="input", description="Repita Cña", maxlength="50"),
    #validators = [form.Validator(unicode('Las contraseñas no coinciden.', 'utf-8'), lambda i: i.password == i.password_again)],
    form.Dropdown('privilege_id', [(0, 'Seleccione Privilegio')] + listingDropdown('privileges', "id,descrip", "id ASC"),
        form.Validator('Debe seleccionar un Privilegio para el usuario', lambda x: int(x) > 0), description="Privilegios", class_="chzn-select"),
    form.Checkbox('activo', value='activo', checked=True, description="Activo"),
    validators = [form.Validator('Las contraseñas no coinciden.', lambda i: i.passwd == i.passwd_again)],
)

# Formulario addvehicle:
formVeh = form.Form(
    form.Textbox("placa",
        form.notnull, post='*',
        class_="input", description="Placa", maxlength="10"),
    #form.Dropdown('gps_id', [('0', 'Dispositivo GPS')] + listingDropdown('gps', "id,name", "id DESC"),
    #    form.notnull,
    #    form.Validator('Debe seleccionar un Dispositivo GPS para el Vehículo', lambda x: int(x) > 0),
    #    post='*', description="Gps", class_="chzn-select"),
    form.Dropdown('gps_id', [('0', 'Dispositivo GPS')],
        form.notnull,
        form.Validator('Debe seleccionar un Dispositivo GPS para el Vehículo', lambda x: int(x) > 0),
        post='*', description="Gps", class_="chzn-select"),
    form.Dropdown('marca_id', [(0, 'Seleccione la Marca')] + listingDropdown('marcas_vehiculo', "id,descrip", "id ASC"),
        form.Validator('Debe seleccionar un tipo de Marca para el Vehículo', lambda x: int(x) > 0),
        post='*', description="Marca", class_="chzn-select"),
    form.Textbox("modelo", form.notnull,
        form.Validator('El Modelo debe ser un año (Por ejemplo: 1978)', lambda x: x.isdigit()), post='*',
        class_="input", description="Modelo", maxlength="4"),

    form.Dropdown('clase_id', [(None, u'Clase del Vehículo')] + listingDropdown('clase_vehiculo', "id,descrip", "id ASC"), #form.notnull,
        #form.Validator('Debe seleccionar una Clase para el Vehículo', lambda x: int(x) > 0),
        description="Clase", class_="chzn-select"),
    form.Dropdown('combustible_id', [(None, 'Seleccione un tipo')] + listingDropdown('combustibles', "id,descrip", "id ASC"),
        #form.Validator('Debe seleccionar un tipo de Combustible para el Vehículo', lambda x: int(x) > 0),
        description="Combustible", class_="chzn-select"),
    form.Dropdown('carroceria_id', [(None, 'Seleccione un tipo')] + listingDropdown('carrocerias', "id,descrip", "id ASC"),
        #form.Validator('Debe seleccionar un tipo de Carroceria para el Vehículo', lambda x: int(x) > 0),
        description="Carrocería", class_="chzn-select"),
    form.Textbox("cilindraje",
        class_="input", description="Cilindraje", maxlength="6"),
    form.Textbox("ejes",
        class_="input", description="Ejes", maxlength="1"),

    form.Dropdown('linea_id', [(None, 'Seleccione un tipo')] + listingDropdown('liena_vehiculo', "id,descrip", "id ASC"),
        #form.Validator('Debe seleccionar un tipo de Carroceria para el Vehículo', lambda x: int(x) > 0),
        description="Línea", class_="chzn-select"),
    form.Dropdown('color_id', [(None, 'Seleccione un tipo')] + listingDropdown('colores', "id,descrip", "id ASC"),
        #form.Validator('Debe seleccionar un tipo de Carroceria para el Vehículo', lambda x: int(x) > 0),
        description="Colores", class_="chzn-select"),
    form.Dropdown('servicio_id', [(None, 'Sevicio del Vehículo')] + listingDropdown('servicio_vehiculo', "id,descrip", "id ASC"),
        #form.Validator('Debe seleccionar un tipo de Servicio para el Vehículo', lambda x: int(x) > 0),
        description="Servicio", class_="chzn-select"),

)

# Formulario addclient:
formClient = form.Form(
    form.Textbox("nombres",
        form.notnull,
        class_="input", description="Nombres", maxlength="30"),
    form.Textbox("apellidos",
        form.notnull,
        class_="input", description="Apellidos", maxlength="30"),
    form.Textbox("documento",
        form.notnull,
        form.regexp('\d+', 'Deben ser digitos'),
        class_="input", description="Documento", maxlength="50"),
    form.Dropdown('tipo_docu', [(0, 'Tipo de Documento')] + listingDropdown('type_document', "id,descrip", "id ASC"),
        form.Validator('Debe seleccionar un tipo de Documento', lambda x: int(x) > 0), description="", class_="chzn-select"),
    form.Textbox("fecha_naci",
        form.notnull,
        form.regexp('^\d{2}\/\d{2}\/\d{4}$', 'Deben ser una fecha DD/MM/AAAA (Por ejemplo: 01/01/1978)'),
        class_="input", description="Fecha Nac.", maxlength="10"),
    form.Dropdown('sexo_id', [(0, 'Género')] + listingDropdown('sexo', "id,descrip", "id ASC"),
        form.Validator('Debe seleccionar un tipo de sexualidad para el usuario', lambda x: int(x) > 0), description="Sexo", class_="chzn-select"),
    form.Textbox("direccion",
        form.notnull,
        class_="input", description="Dirección", maxlength="100"),
    form.Dropdown('ciudad', [(0, 'Municipios')] + listingDropdown('municipio', "codigo,descrip"),
        form.Validator('Debe seleccionar un Municipio', lambda x: int(x) > 0), description="Ciudad", class_="chzn-select"),
    form.Textbox("fijo",
        #form.notnull,
        #form.regexp("^[a-zA-Z0-9._%-+]+@[a-zA-Z0-9._%-]+.[a-zA-Z]{2,6}$", 'Esto no es un e-mail'),
        class_="input tele", description="Tel. Fijo", maxlength="60", id="Fijo", value="tel1, tel2,...teln"),
    form.Textbox("celular",
        #form.notnull,
        #form.regexp("^[a-zA-Z0-9._%-+]+@[a-zA-Z0-9._%-]+.[a-zA-Z]{2,6}$", 'Esto no es un e-mail'),
        class_="input tele", description="Celular", maxlength="60", id="Celular", value="tel1, tel2,...teln"),
    form.Textbox("fax",
        #form.notnull,
        #form.regexp("^[a-zA-Z0-9._%-+]+@[a-zA-Z0-9._%-]+.[a-zA-Z]{2,6}$", 'Esto no es un e-mail'),
        class_="input tele", description="FAX", maxlength="60", id="Fax", value="tel1, tel2,...teln"),
    form.Textbox("pbx",
        #form.notnull,
        #form.regexp("^[a-zA-Z0-9._%-+]+@[a-zA-Z0-9._%-]+.[a-zA-Z]{2,6}$", 'Esto no es un e-mail'),
        class_="input tele", description="PBX", maxlength="60", id="Pbx", value="tel1, tel2,...teln"),
    form.Textbox("email",
        form.regexp("^[a-zA-Z0-9._%-+]+@[a-zA-Z0-9._%-]+.[a-zA-Z]{2,6}$", 'Esto no es un e-mail'),
        class_="input", description="E-mail", maxlength="60", id="email", value='mail@localhost.com'),
)

# Formulario SendData (sendata):
formSendata = form.Form(
    form.Dropdown('gps_id', [('0', 'Dispositivo GPS')],
        form.notnull,
        form.Validator('Debe seleccionar un Dispositivo GPS para el Vehículo', lambda x: int(x) > 0),
        post=' *', description="Gps", class_="chzn-select"),
    form.Textarea('Comandos', form.notnull, cols="40", rows="5"),
    form.Textarea('Comentarios', cols="40"),
    #form.Dropdown('cliente_id', [(0, 'Seleccione un Cliente')] + listingDropdown('clientes', "id,documento", "id ASC"),
    #    form.Validator('Debe seleccionar un dispositivo', lambda x: int(x) > 0) , description="Cliente", class_="chzn-select"),
    #form.Dropdown('cliente_id', [(0, 'Seleccione un Cliente')],
    #    form.Validator('Debe seleccionar un cliente', lambda x: int(x) > 0) , description="Cliente", class_="chzn-select"),
    #form.Dropdown('vehiculo_id', [(0, 'Seleccione un Vehículo')] + listingDropdown('vehiculos', "id,placa", "id ASC"),
    #    form.Validator('Debe seleccionar un dispositivo', lambda x: int(x) > 0) , description="Vehículo", class_="chzn-select"),
    #form.Dropdown('vehiculo_id', [(0, 'Seleccione un Vehículo')],
    #    form.Validator('Debe seleccionar un vehículo', lambda x: int(x) > 0) , description="Vehículo", class_="chzn-select"),
)
