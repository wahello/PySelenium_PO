# -*- coding: utf-8 -*-
__author__ = 'Ray'

"""
Python syslog 发包工具.
mail：tsbc@vip.qq.com
2016-05-05
"""

import socket
import threading
import ConfigParser
import random
import randomip
import weighted_choice
import time
import sys
reload(sys)
sys.setdefaultencoding('utf-8')

class send(threading.Thread):

	def __init__(self, message, host, port):
		threading.Thread.__init__(self)
		self.thread_stop = False
		self.message = message
		self.host = host
		self.port = port
		self.FACILITY = {
			'kern': 0, 'user': 1, 'mail': 2, 'daemon': 3,
			'auth': 4, 'syslog': 5, 'lpr': 6, 'news': 7,
			'uucp': 8, 'cron': 9, 'authpriv': 10, 'ftp': 11,
			'local0': 16, 'local1': 17, 'local2': 18, 'local3': 19,
			'local4': 20, 'local5': 21, 'local6': 22, 'local7': 23,
		}

		self.LEVEL = {
			'emerg': 0, 'alert':1, 'crit': 2, 'err': 3,
			'warning': 4, 'notice': 5, 'info': 6, 'debug': 7
		}
		weights = [0.03, 0.04, 0.05, 0.07, 0.1, 0.2, 0.5, 0.01] #随机产生日志级别的概率

		if 'success' in self.message:
			self.levl = self.LEVEL['info']
		elif 'failed' in self.message:
			self.levl = self.LEVEL['warning']
		elif 'permit' in self.message:
			self.levl = self.LEVEL['info']
		elif 'deny' in self.message:
			self.levl = self.LEVEL['warning']
		else:
			self.levl = weighted_choice.weighted_choice_sub(weights)
			# self.levl = random.choice(self.LEVEL.keys())
	def run(self):

		"""
		Send syslog UDP packet to given host and port.
		"""
		sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
		data = '<%d>%s' % (self.levl + self.FACILITY['local7']*8, self.message)
		print data
		sock.sendto(data, (self.host, self.port))
		sock.close()

	def stop(self):
		self.thread_stop = True

