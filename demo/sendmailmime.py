# -*- coding: utf-8 -*-
__author__ = 'Ray'
#Date :  2016-05-25
#mail : tsbc@vip.qq.com

import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.application import MIMEApplication
import random, time

string = 'AaBbCcDdEeFfGgHhIiJjKkLlMmNnOoPpQqRrSsTtUuVvWwXxYyZz0123456789'
#mailto_list = ['jumptest123456@sina.com', 'jumptestjump@sogou.com', 'jumptest@eyou.com', 'jump123456@aliyun.com', 'yangqing.201219@yahoo.cn', 'admin@bj11.link263.com', 'jumptest@sohu.com', 'jumptest123456@hotmail.com', 'yangqing201219@tom.com', 'jumptest123456@126.com', 'shaoleiking@21cn.com']


"""

带不同类型附件和内容发送邮件！

"""

mailto_list = ['jumptest123456@sina.com','jumptestjump@163.com']
mail_host = "smtp.sohu.com"  #设置服务器
mail_user = "jumptest"    #用户名
mail_pass = "Admin123456"   #口令
mail_postfix = "sohu.com"  #发件箱的后缀

def send_mail(to_list, sub):
    me="Chenjp"+"<"+mail_user+"@"+mail_postfix+">"
    #如名字所示Multipart就是分多个部分
    msg = MIMEMultipart()
    msg['Subject'] = sub
    msg['From'] = me
    msg['To'] = ";".join(to_list)

    #---这是文字部分---
    part = MIMEText("好好学习，天天向上！", _subtype='plain', _charset='utf-8')
    msg.attach(part)

    #---这是附件部分---
    #xlsx类型附件
    part = MIMEApplication(open('foo.xlsx','rb').read())
    part.add_header('Content-Disposition', 'attachment', filename="foo.xlsx")
    msg.attach(part)

    #txt类型附件
    part = MIMEApplication(open('foo.txt','rb').read())
    part.add_header('Content-Disposition', 'attachment', filename="foo.txt")
    msg.attach(part)

    #pdf类型附件
    part = MIMEApplication(open('foo.pdf','rb').read())
    part.add_header('Content-Disposition', 'attachment', filename="foo.pdf")
    msg.attach(part)

    #doc类型附件
    part = MIMEApplication(open('foo.doc','rb').read())
    part.add_header('Content-Disposition', 'attachment', filename="foo.doc")
    msg.attach(part)

    
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
    for i in xrange(1):
        time.sleep(1)
        if send_mail(mailto_list, "Python_mail_Ray_" + str(random.random())):
            print u"发送成功，邮件ID:" + str(i)
        else:
            print u"发送失败，邮件ID:" + str(i)
