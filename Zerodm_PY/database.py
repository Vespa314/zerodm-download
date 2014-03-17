# -*- coding: utf-8 -*-
"""
Created on Sun Mar 16 19:16:27 2014

@author: ss
"""

import urllib2
import time
import os
from zerocommon import *

def GetAnimateTitle(id):
    url = "http://dmxz.zerodm.net/xiazai/"+str(id)+".html";
    try:
        urllib2.urlopen(url);
    except:
        print "url %s not exist!" % url;
        return None;
    content = urllib2.urlopen(url).read();
    regexp = r'<p class="nrymc">(.+?)</p>';
    result = GetRE(content,regexp);
    if len(result)>0:
        return result[0];
    else:
        return None;

def GetBeginIndex():
    if not os.path.exists("./database.dat"):
        return 1;
    f = open("database.dat","r");
    for line in f:
        pass;
    f.close()
    return int(line.split("::")[0])+1;

databasefile = open("database.dat","a+");
invalidfile = open("invalid.dat","a+");
id = GetBeginIndex();
invalid_counter = 0;
while True:
    title = GetAnimateTitle(id);
    if None == title:
        invalid_counter = invalid_counter + 1;
        invalidfile.write("%d\n" % (id));
        id = id + 1;
        if invalid_counter > 10:
            break;
        continue;
    invalid_counter = 0;
    databasefile.write("%d::%s\n" % (id,title));
    print "Add Animate Item:%s(%d)" % (title,id);
    id = id + 1;
    time.sleep(2);
databasefile.close();
invalidfile.close();
