#encoding:utf-8

#author:yezhiye
#github: https://github.com/yezhiye/python

import datetime
import os

def danci(file="words.txt"):
    #file为本地词库，默认为words.txt
    words = []
    tab = "    " #间隔单词与时间，默认为四个空格
    def save(word,file):
        with open(file,'a+') as f:
            f.write(tab.join((word,str(datetime.date.today())))+"\n")
    def init(file):
        if os.path.exists(file):
            with open(file,'r') as f:
                temp = f.readlines()
                #切割，读入每行单词
                for i in temp:
                    words.append(i.split(tab)[0])    
    def add():
        init(file)
        while 1:
            word = input("请输入你要记录的单词（直接按回车退出程序）：")
            if word == "":
                break
            elif word in words:
                print("单词已存在")
            else:
                words.append(word)
                save(word,file)
            print("已记录 %d 个单词/词组"%len(words))
    return add
    
start = danci()
start()