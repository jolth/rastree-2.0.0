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
    "/reports", "reports",
    "/check_plate", "check_plate",
    "/reports_json", "reports_json"
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


class check_plate:
    @Sesion
    def GET(self):
        "http://localhost:8080/controlmonitoring/check_plate?plate=${plate}"
        from db import check_plate as chp
        import simplejson as json

        ipt = web.input(plate=None)
        web.header('content-Type', 'application/json')
        res = chp(ipt.plate)

        return json.dumps({'plate': res})


class reports_json:
    @Sesion
    def GET(self):
        """http://localhost/controlmonitoring/reports_json?plate=tk303
        http://localhost/controlmonitoring/reports_json?plate=tk303&started=2022-09-27
        """
        import simplejson as json
        from db import vehicle_reports

        ipt = web.input(plate=None, started=None, endend=None)
        web.header('content-type', 'application/json')

        print(ipt.plate, ipt.started, ipt.endend) # testing
        assert ipt.endend is not None
        return json.dumps(map(parse_date, vehicle_reports(ipt.plate,
                                                          ipt.started,
                                                          ipt.endend)))


def parse_date(obj):
    """Convert obj.datetime"""
    obj.fecha = obj.fecha.strftime("%F %X%z")
    return obj



app_controlmonitoring = web.application(urls, locals())
