# This Python file uses the following encoding: utf-8
#DNS域名轮询监控
import dns.resolver
import os
import httplib

iplist = []
appdomain = "www.tvjoy.cn.ttt"
#appdomain = "baidu.com"

def get_iplist(domain=""):
    try:
        A = dns.resolver.query(domain, 'A')
    except Exception,e:
        print "dns resolver error:"+str(e)
        return
    for i in A.response.answer:
        for j in i.items:
            iplist.append(j.address)
    return True

def checkip(ip):
    checkurl=ip+":80"
    getcontent=""
    httplib.socket.setdefaulttimeout(5) #定义http链接超时时间
    conn=httplib.HTTPConnection(checkurl)   #创建http链接对象
    try:
        conn.request("GET", "/", headers = {"Host": appdomain})     #发起url请求，添加host主机头
        r=conn.getresponse()
        getcontent = r.read(15)
        #getcontent = r.read(6)   #获取页面的前6个字符做校验
    finally:
        if getcontent=="<!DOCTYPE html>":
        #if getcontent == "<html>":
            print ip+" [ok]"
        else:
            print ip+" [ERROR]"
            #print getcontent

if __name__=="__main__":
    if get_iplist(appdomain) and len(iplist)>0:
        for ip in iplist:
            checkip(ip)
    else:
        print "dns resolver error"
