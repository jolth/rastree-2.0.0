# -*- coding: utf-8 -*-
"""Módulo Atalaya

Autor: Jorge A. Toro [jolthgs@gmail.com]
Copyright (c) 2014 Dev Microsystem S.A.S.

"""
import web
from common import Sesion
from view import render_controlmonitoring as render
import db
import datetime

urls = (
    "", "reuser",
    "/", "dashboard",
    "/overview", "overview",
    "/reports", "reports"
)


class reuser:
    def GET(self):
        raise web.seeother('/')


class dashboard:
    @Sesion
    def GET(self):
        return render.base(render.dashboard(), "Dashboard")


class overview:
    @Sesion
    def GET(self):
        from db import listingAllVehicle
        #vehicles = db.generalView()
        #return render.base(render.overview(vehicles, datetime), "Overview")
        vehicles = db.show_avl()
        return render.base(render.overview(vehicles, datetime), "Overview")


class reports:
    @Sesion
    def GET(self):
        return render.base(render.reports(), "Reports")


app_controlmonitoring = web.application(urls, locals())
