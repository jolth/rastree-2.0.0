# -*- coding: utf-8 -*-
"""
Autor: Jorge A. Toro [jolthgs@gmail.com]
Copyright: 2012 - 2018
"""
import web
from urls import urls
# import view, config
from view import render
import sys
import os
ROOT_PATH = os.path.dirname(__file__)
sys.path.append(ROOT_PATH)


# Producción
# web.config.debug = False
# Testing
web.config.debug = True

app = web.application(urls, globals())

if web.config.get('_sesion') is None:
    # Quitar en Producción:
    session = web.session.Session(
        app, web.session.DiskStore('sesiones'), {'count': 0})
    web.config._sesion = session

    # Producción
    #curdir = os.path.dirname(__file__)
    #session = web.session.Session(
    #    app, web.session.DiskStore(
    #        os.path.join(curdir, 'sesiones')), {'count': 0})
    #web.config._sesion = session
else:
    session = web.config._sesion


def session_hook():
    # Session available in Sub-apps
    web.ctx.session = session
    # Sessions avaible in templates
    web.template.Template.globals['sesion'] = session


app.add_processor(web.loadhook(session_hook))


class Index:
    def GET(self):
        if session.get('logged_in', False):
            referer = web.ctx.env.get('HTTP_REFERER', web.ctx.homedomain)
            # Resuelve el Referer
            if referer is web.ctx.homedomain:
                raise web.seeother('/login')
            raise web.seeother(referer)
        raise web.seeother('/login')


class Login:
    def GET(self):
        return render.login()

    def POST(self):
        from db import listingUser

        i = web.input()
        result = listingUser(vars=locals())
        if result:
            from db import listingPrivilege, getNameClient, lastentry

            clienteId, idUser, privilegeId = result[0].values()

            session.logged_in = True
            # usuario
            session.user = i.username

            # Last Entry:
            lastentry(idUser)

            # App Companies:
            if privilegeId == 4:
                try:
                    from db import getCompany
                    # Otenemo los datos de la compañia:
                    session.company = getCompany(vars=locals())
                except:
                    # Si el cliente no esta asociado a una
                    # empresa en public.clientes_empresa:
                    session.logged_in = False
                    return render.login(u'Sesión %s. No se tiene una empresa\
                        parar este usuario.' % session.get('logged_in', False))

            # ID Cliente (clientes.id):
            session.clienteId = clienteId
            # Nombre del cliente:
            session.username = getNameClient(vars=locals())
            # Homepath según usuarios.privilege_id
            session.homepath = listingPrivilege(vars=locals())
            raise web.seeother(session.homepath)
        else:
            return render.login(u'Sesión %s. Usuario o Contraseña\
                    inválido(s).' % session.get('logged_in', False))


class Logout:
    def GET(self):
        session.logged_in = False
        raise web.seeother('/')


# Producción
#application = app.wsgifunc()
if __name__ == "__main__":
    app.run()
