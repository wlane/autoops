# This Python file uses the following encoding: utf-8
#比较两个文件内容的差异
import difflib
import sys

try:
    textfile1=sys.argv[1]
    textfile2=sys.argv[2]
except Exception,e:
    print "ERROR:"+str(e)
    print "Usage: python diff-simple.py filename1 filename2 > result.html"
    sys.exit()

def readfile(filename):
    try:
        fileHandle = open(filename, 'rb')
        text=fileHandle.read().splitlines()
        fileHandle.close()
        return text
    except IOError as error:
        print ('Read file Error:'+str(error))
        sys.exit()

if textfile1=="" or textfile2=="":
    print "Usage:python diff-simple.py filename1 filename2 > result.html"
    sys.exit()

text1_lines = readfile(textfile1)
text2_lines = readfile(textfile2)

d = difflib.HtmlDiff()
print d.make_file(text1_lines, text2_lines) #HTML格式的输出结果


