# -*- coding:utf-8 -*-
__author__ = 'Ray'

import threading
import time
import xmpp
"""
xmpp download http://pan.baidu.com/s/1ntvI445
"""
class chat(threading.Thread):
	def __init__(self,fuser,password,tuser):
		threading.Thread.__init__(self)
		self.fuser = fuser
		self.passwd = password
		self.tuser = tuser
		self.thread_stop = False

	def run(self):
		while not self.thread_stop:
			now = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time()))
			msg = "This is Test. I'M " + self.fuser + '\n' + " (From python msg)"  + now
			client = xmpp.Client('im.e-u.cn')
			client.connect(server = ('im.e-u.cn', 5223))
			client.auth(self.fuser, self.passwd, 'botty')
			client.sendInitPresence()
			message = xmpp.Message(self.tuser, msg, typ = 'chat')
			client.send(message)
	def stop(self):
		self.thread_stop = True

def test():
	thread1 = chat('ts_001','111111','admin@im.e-u.cn')
	thread2 = chat('ts_002','111111','admin@im.e-u.cn')
	thread3 = chat('ts_003','111111','admin@im.e-u.cn')
	thread4 = chat('ts_004','111111','admin@im.e-u.cn')
	thread5 = chat('ts_005','111111','admin@im.e-u.cn')
	thread6 = chat('ts_006','111111','admin@im.e-u.cn')
	thread7 = chat('ts_007','111111','admin@im.e-u.cn')
	thread8 = chat('ts_008','111111','admin@im.e-u.cn')
	thread9 = chat('ts_009','111111','admin@im.e-u.cn')
	thread10 = chat('ts_010','111111','admin@im.e-u.cn')

	thread1.start()
	thread2.start()
	thread3.start()
	thread4.start()
	thread5.start()
	thread6.start()
	thread7.start()
	thread8.start()
	thread9.start()
	thread10.start()

	time.sleep(20)

	thread1.stop()
	thread2.stop()
	thread3.stop()
	thread4.stop()
	thread5.stop()
	thread6.stop()
	thread7.stop()
	thread8.stop()
	thread9.stop()
	thread10.stop()

	return

if __name__ == '__main__':
	test()