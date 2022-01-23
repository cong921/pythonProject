import time

import requests
from lxml import etree
import smtplib
import smtplib
from email.mime.text import MIMEText
from email.header import Header

def sendMail():
    sender = 'mailttest@163.com'
    receivers = ['710805546@qq.com']  # 接收邮件，可设置为你的QQ邮箱或者其他邮箱

    # 三个参数：第一个为文本内容，第二个 plain 设置文本格式，第三个 utf-8 设置编码
    message = MIMEText('Python 邮件发送测试...', 'plain', 'utf-8')
    message['From'] = Header("菜鸟教程", 'utf-8')  # 发送者
    message['To'] = Header("测试", 'utf-8')  # 接收者

    subject = 'Python SMTP 邮件测试'
    message['Subject'] = Header(subject, 'utf-8')

    try:
        smtpObj = smtplib.SMTP_SSL('smtp.163.com',465)
        smtpObj.login(sender, 'mailtest1')
        smtpObj.sendmail(sender, receivers, message)

        print
        "邮件发送成功"
    except smtplib.SMTPException:
        print
        "Error: 无法发送邮件"

r=requests.get("https://www.gdmede.com.cn/").text
print(r)
html = etree.HTML(r)
t=html.xpath('/html/body/div[1]/div/div/div[1]/div/div/div[2]/div[1]/div[2]/a[1]/div[3]/text()')
t=str(t)
newitem=t[2:6]+t[7:9]+t[10:12]
nowtime=time.strftime('%Y%m%d',time.localtime())

# if(newitem==b):
#
sendMail()