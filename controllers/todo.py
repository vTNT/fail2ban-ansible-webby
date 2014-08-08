#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2013-07-30 14:37:47
# @Author  : Your Name (you@example.org)
# @Link    : http://example.org
# @Version : $Id$

import web
from config import settings
from datetime import datetime
import base

render = settings.render
db = settings.db
config = settings.config
admin = config.admin
pwd = config.password

tb = 'atta'

class Index:

    def GET(self,page=1,statustype='ban'):
        if not base.logged():
            raise web.seeother('/')
        else:
            page = int(page)
            perpage = 10
            current_page = page
            page_status = statustype
            offset = (page-1) * perpage
            if statustype == 'fail' :
                todos = db.select(tb, where="action='unban' and status = 1",order='time asc, id asc',offset=offset,limit=perpage,vars=locals())
                sql = 'select * from atta where action="unban" and status = 1' 
            else:
                todos = db.select(tb, where='action=$statustype and status = 0',order='time asc, id asc',offset=offset,limit=perpage,vars=locals())
                sql = 'select * from atta where action="%s" and status = 0' % statustype
            postcount = len(db.query(sql))
            pages = postcount / perpage
            print page,pages,postcount
            if postcount % perpage > 0:
                pages += 1
            if page > pages:
                raise web.seeother('/main')
            else:
                return render.index(config=config,todos=todos,pages=pages,current_page=current_page,statustype=statustype,page_status=page_status)


class Delete:

    def GET(self, id):
        db.delete(tb, where='id=$id', vars=locals())
        raise web.seeother('/main')

class Search:

    def POST(self):
        i = web.input()
        timeafter = i['timeafter']
        timebefore = i['timebefore']
        sql = 'select * from atta where post_date between "%s" and "%s" ' % (timebefore, timeafter)
        todos = db.query(sql)
        num = len(todos)
        return render.search(todos=todos,config=config,num=num)
       # return render.search(timeafter=timeafter,timebefore=timebefore,config=config)
       
class Ansible:

    def GET(self,type='main'):
        if not base.logged():
            raise web.seeother('/')
        else:
            return render.job(config=config)

class Login:
    def GET(self):
        if base.logged():
            raise web.seeother('/main')
        else:
            return render.login()

    def POST(self):
        username = web.input().username
        password = web.input().password

        if (password == pwd) and (username == admin):
            web.ctx.session.logined = 1
            raise web.seeother('/main')
        else:
            return "you are wrong!!"

class Logout:
    def GET(self):
        web.ctx.session.kill()
        raise web.seeother('/')
