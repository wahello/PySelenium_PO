# -*- coding: utf-8 -*-
__author__ = 'Ray'
#Date :  2016-04-13
#mail： tsbc@vip.qq.com

import smtplib
from email.mime.text import MIMEText
import random, time

string = 'AaBbCcDdEeFfGgHhIiJjKkLlMmNnOoPpQqRrSsTtUuVvWwXxYyZz0123456789'
#mailto_list = ['jumptest123456@sina.com', 'jumptestjump@sogou.com', 'jumptest@eyou.com', 'jump123456@aliyun.com', 'yangqing.201219@yahoo.cn', 'admin@bj11.link263.com', 'jumptest@sohu.com', 'jumptest123456@hotmail.com', 'yangqing201219@tom.com', 'jumptest123456@126.com', 'shaoleiking@21cn.com']
'''
发送文本邮件！
'''
mailto_list = ['jumptest123456@sina.com','jumptestjump@163.com']
mail_host = "smtp.sohu.com"  #设置服务器
mail_user = "jumptest"    #用户名
mail_pass = "Admin123456"   #口令
mail_postfix = "sohu.com"  #发件箱的后缀

def send_mail(to_list, sub, content):
    me="Chenjp"+"<"+mail_user+"@"+mail_postfix+">"
    msg = MIMEText(content, _subtype='plain', _charset='gb2312')
    msg['Subject'] = sub
    msg['From'] = me
    msg['To'] = ";".join(to_list)
    try:
        server = smtplib.SMTP()
        server.connect(mail_host)
        server.login(mail_user, mail_pass)
        server.sendmail(me, to_list, msg.as_string())
        server.close()
        return True
    except Exception, e:
        print str(e)
        return False
if __name__ == '__main__':
    for i in xrange(1,2):
        time.sleep(1)
        if send_mail(mailto_list, "Python_mail_Ray_" + str(random.random()), "Hi!_Python_Mail!"):
            print u"发送成功，邮件ID:" + str(i)
        else:
            print u"发送失败，邮件ID:" + str(i)
