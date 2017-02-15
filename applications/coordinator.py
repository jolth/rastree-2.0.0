# -*- coding: utf-8 -*-
import web
from common import Sesion

from view import render

urls = (
  "", "reuser",
  "/", "monitoreo",
)


class reuser:
    def GET(self):
        raise web.seeother('/')

class monitoreo:
    @Sesion
    def GET(self):
        if web.ctx.session.get('logged_in'):
            print "Login: Si"
        else: print "Login: No"

        #return render.coordinator.monitoreo(web.ctx.path, web.ctx.session.get('logged_in')) 
        return render.coordinator.monitoreo(web.ctx.session) 
        #return render.coordinator.monitoreo() 

#class Login:
#    def GET(self):
#        web.ctx.session.logged_in = True
#        raise web.seeother('/')


app_coordinator = web.application(urls, locals())
