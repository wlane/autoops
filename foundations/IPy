# This Python file uses the following encoding: utf-8
from IPy import IP

print IP('10.0.0.0/8').version()    #ip类型
print IP('::1').version()

ip = IP('192.168.0.0/30')   #列出网段内的ip清单
print ip.len()
for x in ip:
    print x

ip = IP('192.168.1.20')
print ip.reverseNames()     #反向解析
print ip.iptype()   #判断ip是私网还是公网
print IP('8.8.8.8').iptype()
print IP('8.8.8.8').int()
print IP('8.8.8.8').strHex()
print IP('8.8.8.8').strBin()
print IP(0x8080808)
print IP('192.168.1.0').make_net('255.255.255.0')   #根据ip和掩码产生网段格式
print IP('192.168.1.0/255.255.255.0', make_net=True)
print IP('192.168.1.0-192.168.1.255', make_net=True)
print IP('192.168.1.0/24').strNormal(0)     #根据不同类型的参数值输出不同类型的网段
print IP('192.168.1.0/24').strNormal(1)
print IP('192.168.1.0/24').strNormal(2)
print IP('192.168.1.0/24').strNormal(3)

print IP('10.0.0.0/24') < IP('12.0.0.0/24')     #ip大小比较
print '192.168.1.100' in IP('192.168.1.0/24')   #ip地址和网段是否包含于另一个网段中
print IP('192.168.1.0/24') in IP('192.168.0.0/16')
print IP('192.168.0.0/23').overlaps('192.168.1.0/24')   #判断网段是否有重叠的部分（分前后关系）
print IP('192.168.1.0/24').overlaps('192.168.0.0/23')
print IP('192.168.1.0/24').overlaps('192.168.2.0')





