# -*- coding: utf-8 -*-
import web
import config
#import db
#import re
#import datetime

# No usar 't_globals':
#t_globals = dict(
#  datestr=web.datestr,
#)

# Produccción
#render = web.template.render('/var/www/rastree/templates/', cache=config.cache) 
#    globals=t_globals)
render = web.template.render('templates/', cache=config.cache)
#    globals=t_globals)


#render._keywords['globals']['render'] = render

# Producción
#renderbase_admin = web.template.render('/var/www/rastree/templates/admin', 
#        base='layout', cache=config.cache)
renderbase_admin = web.template.render('templates/admin',
        base='layout', cache=config.cache)

# Producción
#render_atalaya = web.template.render("templates/atalaya/")
render_atalaya = web.template.render("templates/atalaya/")

# Production
#render_controlmonitoring = web.template.render("/var/www/rastree/templates/controlmonitoring/")
#render_controlmonitoring = web.template.render("templates/controlmonitoring/")
render_controlmonitoring = web.template.render("templates/controlmonitoring/",
                           cache=False)

# Production
render_fleet = web.template.render("templates/fleet/")
