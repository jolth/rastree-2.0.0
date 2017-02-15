# -*- coding: utf-8 -*-
import web
from common import Sesion

from view import render

urls = (
  "", "reuser",
  "/", "dashboard",
  "/user_profile", "userProfile",
  "/informes", "informes",
  "/localizacion","localizacion",
)


class reuser:
    def GET(self):
        raise web.seeother('/')

class dashboard:
    @Sesion
    def GET(self):
        return render.company.dashboard(web.ctx.session) 

class informes:
    @Sesion
    def GET(self):
        return render.company.informes(web.ctx.session)

class userProfile:
    @Sesion
    def GET(self):
        return render.company.user_profile(web.ctx.session)

class localizacion:
    @Sesion
    def GET(self):
        return render.company.localizacion(web.ctx.session)



app_company = web.application(urls, locals())
