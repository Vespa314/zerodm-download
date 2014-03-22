# -*- coding: utf-8 -*-
"""
Created on Sun Mar 16 19:16:27 2014

@author: Vespa
"""

import urllib2
import time
import sys
from zerocommon import *

def GetAnimateTitle(id):
    url = "http://dmxz.zerodm.net/xiazai/"+str(id)+".html";
    headers = {'User-Agent':'Mozilla/5.0 (Windows; U; Windows NT 6.1; en-US; rv:1.9.1.6) Gecko/20091201 Firefox/3.5.6'}
    req = urllib2.Request(url = url,headers = headers);   
    try:
        content = urllib2.urlopen(req).read();
    except:
#        print "url %s not exist!" % url;
        return None;
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
    lastline = "";
    for line in f:
        lastline = line;
    f.close();
    if len(lastline) == 0:
        return 1;
    return int(lastline.split("::")[0])+1;

def CreateDatabase(mode):
    databasefile = open("database.dat",mode);
    invalidfile = open("invalid.dat",mode);
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
    
def main(argv):
    message = """
Usages:
========================================================
python database.py -u[pdate]
python database.py -c[reate]:Not recommended
python database.py -r[echeck]:Not recommended
========================================================
Learn more detail,please visit:   www.kylen314.com/archives/5729""";
    if len(argv) != 2 or len(argv[1]) < 2 or argv[1][0] !="-":
        print message;
        return;
    command = argv[1][1].lower();
    if command == "c":
        CreateDatabase("w");
    elif command == "r":
        Check();
    elif command == "u":
        CreateDatabase("a+");
    else:
        print message;
    
    
if __name__ == '__main__':
    main(sys.argv);