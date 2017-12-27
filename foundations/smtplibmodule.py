# This Python file uses the following encoding: utf-8

import smtplib
import string

HOST = "smtp.163.com"
SUBJECT = "Test email from python"
TO = "564354487@qq.com"
FROM = "xyf2424094@163.com"
text = "Python rules them all"
BODY = string.join((
    "From: %s" % FROM,
    "To: %s" % TO,
    "Subject: %s" % SUBJECT,
    "",
    text
),"\r\n")

server = smtplib.SMTP()
server.connect(HOST,"25")
#server.starttls()
server.login("xyf2424094@163.com","xyf5202520")
server.sendmail(FROM, TO, BODY)
server.quit()


