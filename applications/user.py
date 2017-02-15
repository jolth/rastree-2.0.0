# -*- coding: utf-8 -*-
import web
from common import Sesion

from view import render

urls = (
  "", "reuser",
  "/", "dashboard",
  "/eventos", "eventos",
  "/search", "search",
  "/reportday", "reportday",
  "/reporthistoric", "reporthistoric",
  "/printreportday", "printreportday",
  # JSON
  "/reportdayjson", "reportdayjson",
  "/listeventjson", "listeventjson",
  "/listvehiclesjson", "listvehiclesjson",
)


class reuser:
    def GET(self):
        raise web.seeother('/')

class dashboard:
    @Sesion
    def GET(self):
        from db import listingVehicleClient
        #return render.user.monitoreo(web.ctx.path, web.ctx.session) 
        return render.user.dashboard(web.ctx.session, listingVehicleClient(web.ctx.session.clienteId))

class eventos:
    @Sesion
    def GET(self):
        #web.ctx.session.logged_in = True
        #raise web.seeother('/')

        #return eventos
        #return render.user.eventos(web.ctx.session)
        #from db import listingVehicleClient
        #return render.user.eventos(web.ctx.session, listingVehicleClient(web.ctx.session.clienteId))
        from db import eventsClient
        return render.user.eventos(web.ctx.session, eventsClient(web.ctx.session.clienteId))

class search:
    @Sesion
    def GET(self):
        from db import listingVehicleClient
        return render.user.search(web.ctx.session, listingVehicleClient(web.ctx.session.clienteId))

class reportday:
    @Sesion
    def GET(self):
        from db import listingVehicleClient
        return render.user.reportday(web.ctx.session, listingVehicleClient(web.ctx.session.clienteId))

class printreportday:
    @Sesion
    def GET(self): # Pasarlo a POST
        """
           http://127.0.0.1:8080/user/printreportday?carid=9&date=04-02-2013
        """
        i = web.input(carid=None, date=None)
        from db import reportday, listVehicle, listingVehicleClient
        try:
            return render.user.printreportday(i.date, listVehicle(i.carid), reportday(i.carid, i.date))
        except:
            return render.user.reportday(web.ctx.session, listingVehicleClient(web.ctx.session.clienteId))

class reporthistoric:
    @Sesion
    def GET(self):
        return reporthistoric


###### JSON

class reportdayjson:
    @Sesion
    def GET(self):
        """
            http://127.0.0.1:8080/user/reportdayjson?id=5&fecha=27-08-2012
        """
        import simplejson as json 
        from db import reportday

        i = web.input(id=None, fecha=None)
        print "VEHICLE ID: ", i.id
        print "FECHA: ", i.fecha
        web.header('content-Type', 'application/json')
        def dthandler(obj):
            obj.fecha = obj.fecha.strftime("%F %H:%M:%S")
            return obj
        return json.dumps([dthandler(row) for row in reportday(i.id, i.fecha)])

class listeventjson:
    @Sesion
    def GET(self):
        import simplejson as json 
        from db import countEventClient
        web.header('content-Type', 'application/json')
        return json.dumps([row for row in countEventClient(web.ctx.session.clienteId)])
 

class listvehiclesjson:
    @Sesion
    def GET(self):
        import simplejson as json 
        from db import listingVehicleClient
        web.header('content-Type', 'application/json')
        #return json.dumps([row for row in listingVehicleClient(web.ctx.session.clienteId)])
        def dthandler(obj):
            obj.fecha = obj.fecha.strftime("%F %H:%M:%S")
            return obj
        #return json.dumps([dthandler(row) for row in views])
        return json.dumps([dthandler(row) for row in listingVehicleClient(web.ctx.session.clienteId)])

        

app_user = web.application(urls, locals())
