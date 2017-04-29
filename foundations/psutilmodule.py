# This Python file uses the following encoding: utf-8
import psutil, datetime
from subprocess import PIPE

print(psutil.cpu_times())  # 显示cpu完整信息
print(psutil.cpu_times(percpu=True))  #分别显示每个cpu核心的信息
print(psutil.cpu_times().user)   #显示用户user的cpu时间比
print(psutil.cpu_count())  #显示cpu的逻辑个数
print(psutil.cpu_count(logical=False))  #显示cpu的物理个数

mem = psutil.virtual_memory() #获取内存完整信息
print mem
print mem.total     #获取内存总数
print mem.free      #获取空闲内存数
print psutil.swap_memory()      #获取swap分区信息

print psutil.disk_partitions()  #获取磁盘完整信息
print psutil.disk_usage('c:\\')   #获取分区使用情况
print psutil.disk_io_counters()     #获取磁盘总的io数，读写信息
print psutil.disk_io_counters(perdisk=True)     #获取单个磁盘分区的io数，读写信息

print psutil.net_io_counters()  #获取网络总的io
print psutil.net_io_counters(pernic=True)   #获取每个网络的io

print psutil.users()    #当前用户的登陆信息
print psutil.boot_time()    #获取已linux时间戳格式返回的开机时间
print datetime.datetime.fromtimestamp(psutil.boot_time()).strftime("%Y-%m-%d %H:%M:%S")     #转换成自然时间格式

print psutil.pids()     #列出所有进程的id
p = psutil.Process(1800)
print p.name()
#print p.exe()
#print p.cwd()
print p.status()
print p.create_time()
#print p.uids
#print p.gids()
print p.cpu_times()
#print p.cpu_affinity()
print p.memory_percent()
print p.io_counters()
print p.connections()
print p.num_threads()

p = psutil.Popen(["D:\Python27\python.exe", "-c", "print('hello')"], stdout=PIPE)  #跟踪程序运行的相关信息
print p.name()
print p.username()
print p.connections()
print p.cpu_times()     #得到进程运行的cpu时间