def test():

	#从配置文件读取数据
	cf = ConfigParser.ConfigParser()
	cf.read('send.config')
	host = cf.get('receiver', 'host').split(',')#获取接收log服务主机
	port = int(cf.get('receiver', 'port'))
	sip  = randomip.__get_random_ip([cf.get('mesg', 'sip')])#随机生成源IP
	dip	 = randomip.__get_random_ip([cf.get('mesg', 'dip')])#随机生成目的IP
	sportstr = tuple(cf.get('mesg', 'sport').split(',')) #随机生成源端口
	sport = str(random.randint(int(sportstr[0]), int(sportstr[1])))
	dportstr = cf.get('mesg', 'dport').split(',')#随机生成目的端口
	dport = random.choice(dportstr)

	#获取系统当前时间
	now = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime())
	nowstr = time.strftime('%b %d %H:%M:%S', time.localtime())

	'''漏扫'''
	#操作日志
	nvaslog1 = ' '+now + ' ADMIN CONFIG user admin ip 10.0.1.48 module 系统-云中心配置 cmd "云中心配置。" result success'
	#管理员登录
	nvaslog2 = ' '+now + ' ADMIN LOGIN user tsbc ip 10.0.1.104 action login result failed'
	#漏洞发现
	nvaslog3 = ' '+now + ' SECURITY VUL host tsbc type 常规  mintype 轻蠕虫 id CN-CVE name 洪泛攻击 desc "容易受到ARP攻击"'

	threadnvas1 = send(nvaslog1, host[0], port)
	threadnvas2 = send(nvaslog2, host[0], port)
	threadnvas3 = send(nvaslog3, host[0], port)

	'''信息审计'''
	#内容审计
	bca1 = ' '+now + ' AUDIT CONTENT user admin usergroup 管理员组 access permit prot tcp sip ' + sip + ' sport ' + sport + ' dip ' + dip + ' dport 80 type HTTP url http://www.163.com filename "找工作.txt" keyword 找工作 cmd "找工作" subject 邮件主题 sender lietou@163.com receiver lietou@163.com'
	bca2 = ' '+now + ' AUDIT CONTENT user admin usergroup 管理员组 access deny prot tcp sip ' + sip + ' sport ' + sport + ' dip ' + dip + ' dport 80 type HTTP url http://mail.163.com filename "找工作.txt" keyword 找工作 cmd "找工作" subject 邮件主题 sender lietou@163.com receiver lietou@163.com'
	#应用行为审计
	bca3 = ' '+now + ' AUDIT APP user 10.0.1.48 usergroup NULL access permit prot "UDP" sip ' + sip + ' sport ' + sport + ' dip ' + dip + ' dport ' + dport + u' type "IM通信" behav "飞秋" desc "内置特征"'
	threadbca1 = send(bca1, host[0], port)
	threadbca2 = send(bca2, host[0], port)
	threadbca3 = send(bca3, host[0], port)

	'''上网行为'''
	#IP访问事件  --事件入库了但是界面没有对应的类别查询不到
	nca1 = ' '+now + ' SECURITY POLICY access permit prot http smac 00:22:46:0D:91:7C dmac 00:22:46:0D:91:7C sip ' + sip + ' sport ' + sport + ' dip ' + dip + ' dport ' + dport + ' times 1'
	#应用行为审计
	nca2 = ' '+now + ' AUDIT APP user tsbc usergroup 管理员组 access deny prot 代理上网 sip ' + sip + ' sport ' + sport + ' dip ' + dip + ' dport ' + dport + ' type GAME behav 访问网络游戏 desc "访问英雄联盟游戏"'
	#用户认证事件
	nca3 = ' '+now + ' USER AUTH name tsbc group 管理员组 ip ' + sip + ' type local result success'
	threadnca1 = send(nca1, host[0], port)
	threadnca2 = send(nca2, host[0], port)
	threadnca3 = send(nca3, host[0], port)

	'''IDS/IPS'''
	#设备流量日志
	idslog1 = ' '+now + ' SYSTEM TRAFFIC sendbps 10211 recvbps 10211 sendpps 19621 recvpps 18954'
	threadids1 = send(idslog1, host[0], port)


	'''Jump防火墙'''
	#安全监测/访问控制
	fwlog1 = ' '+now + ' SECURITY POLICY access permit prot TCP smac 00:22:46:1d:eb:b5 dmac 00:22:46:1f:aa:47 sip ' + sip + ' sport ' + sport + ' dip ' + dip + ' dport ' + dport + ' times 1'
	#攻击检测
	fwlog2 = ' '+now + ' SECURITY INSTRUCTION type ddos id '+str(random.randint(1000,9999))+' name "尝试攻击" smac 00:22:46:0D:91:7d  dmac 00:22:46:0D:91:7C prot ICMP sip ' + sip + ' sport ' + sport + ' dip ' + dip + ' dport ' + dport + ' times 1'
	#病毒日志
	fwlog3 = ' '+now + ' SECURITY VIRUS type 木马病毒 name "灰鸽子" smac 00:22:46:0A:B1:BC  dmac 00:22:46:0D:91:7C prot tcp sip ' + sip + ' sport ' + sport + ' dip ' + dip + ' dport ' + dport + ' filename "新建文本文档.exe"'
	#隧道日志
	fwlog4 = ' '+now + ' IPSEC TUNNEL id 1 localip ' + sip + ' remote ' + dip + ' desc "Error!!!"'
	# thread2 = send(msg.encode(encoding='gb2312'), host[0], 514)
	threadfw1 = send(fwlog1, host[0], port)
	threadfw2 = send(fwlog2, host[0], port)
	threadfw3 = send(fwlog3, host[0], port)
	threadfw4 = send(fwlog4, host[0], port)

	'''主机审计'''
	#移动介质审计
	hostlog1 = ' '+now + ' AUDIT MEDIUM operator admin action 接入 medtype U 盘 medname 小明的U盘 access "D:\Menu" times 50 result permit'
	threadhost1 = send(hostlog1, host[0], port)

	'''用户/系统'''
	#网口状态变化
	systemlog1 = ' '+now + ' SYSTEM INTERFACE eth '+str(random.randint(0, 10))+' type '+random.choice(['phy', 'link'])+' state '+random.choice(['up', 'down'])
	#用户登录
	systemlog2 = ' '+now + ' USER LOGIN user tsbc group 运维管理员组 ip '+ dip +' action '+random.choice(['login', 'logout'])+' result '+random.choice(['success', 'failed'])
	#用户认证
	systemlog3 = ' '+now + ' USER AUTH name tsbc group 运维管理员组 ip '+ dip +' type '+random.choice(['local', 'radius', 'tacacs', 'ldap', 'msad', 'pop3', 'cert', 'other'])+' result '+random.choice(['success', 'failed'])
	#用户访问资源
	systemlog4 = ' '+now + ' USER ACCESS name tsbc group 安全管理员组 restype web resname "信息审计系统" sip '+ sip +' dip '+ dip +' prot tcp sport '+ sport +' dport '+ dport +' result '+random.choice(['permit', 'deny'])
	#性能日志
	systemlog5 = ' '+now + ' SYSTEM PERFORMANCE cpu '+str(random.randint(80, 90))+' memory '+str(random.randint(75, 95))+' connections '+str(random.randint(80, 300))
	#系统关键进程
	systemlog6 = ' '+now + ' SYSTEM PROCESS explorer.exe exit'
	threadsystem1 = send(systemlog1, host[0], port)
	threadsystem2 = send(systemlog2, host[0], port)
	threadsystem3 = send(systemlog3, host[0], port)
	threadsystem4 = send(systemlog4, host[0], port)
	threadsystem5 = send(systemlog5, host[0], port)
	threadsystem6 = send(systemlog6, host[0], port)

	'''H3C交换机'''
	h3clog1 = nowstr + ' 2000 H3C %%10IFNET/3/LINK_UPDOWN(l): GigabitEthernet1/0/7 link status is UP.'
	h3clog2 = nowstr + ' 2000 H3C %%10SHELL/4/LOGOUT(t):   Trap 1.3.6.1.4.1.25506.2.2.1.1.3.0.2<hh3cLogOut>: logout from VTY'
	threadh3c1 = send(h3clog1, host[0], port)
	threadh3c2 = send(h3clog2, host[0], port)

	'''Cisco路由器'''
	#管理员操作
	csicolog1 = '29: *'+nowstr+'.'+ str(random.randint(001, 999)) +': %SYS-5-CONFIG_I: Configured from console by admin on vty0 (10.0.1.49)'
	threadcisco1 = send(csicolog1, host[0], port)

	# threadnvas1.start()
	# threadnvas2.start()
	# threadnvas3.start()
	# threadbca1.start()
	# threadbca2.start()
	# threadbca3.start()
	# threadnca1.start()
	# threadnca2.start()
	# threadnca3.start()
	# threadids1.start()
	# threadfw1.start()
	# threadfw2.start()
	# threadfw3.start()
	# threadfw4.start()
	# threadhost1.start()
	# threadsystem1.start()
	# threadsystem2.start()
	# threadsystem3.start()
	# threadsystem4.start()
	# threadsystem5.start()
	# threadsystem6.start()
	# threadh3c1.start()
	threadh3c2.start()
	threadcisco1.start()

	# threadnvas1.stop()
	# threadnvas2.stop()
	# threadnvas3.stop()
	# threadbca1.stop()
	# threadbca2.stop()
	# threadbca3.stop()
	# threadnca1.stop()
	# threadnca2.stop()
	# threadnca3.stop()
	# threadids1.stop()
	# threadfw1.stop()
	# threadfw2.stop()
	# threadfw3.stop()
	# threadfw4.stop()
	# threadhost1.stop()
	# threadsystem1.stop()
	# threadsystem2.stop()
	# threadsystem3.stop()
	# threadsystem4.stop()
	# threadsystem5.stop()
	# threadsystem6.stop()
	# threadh3c1.stop()
	threadh3c2.stop()
	threadcisco1.stop()

if __name__ == '__main__':
	for i in xrange(1):
		# print i
		test()