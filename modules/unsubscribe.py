#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
unsubscribe bbs notification
"""
import os, sys

reload(sys)
sys.setdefaultencoding('utf-8')
sys.path.append('/home/skype/webots')
import bbsbot

username = unicode(os.environ["SKYPE_USERNAME"], 'utf-8')

bbsbot.delete_subscriber(username)
print '取消订阅成功!'
