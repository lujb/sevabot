#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
list all subscribers
"""
import sys
sys.path.append('/home/skype/webots')
import bbsbot

reload(sys)
sys.setdefaultencoding('utf-8')
bbsbot.init_db()

print 'Current subscribers:'
for sid, sname, bbsid in bbsbot.get_subscribers():
    print sid + " <--> " + bbsid


    
