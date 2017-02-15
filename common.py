# -*- coding: utf-8 -*-
import web

# Decorador para verificar la conexión (session)
# de los usuarios, para cada una de las URL (clases)
def Sesion(url):
    def verificaSesion(*args, **kwargs):
        #print "Verificando Session: %s" % web.ctx.session.get('logged_in')
        #print "Proviene", web.ctx.env.get('PATH_INFO') 
        #print "PATH", web.ctx.path
        #print "########"
        #print "HOMEPATH:", web.ctx.homepath
        #print "PRIVILEGE:", web.ctx.session.get('homepath')
        #print "SESSIONHOMEPATH:", web.ctx.session.homepath # except si no existe
        #print "########"
        #print "HOMEDOMAIN", web.ctx.homedomain
        if web.ctx.session.get('logged_in'):
            # Verificar q el ususio si 
            if web.ctx.homepath == web.ctx.session.homepath:
                return url(*args, **kwargs) # Llamamos a la clases 
        #print "Proviene", web.ctx.env.get('PATH_INFO') 
        #print "PATH", web.ctx.path
        #print "HOMEPATH", web.ctx.homepath
        #print "HOMEDOMAIN", web.ctx.homedomain
        #raise web.seeother('/login')
        raise web.seeother(web.ctx.homedomain)
    return verificaSesion
