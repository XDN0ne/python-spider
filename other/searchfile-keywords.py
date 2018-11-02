#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/11/02
# @Author  : XDN01
# @Site    : www.raosong.cc
# @File    : searchfile-keywords.py
import os

def word_file(file_list, query_word): 
    for _file in file_list:
        if query_word in open(_file).read():
            print _file
    print("Finish searching.")
    
def get_all_file(floder_path):
    file_list = []
    if floder_path is None:
        raise Exception("floder_path is None")
    for dirpath, dirnames, filenames in os.walk(floder_path):
        for name in filenames:
            file_list.append(dirpath + '/' + name)
    return file_list

query_word = raw_input("Please input the key word that you want to search:")
basedir = raw_input("Please input the directory:")

word_file(get_all_file(basedir), query_word)
raw_input("Press Enter to quit.")
