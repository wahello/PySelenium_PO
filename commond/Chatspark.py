# -*- coding:utf-8 -*-
__author__ = 'Ray'

import xmpp
import time
"""
xmpp download http://pan.baidu.com/s/1ntvI445
"""

to = ['admin@im.e-u.cn']
fname = {'ts_001':'111111','ts_002':'111111',
		 'ts_003':'111111','ts_004':'111111',
		 'ts_005':'111111','ts_006':'111111',
		 'ts_007':'111111','ts_008':'111111',
		 'ts_009':'111111','ts_010':'111111'}
#to = ['chenjiangpeng@xtpt.e-u.cn','zhangyy@xtpt.e-u.cn','liujiao@xtpt.e-u.cn']

def to_msg(username,password):
	msg = "This is Test. I'M " + username + " (from python msg)"
	client = xmpp.Client('im.e-u.cn')
	client.connect(server = ('im.e-u.cn', 5223))
	client.auth(username, password, 'botty')

	client.sendInitPresence()
	message = xmpp.Message(to, msg, typ = 'chat')
	client.send(message)
	time.sleep(0.2)
	for i in to:
		#print i
		client.sendInitPresence()
		message = xmpp.Message(i, msg, typ = 'chat')
		client.send(message)
		time.sleep(0.2)
	#print msg

def too_msg(username,password):
	msg = "This is Test. I'M " + username + " (from python msg)"
	client = xmpp.Client('im.e-u.cn')
	client.connect(server = ('im.e-u.cn', 5223))
	client.auth(username, password, 'botty')

	# client.sendInitPresence()
	# message = xmpp.Message(to, msg, typ = 'chat')
	# client.send(message)
	# time.sleep(0.2)
	for i in to:
		#print i
		client.sendInitPresence()
		message = xmpp.Message(i, msg, typ = 'chat')
		client.send(message)
		time.sleep(0.2)

if __name__=='__main__':
	to_msg('ts_001','111111')
	to_msg('ts_002','111111')