# -*- coding: utf-8 -*-
"""
    Módulo Atalaya

    Autor: Jorge A. Toro [jolthgs@gmail.com]
    Copyright (c) 2014 Dev Microsystem S.A.S. 
"""
import web
from common import Sesion
from view import render_atalaya as render

urls = (
    "", "reuser",
    "/", "dashboard"
)

class reuser:
    def GET(self):
        raise web.seeother('/')

class dashboard:
    @Sesion
    def GET(self):
        return render.base(render.dashboard(), "Dashboard")



app_atalaya = web.application(urls, locals())
