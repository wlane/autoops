#!/usr/bin/python
# -*- coding:utf-8 -*-

import xlsxwriter

workbook = xlsxwriter.Workbook('chart.xlsx')
worksheet = workbook.add_worksheet()
chart = workbook.add_chart({'type':'column'})

title = [u'业务流量',u'星期一',u'星期二',u'星期三',u'星期四',u'星期五',u'星期六',u'星期日',u'平均流量']
buname = [u'业务官网',u'新闻中心',u'购物频道',u'体育频道',u'亲子频道']
data = [[150,152,158,149,155,145,148],[89,88,95,93,99,87,90],[200,201,199,195,204,210,187],[71,75,78,77,75,79,80],[88,85,86,84,82,89,81]]

format=workbook.add_format()
format.set_border(1)

format_title=workbook.add_format()
format_title.set_border(1)
format_title.set_bg_color('#cccccc')
format_title.set_align('center')
format_title.set_bold()

format_avg=workbook.add_format()
format_avg.set_border(1)
format_avg.set_num_format('0.00')

worksheet.write_row('A1',title,format_title)
worksheet.write_column('A2',buname,format)
worksheet.write_row('B2',data[0],format)
worksheet.write_row('B3',data[1],format)
worksheet.write_row('B4',data[2],format)
worksheet.write_row('B5',data[3],format)
worksheet.write_row('B6',data[4],format)

def chart_series(cur_row):
    worksheet.write_formula('I'+cur_row,'=AVERAGE(B'+cur_row+':H'+cur_row+')',format_avg)
    chart.add_series({
        'categories':'=Sheet1!$B$1:$H$1',
        'values':'=Sheet1!$B$'+cur_row+':$H$'+cur_row,
        'line':{'color':'black'},
        'name':'=Sheet1!$A$'+cur_row,
    })

for row in range(2,7):
    chart_series(str(row))

chart.set_size({'width':577,'height':287})
chart.set_title({'name':u'业务流量周报图表'})
chart.set_y_axis({'name':'Mb/s'})

worksheet.insert_chart('A8',chart)
workbook.close()
