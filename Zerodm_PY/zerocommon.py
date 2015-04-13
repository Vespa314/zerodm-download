# -*- coding: utf-8 -*-
"""
Created on Sun Mar 16 19:28:48 2014

@author: Vespa
"""
import re
import os
import sys

class UnicodeStreamFilter:
    def __init__(self, target):
        self.target = target
        self.encoding = 'utf-8'
        self.errors = 'replace'
        self.encode_to = self.target.encoding
    def write(self, s):
        if type(s) == str:
            s = s.decode("utf-8")
        s = s.encode(self.encode_to, self.errors).decode(self.encode_to)
        self.target.write(s)

if sys.stdout.encoding == 'cp936':
    sys.stdout = UnicodeStreamFilter(sys.stdout)

def GetRE(content,regexp):
    return re.findall(regexp, content)

def toUTF8(input_str):
    try:
        input_str.decode('utf8')
    except:
        input_str = input_str.decode('gbk').encode('utf8')
    return input_str

def encodeFileName(f):
    if sys.stdin.encoding == 'cp936':
        return f.decode('utf8').encode('gbk')
    else:
        return f

def GetAnimateList():
    if not os.path.exists("./database.dat"):
        print "database.dat not exist!"
        return None
    f = open("database.dat","r")
    animateList = {}
    for line in f:
        info = line.strip("\n").split("::")
        animateList[info[0]] = info[1]
    f.close()
    return animateList