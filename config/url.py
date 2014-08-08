#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2013-07-30 14:25:45
# @Author  : Your Name (you@example.org)
# @Link    : http://example.org
# @Version : $Id$

pre_fix = 'controllers.'

urls = (
    '/main',                         pre_fix + 'todo.Index',   
    '/page/(\d+)/(\w+)',            pre_fix + 'todo.Index',   
    '/todo/new',              pre_fix + 'todo.New', 
    '/todo/(\d+)/edit',      pre_fix + 'todo.Edit',  
    '/todo/(\d+)/delete',   pre_fix + 'todo.Delete',
    '/todo/search',          pre_fix + 'todo.Search',
    '/$',                   pre_fix + 'todo.Login',
    '/logout',              pre_fix + 'todo.Logout',  
    '/ansible/(\w+)',      pre_fix + 'todo.Ansible',
    )
