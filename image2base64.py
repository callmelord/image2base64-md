#! /usr/bin/python3.8
#coding: utf-8
import base64
import os

path = "./"
files= os.listdir(path)
file1 = 'data.txt'
fi = open(file1,'w')
a = []
for file in files:
    if not os.path.isdir(file) and ".png" in file:
        f = open(path+"/"+file, 'rb'); #二进制的方式打开图文件
        ls_f=base64.b64encode(f.read()) #读取文件内容，转换为base64编码
        a.append("[" + file +"]:data:image/png;base64,"+str(ls_f)[2:-1])
    elif not os.path.isdir(file) and ".md" in file:
        b = file
with open(b, 'a+') as f:
    for n in a:
        f.write(n)
        f.write("\n")

