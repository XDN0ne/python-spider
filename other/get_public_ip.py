#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/02/25
# @Author  : XDN01
# @Site    : www.raosong.cc
# @File    : get_public_ip.py
import socket
import csv
import requests
import threading
import queue

q = queue.Queue()
threading_num = 50


with open("alldomain.txt" , "r") as f:
    filedata = f.readlines()
    q.put(filedata)
    f.close()

def run():
    while not q.empty():
        filedata = q.get()
        for i in filedata:
            url = str(i).replace("\n",'')
            #print(url)
            try:
                myaddr = socket.getaddrinfo(url, 'http')
                #print(str(myaddr[0][4][0])[:3])
                if str(myaddr[0][4][0])[:3] != str(172):
                    #print(url+" "+str(myaddr[0][4][0]))
                    #value_array.append(url).append(str(myaddr[0][4][0]))
                    with open("public_domain.csv","a") as fw:
                        writer = csv.writer(fw)
                        writer.writerow([url,str(myaddr[0][4][0])])
            except:
                #print('can't open')
                pass
        #f.close()

if __name__ =="__main__":
    print('begin')
    for i in range(threading_num):
        t = threading.Thread(target=run)
        t.start()
        t.join()
    print('over')
