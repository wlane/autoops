# This Python file uses the following encoding: utf-8
#根据ip或者子网返回网络信息
from IPy import IP

ip_s = raw_input('please input an IP or net-range: ')
ips = IP(ip_s)
if len(ips) > 1:
    print ('net: %s' % ips.net())   #输出网络地址
    print ('netmask: %s' % ips.netmask())   #输出子网掩码
    print ('broadcast: %s' % ips.broadcast())   #输出广播地址
    print ('reverse address: %s' % ips.reverseNames()[0])   #输出反向解析地址（结果数组中的第一个值）
    print ('subnet: %s' % len(ips))     #输出子网数
else:
    print ('reverse address: %s' % ips.reverseNames()[0])

print ('hexadecimal: %s' % ips.strHex())
print ('binary ip: %s' % ips.strBin())
print ('iptype: %s' % ips.iptype())
