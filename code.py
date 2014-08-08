#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2013-07-30 14:22:46
# @Author  : Your Name (you@example.org)
# @Link    : http://example.org
# @Version : $Id$

from config.url import urls
import web,os

app = web.application(urls,globals())

# Loading system config
app = web.application(urls, globals())

# Define sessions
curdir = os.path.dirname(__file__)

if web.config.get('_session') is None:
    session = web.session.Session(app, web.session.DiskStore(os.path.join(curdir, 'sessions')), initializer={'logined': 0, 'uid': 0, 'username': '', 'privilege': 0})
    web.config._session = session
else:
    session = web.config._session

def session_hook():
    web.ctx.session = session

app.add_processor(web.loadhook(session_hook))

if __name__ == "__main__":
    app.run()
