# -*- coding:utf-8 -*-
# from Tkinter import *
# root = Tk()
# root.mainloop()

# import time
#
# SECONDS_PER_DAY = 24 * 60 * 60
#
# def doFunc():
#     print "do Function..."
#
# def doFirst():
#     from datetime import datetime, timedelta
#     curTime = datetime.now()
#     desTime = curTime.replace(hour=2, minute=0, second=0, microsecond=0)
#     delta = curTime - desTime
#     skipSeconds = SECONDS_PER_DAY - delta.total_seconds()
#     print "Must sleep %d seconds" % skipSeconds
#     return skipSeconds
#
# print doFirst()

# !/usr/bin/env python3
# coding: utf-8
import smtplib
from email.mime.text import MIMEText
from email.header import Header

sender = 'ranw1120@gmail.com'
receiver = 'wrr_1120@163.com'
subject = 'python email test'
smtpserver = 'smtp.gmail.com'
username = 'ranw1120@gmail.com'
password = '50421_01016'

msg = MIMEText('你好', 'text', 'utf-8')  # 中文需参数‘utf-8’，单字节字符不需要
msg['Subject'] = Header(subject, 'utf-8')

smtp = smtplib.SMTP()
smtp.connect('smtp.gmail.com')
smtp.login(username, password)
smtp.sendmail(sender, receiver, msg.as_string())
smtp.quit()