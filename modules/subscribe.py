#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
subscribe bbs notification
"""
import os, sys

reload(sys)
sys.setdefaultencoding('utf-8')
sys.path.append('/home/skype/webots')
import bbsbot

username = unicode(os.environ["SKYPE_USERNAME"], 'utf-8')
fullname = unicode(os.environ["SKYPE_FULLNAME"], 'utf-8')

def u(string):
    unicode(string, 'utf-8')

if len(sys.argv) == 2:
    bbsid = unicode(sys.argv[1], 'utf-8')
    ret = bbsbot.insert_subscriber(username, fullname, bbsid)
    if ret == 0:
	print u'订阅成功!'
    elif ret == 1:
	print u'你已经订阅了--'
    elif ret == 2:
	print u'成功修改订阅信息!'
    else:
	print u'神秘的未知错误!'
else:
    print u'参数错误! (eg: !subscribe BBS_ID)'
