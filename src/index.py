#-*- coding:utf-8 -*-
import os
import sys
from urllib import request
import re
import threading

def download_pic(pathinfo, filename):
    url = pathinfo[0] + '://' + pathinfo[1] + '.' + pathinfo[2]
    print(url)
    try:
        request.urlretrieve(url,filename)
    except:
        print(url+'下载失败！')
    return None

def multiDownload(urlList):
    print("共有%d个图片文件需要下载"%len(urlList))
    task_threads = []

    for pathinfo in urlList:
        path = sys.path[0]
        dir = path + "/../assets/img/" + pathinfo[2]
        if not os.path.exists(dir):
            os.mkdir(dir)
        name = pathinfo[1][pathinfo[1].rindex('/') + 1:] + '.' + pathinfo[2]
        file = dir + '/' + name
        t_down = threading.Thread(target=download_pic,args=(pathinfo,file))
        task_threads.append(t_down)

    for task in task_threads:
        task.start()
    for task in task_threads:
        task.join()
    return None

def main():
    response = request.urlopen('http://www.baidu.com')
    content = response.read().decode('utf-8')
    pattern = r"(http|https)://(\S+?)\.(png|jpg|gif|bmp|jpeg)"
    result = re.findall(pattern, content, re.M | re.S)
    multiDownload(result)
    return None
main()