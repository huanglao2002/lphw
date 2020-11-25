#阅读代码1 网络下载文件

#映入系统模块/函数
import os
import urllib
 
#打印提示 
print("downloading with urllib")

#设置变量，即为url前半部分。
url0 = "http://bcmi.sjtu.edu.cn/log/files/lecture_notes/ml_2014_spring_ieee/"
#设置for循环，输出item1-14.
for item in range(1, 15):
    #定义文件名称，其中数值有str函数转化为字符串。
    file = "lecture" + str(item) + ".pdf"
    #url名称由url10 和file名称拼接而成。
    url = url0 + file
    #打印提示信息，下载某个文件。
    print("downloading with " + file)
    # join(path, *paths)
    # Join two (or more) paths.
    LocalPath = os.path.join('C:/Users/goatbishop/Desktop',file)
    #os.path.join将多个路径组合后返回
    urllib.request.urlretrieve(url,LocalPath)
    #第一个参数url:需要下载的网络资源的URL地址
    #第二个参数LocalPath:文件下载到本地后的路径


#python标准库 https://docs.python.org/3/library/index.html
#主要包含如下部分
#3 内建69个function，不需要import https://docs.python.org/3/library/functions.html
#4 内建Built-in Constants False,True,None,NotImplemented,Ellipsis,__debug__,site module
#5 内建type
#6 内建exception
#7 内建处理工具
#8 内建数据类型例如 datatime,calendar,coolections,collections.abc,heaqq,binsect,arrary,weakref,type,copy,pprint,reprlib,enum
#9 数字
#10 功能程序模块 itertiools,functools,operator
#11 文件和目录访问
#12 数据持久化
#13 数据压缩和归档 
#14 文件格式化  csv,configparser,nettrc,xdrlib,plistlib
#15 加密 hashlib,hmac,secrets
#16 操作系统服务
#17 并行执行 threading,multiprocessing等
#18 contextvars
#19 网络通讯
#20 互联网数据处理 email,json,mailcap,mailbox,mimetypes,base64,binhex,binascii,quorpri,uu
#21 结构标记处理工具 html,html.parser,haml.entities,xml
#22 互联网协议和支持 cgi,urllib,http,ftplib,poplib,.....
#23 多媒体  audioop,aifc,sumau,wavw,chunk,colrsys,imghdr,sndhdr,ossaudiodev
#24 国际化 gettext,locale
#25 程序框架 turtle,cmd,shlex
#26 图形化 tkinter,IDLE
#27 开发工具  typing,pydoc,doctest,unittest,test,test.support
#28 debugging and profiling  bdb,faulthandler,pdb
#29 软件打包和分发 distutils
#30 python运行服务  sys,sysconfig,builtins,__mail__,warings,
#31 客户定制化运行解释程序
#32 导入模块 zipimport,pkgutil,modulefinder,runpy,importlib
#33 python语言服务  parser,ast,systable,symbol,token,keyword,tokenize,tabnanny,pyclbr,py_compile
#34 杂项服务  formatter
#35 windows 专属服务 msislib,msvcrt,winreg,winsound
#36 unix 专属服务 posix,pwd,spwd,grp,crypt,termios,tty,pty,fcntl,pipes,resource,nis,syslog
#37 superseded modules optparse,imp
#38 无文档的模块 

