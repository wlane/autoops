# This Python file uses the following encoding: utf-8

import dns.resolver

domaina =  raw_input('please input an domain: ')    #最好使用一级域名，如baidu.com,使用二级域名就会报错，但是www.tvjoy.cn这种二级域名正常，可能和cname记录有关
A = dns.resolver.query(domaina, 'A') #获取A记录
print A.response
print '\n'
print A.response.answer[0]
print '\n'
print A.response.answer
print '\n'
for i in A.response.answer:
    print i.items
    for j in i.items:
        print j.address

domainb = raw_input('please input an domain: ') #使用二级域名，如www.baidu.com
cname = dns.resolver.query(domainb, 'CNAME') #获取cname记录
for i_c in cname.response.answer:
    for j_c in i_c.items:
        print j_c.to_text()

