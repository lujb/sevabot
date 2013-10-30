#!/usr/bin/env python
#-*-coding:utf-8-*-

import urllib2
import re
import time
import random

key = time.strftime('%Y-%m-%d')


def random_joke():
    r = urllib2.urlopen('http://feed.feedsky.com/qiushi', timeout=60)
    p = r.read()
    r = re.findall('&lt;p&gt;([\s]+)([^\t]+)&lt;br/&gt;', p)
    if r:
	res, n = re.subn("&lt;br/&gt;", " ", random.choice(r)[1])
        return res
    else:
	return 'None'

print random_joke()
