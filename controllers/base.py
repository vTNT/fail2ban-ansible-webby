#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2013-09-01 22:21:54
# @Author  : Your Name (you@example.org)
# @Link    : http://example.org
# @Version : $Id$

import web

def logged():
    if web.ctx.session.logined != 0:
        return True
    else:
        return False
