#!/usr/bin/env python
#-*-coding:utf-8-*-

import requests
import random
import sys

url_chat = 'http://www.simsimi.com/func/req?msg=%s&lc=ch'
h_accept = "application/json, text/javascript, */*; q=0.01" 
h_xrw =  "XMLHttpRequest" 
h_ua = "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/27.0.1453.116 Safari/537.36"
h_cookie = "sagree=true; selected_nc=ch; JSESSIONID=C2BD358F72447923A47338265045B62D; AWSELB=15E16D030EBAAAB8ACF4BD9BB7E0CA8FB501388662640BCEC6E9C54E70B150AA8514D30E844A0F6781F3C00BEC43069730243F418119D4A1660F073D105DD873991975B881; __utma=119922954.1581747215.1382876735.1382876756.1382964833.3; __utmb=119922954.2.10.1382964833; __utmc=119922954; __utmz=119922954.1382876735.1.1.utmcsr=(direct)|utmccn=(direct)|utmcmd=(none)" 
h_referer = "http://www.simsimi.com/talk.htm" 

class Bot:

    def __init__(self):
        self.session = requests.Session()
        self.init_session()

    def init_session(self):
        self.session.headers.update({'User-Agent': h_ua})
        self.session.get('http://www.simsimi.com/talk.htm')
        self.session.headers.update({'Referer': h_referer})
        self.session.headers.update({'Accept': h_accept})
        self.session.headers.update({'X-Requested-With': h_xrw})
        self.session.headers.update({'Cookie': h_cookie})

    def chat(self, message='hello'):
	try:
	    res = self.session.get(url_chat % message)
	    answer = res.json()['response'].encode('utf-8')
	    if answer == 'SimSimi is tired, I only can speak 200 time a day. Please visit again tomorrow. See ya~ ':
		return random.choice(['hehe', '。。。', '-_-!', '=。='])
	    return answer
	except Exception, e:
	    return random.choice(['|hehe', '|。。。', '|-_-!', '|=。='])
	
        
bot = Bot()
if len(sys.argv) >1:
    print bot.chat(" ".join(sys.argv[1:]))
else:
    print bot.chat("我什么也不想说")+" (eg: !chat 钓鱼岛是中国的)"
