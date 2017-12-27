# This Python file uses the following encoding: utf-8

import difflib

text1 = """text1:
This module provides classes and functions for comparing sequences.
"""
text1_lines = text1.splitlines()    #以行分割
print text1_lines
text2 = """text2:
This module provides classes and functions for comparing sequences.
"""
text2_lines = text2.splitlines()
d = difflib.Differ()    #创建differ对象
diff = d.compare(text1_lines, text2_lines)  #对字符串进行比较
print '\n'.join(list(diff))

dh = difflib.HtmlDiff() #输出html格式文档，可以使用浏览器打开
print dh.make_file(text1_lines, text2_lines)

