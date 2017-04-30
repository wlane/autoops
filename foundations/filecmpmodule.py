# This Python file uses the following encoding: utf-8
# 通过调用cmp()比较单文件的差异
# 通过调用cmpfiles()比较目录中指定文件的清单对比
# 通过调用dircmp()实现目录差异对比功能，同时输出目录对比对象所有属性信息

import filecmp

a="E:\/test\/dir1"
b="E:\/test\/dir2"

print filecmp.cmp("E:\/test\/dir1\/f1.txt","E:\/test\/dir2\/f1.txt")    #默认比较文件内容???实际操作和书上不同

print filecmp.cmpfiles(a,b,['f1.txt','f2.txt','f3.txt','f4.txt','f5.txt'])
print "\n"
dirobj=filecmp.dircmp(a,b,['test.py'])  #目录比较，忽略文件test.py
dirobj.report()
print "\n"
dirobj.report_partial_closure()
print "\n"
dirobj.report_full_closure()
print "\n"
print "left_list:"+ str(dirobj.left_list)
print "right_list:"+ str(dirobj.right_list)
print "common:"+ str(dirobj.common)
print "left_only:"+ str(dirobj.left_only)
print "right_only:"+ str(dirobj.right_only)
print "common_dirs:"+ str(dirobj.common_dirs)
print "common_files:"+ str(dirobj.common_files)
print "common_funny:"+ str(dirobj.common_funny)
print "same_file:"+ str(dirobj.same_files)
print "diff_files:"+ str(dirobj.diff_files)
print "funny_files:"+ str(dirobj.funny_files)
