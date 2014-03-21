# -*- coding: utf-8 -*-
"""
Created on Tue Mar 18 21:40:28 2014

@author: Vespa
"""

import urllib2
import time
import sys
from zerocommon import *

def FindAnimate(dblist,inputname):
    """
    find animate match input from the database
    """
    idx = sorted(dblist);
    bestid = [];
    for id in idx:
        if len(re.findall(inputname,dblist[id]))>0:
            bestid.append(id);
    return bestid;
    

def ShowAnimateFound(name,idlist,dblist):
    """
    show the animate found, and let user make the choice;
    """
    if len(idlist) == 0:
        print name," Not Found!!";
        return 0;
    if len(idlist) == 1:
        if name == dblist[idlist[0]]:
            return 1;
        else:
            print "\nDownload :",dblist[idlist[0]],"?[Y/N]";
            result = raw_input("");
            if result.lower() == "y":
                return 1;
            else:
                return 0;
    
    print "\nAnimate Found Are Listed Below,Select The Index You Want:\n";
    for (i,id) in zip(range(1,len(idlist)+1),idlist):
        print "[%d]:%s"%(i,dblist[id]);
    print "[Q]:quit\n";
    
    while True:
        result = raw_input("Input:");
        if result.lower() == "q":
            return 0;
        if not result.isdigit():
            print "Input a Number";
        elif not int(result) in range(1,len(idlist)+1):
            print "Out of Range!!";
        else:
            return int(result);

def ShowEpsInfo(EPSInfo):
    """
    show Eps info for chioce
    4 in a row
    """
    eps_list = map(lambda x:x[1],EPSInfo);
    m_str = "";
    for (eps,epsinfo) in zip(range(1,len(eps_list)+1),eps_list):
        strtemp = "[%d]:%s"%(eps,epsinfo);
        m_str = m_str + strtemp.ljust(15);
        if not (eps % 4):
            m_str = m_str + "\n";
    print m_str;

def GetChoice():
    while True:
        inputrange = raw_input("Input Download Range:(For Example:2-10 or 17 or all)");
        if inputrange.find('-')>=0:
            eps = inputrange.split('-');
            if len(eps)==2 and eps[0].isdigit() and eps[1].isdigit():
                if int(eps[1]) >= int(eps[0]):
                    return range(int(eps[0]),int(eps[1])+1);
        elif inputrange.isdigit():
            return [int(inputrange)];
        elif inputrange.lower()=="all":
            return range(-1,1000);#Infinite
    return [];

def GetEpsInfo(id):
    """
    get (url,eps_name)
    """
    url = "http://dmxz.zerodm.net/xiazai/"+str(id)+".html";
    content = urllib2.urlopen(url).read();
    regexp = r"<a\s*href=['\"](.+?xunlei.+?)['\"].*?>(.*?)</a>";
    return GetRE(content,regexp);

def GetDLURL_xunlei(pageurl):
    try:
        content = urllib2.urlopen(pageurl).read();
    except:
        return [];
    regexp = r"href=['\"](http.+?sendfile.+?)['\"].*?>"
    urllist = GetRE(content,regexp);
    downloadlist = [];
    if len(urllist) == 0:
        return [];
    for url in urllist:
            downloadlist.append(url);
    return downloadlist;

def AnimateNameCheck(animate_name):
    """
    make sure the file name is valid;
    """
    if animate_name.find(r"/")>=0:
        animate_name = animate_name.replace(r"/","");
    if animate_name.find(r":")>=0:
        animate_name = animate_name.replace(r":","");
    if animate_name.find(r"?")>=0:
        animate_name = animate_name.replace(r"?","");
    return animate_name;

def DownLoad(EPSInfo,eps_range,animate_name):
    animatename = AnimateNameCheck(animate_name);
    downloadfile = open(animatename+".txt","w");
    EpsFailList = [];
    for i in range(len(EPSInfo)):
        if i+1 in eps_range:
            print "Getting Download URL for ",EPSInfo[i][1],":",;
            downloadlist = GetDLURL_xunlei(EPSInfo[i][0]);
            if len(downloadlist) == 0:
                print "Get Url Fail!!";
                EpsFailList.append(i);
            else:
                print "Get Daze!"
                for url in downloadlist:
                    downloadfile.write(url+"\n\n");
            if i != len(EPSInfo)-1:#LAST ONE DON'T NEED DELAY
                time.sleep(3);
            
    if len(EpsFailList) != 0:
        print "\n",animate_name,":\nItem(s) shown below get url fail,Please download it manually...";
        downloadfile.write(animate_name+":\nItem(s) shown below get url fail:\n");
        for eps in EpsFailList:
            print EPSInfo[eps][1],"  ",
            downloadfile.write(EPSInfo[eps][1]+":\n"+EPSInfo[eps][0]+"\n");
    
    downloadfile.close();


def main(argv):
    if len(argv) == 1:
        print """
Usages:
========================================================
python zerodm.py AnimateName
========================================================
Learn more detail,please visit:   www.kylen314.com/archives/5729"""
        return
    dblist = GetAnimateList();
    idlist = FindAnimate(dblist,argv[1]);
    choice = ShowAnimateFound(argv[1],idlist,dblist)-1;
    if choice != -1:
        print "Getting Info of ",dblist[idlist[choice]],".......";

        EPSInfo = GetEpsInfo(idlist[choice])
        ShowEpsInfo(EPSInfo);
        Eps_Range = GetChoice();
        DownLoad(EPSInfo,Eps_Range,dblist[idlist[choice]]);
        

if __name__ == '__main__':
    main(sys.argv);
    