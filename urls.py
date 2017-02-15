# -*- coding:utf-8 -*-
"""
URL's
"""
import applications.user as user
import applications.admin as admin
import applications.coordinator as coordinator
import applications.company as company
import applications.driver as driver
import applications.atalaya as atalaya
import applications.controlmonitoring as controlmonitoring
#import applications.fleet as fleet

#urls = (
#    '/(styles|js|img)/(.*)', 'static',
#    '/', 'login'
#)

urls = (
    "/user", user.app_user,
    "/admin", admin.app_admin,
    "/coordinator", coordinator.app_coordinator,
    "/company", company.app_company,
    "/driver", driver.app_driver,
    "/atalaya", atalaya.app_atalaya,
    "/controlmonitoring", controlmonitoring.app_controlmonitoring,
    #"/fleet", fleet.app_fleet,
    # 
    "/", 'Index',
    "/login", 'Login',
    "/logout", 'Logout'
)



