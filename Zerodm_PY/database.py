# -*- coding: utf-8 -*-
"""
Created on Sun Mar 16 19:16:27 2014

@author: Vespa
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
#        print "url %s not exist!" % url;
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

def CreateDatabase():
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

def GetAnimateList():
    if not os.path.exists("./database.dat"):
        print "database.dat not exist!";
        return None;
    f = open("database.dat","r");
    animateList = {};
    for line in f:
        info = line.strip("\n").split("::");
        if animateList.get( int(info[0]) ) != None:
            print "Item %s(%s) is repeat;"%(info[0],info[1]);
            f.close();
            return None;
        else:
            animateList[int(info[0])] = info[1];
    f.close();
    return animateList;

def RecreateDB(animateList):
    databasefile = open("database.dat","w");
    idx = sorted(animateList);
    for id in idx:
        databasefile.write("%d::%s\n" % (id,animateList[id]));
    databasefile.close();

def ReCreateInvalidFile(invalidlist):
    invalidfile = open("invalid.dat","w");
    for id in invalidlist:
        invalidfile.write("%d\n"%id);
    invalidfile.close();
    
def Check():
    if not os.path.exists("./invalid.dat"):
        print "invalid.dat not exist!";
        return;
    animateList = GetAnimateList();
    if animateList == None:
        print "database.dat Read Fail!";
        return;
        
    print "DataBase Read Finished!!";
    invalidfile = open("invalid.dat","r");
    invalidlist = [];
    
    for line in invalidfile:
        id = int(line);
        title = GetAnimateTitle(id);        
        if title != None:
            print "Find %d(%s) existed!"%(id,title);
            if animateList.get(id) == None:
                animateList[id] = title;
            time.sleep(2);
        else:
            print "%d Still Not Found!"% (id);
            invalidlist.append(id);    
        
    invalidfile.close;
    
    RecreateDB(animateList);
    ReCreateInvalidFile(invalidlist)
    print "Database Rebuild!"
    

if __name__ == '__main__':
    Check();