#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2013-07-30 14:28:06
# @Author  : Your Name (you@example.org)
# @Link    : http://example.org
# @Version : $Id$

import web
from web.contrib.template import render_jinja

db = web.database(dbn='mysql', db='fail2ban', user='root', pw='110', host='192.168.200.209')

render = render_jinja(
    'templates',
    encoding = 'utf-8',
    )

web.config.debug = True

config = web.storage(
    email = 'this is the test',
    site_name = 'this is the test',
    site_desc = '',
    static = '/static',
    admin = 'admin',
    password = 'admin',
    )

