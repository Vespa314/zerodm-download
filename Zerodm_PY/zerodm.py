#!/usr/bin/env python
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
    idx = sorted(dblist)
    bestid = []
    for id in idx:
        if len(re.findall(inputname.lower(),dblist[id].lower()))>0:
            bestid.append(id)
    return bestid


def ShowAnimateFound(name,idlist,dblist,quickmode = 0):
    """
    show the animate found, and let user make the choice
    """
    if len(idlist) == 0:
        print name," Not Found!!"
        return 0
    if len(idlist) == 1:
        if name == dblist[idlist[0]] or quickmode:
            return 1
        else:
            print "\nDownload :",dblist[idlist[0]],"?[Y/N]"
            result = raw_input("")
            if result.lower() == "y":
                return 1
            else:
                return 0

    print "\nAnimate <<%s>> Found Are Listed Below,Select The Index You Want:\n"%(name)
    for (i,id) in zip(range(1,len(idlist)+1),idlist):
        print "[%d]:%s"%(i,dblist[id])
    print "[Q]:quit\n"

    while True:
        result = raw_input("Input:")
        if result.lower() == "q":
            return 0
        if not result.isdigit():
            print "Input a Number"
        elif not int(result) in range(1,len(idlist)+1):
            print "Out of Range!!"
        else:
            return int(result)

def ShowEpsInfo(EPSInfo):
    """
    show Eps info for chioce
    4 in a row
    """
    eps_list = map(lambda x:x[1],EPSInfo)
    m_str = ""
    for (eps,epsinfo) in zip(range(1,len(eps_list)+1),eps_list):
        strtemp = "[%d]:%s"%(eps,epsinfo)
        m_str = m_str + strtemp.ljust(15)
        if not (eps % 4):
            m_str = m_str + "\n"
    print m_str

def GetChoice():
    while True:
        inputrange = raw_input("Input Download Range:(For Example:2-10 or 17 or all)")
        if inputrange.find('-')>=0:
            eps = inputrange.split('-')
            if len(eps)==2 and eps[0].isdigit() and eps[1].isdigit():
                if int(eps[1]) >= int(eps[0]):
                    return range(int(eps[0]),int(eps[1])+1)
        elif inputrange.isdigit():
            return [int(inputrange)]
        elif inputrange.lower()=="all":
            return range(-1,1000);#Infinite
    return []

def GetEpsInfo(id):
    """
    get (url,eps_name)
    """
    if GetRE(id,r'\d+') != []:
        url = "http://dmxz.zerodm.tv/xiazai/"+id+".html"
    else:
        url = "http://dmxz.zerodm.tv/xiazai/"+id
    headers = {'User-Agent':'Mozilla/5.0 (Windows; U; Windows NT 6.1; en-US; rv:1.9.1.6) Gecko/20091201 Firefox/3.5.6'}
    req = urllib2.Request(url = url,headers = headers)
    content = toUTF8(urllib2.urlopen(req).read())
    regexp = r"<a\s*href=['\"](.+?xunlei.+?)['\"].*?>(.*?)</a>"
    return GetRE(content,regexp)

def GetDLURL_xunlei(pageurl):
    try:
        content = urllib2.urlopen(pageurl).read()
    except:
        return []
    regexp = r"href=\"(http://gdl\.lixian\.vip\.xunlei\.com/download\?[^\"]*)\" download=\"([^\"]*)"
    urllist = GetRE(content,regexp)
    downloadlist = []
    if len(urllist) == 0:
        return []
    for url in urllist:
        url = url[0].replace("download",url[1])
        downloadlist.append(url)
    return downloadlist

def AnimateNameCheck(animate_name):
    """
    make sure the file name is valid
    """
    if animate_name.find(r"/")>=0:
        animate_name = animate_name.replace(r"/","")
    if animate_name.find(r":")>=0:
        animate_name = animate_name.replace(r":","")
    if animate_name.find(r"?")>=0:
        animate_name = animate_name.replace(r"?","")
    return animate_name

def DownLoad(EPSInfo,eps_range,animate_name):
    animatename = AnimateNameCheck(encodeFileName(animate_name))
    downloadfile = open(animatename+".txt","w")
    EpsFailList = []
    for i in range(len(EPSInfo)):
        if i+1 in eps_range:
            print "Getting Download URL for ",EPSInfo[i][1],":",
            downloadlist = GetDLURL_xunlei(EPSInfo[i][0])
            if len(downloadlist) == 0:
                print "Get Url Fail!!"
                EpsFailList.append(i)
            else:
                print "Get Daze!"
                for url in downloadlist:
                    downloadfile.write(url+"\n\n")
            if i != len(EPSInfo)-1:#LAST ONE DON'T NEED DELAY
                time.sleep(3)

    if len(EpsFailList) != 0:
        print "\n",animate_name,":\nItem(s) shown below get url fail,Please download it manually..."
        downloadfile.write(animate_name+":\nItem(s) shown below get url fail:\n")
        for eps in EpsFailList:
            print EPSInfo[eps][1],"  ",
            downloadfile.write(EPSInfo[eps][1]+":\n"+EPSInfo[eps][0]+"\n")
        print "\n"
    downloadfile.close()

def DownloadSingleAnimate(dblist,argv):
    idlist = FindAnimate(dblist,argv)
    choice = ShowAnimateFound(argv,idlist,dblist)-1
    if choice != -1:
        print "Getting Info of ",dblist[idlist[choice]],"......."
        EPSInfo = GetEpsInfo(idlist[choice])
        ShowEpsInfo(EPSInfo)
        Eps_Range = GetChoice()
        DownLoad(EPSInfo,Eps_Range,dblist[idlist[choice]])

def downloadFile(dblist,filename):
    AnimateList = {}
    for animateName in open(filename,'r'):
        if animateName.find('\n')>=0:
            animateName = animateName.replace('\n','')
        if animateName.find('\r')>=0:
            animateName = animateName.replace('\r','')


        idlist = FindAnimate(dblist,animateName)
        choice = ShowAnimateFound(animateName,idlist,dblist,1)-1
        if choice != -1:
            AnimateList[idlist[choice]]= dblist[idlist[choice]]

    for id in AnimateList:
        EPSInfo = GetEpsInfo(id)
        Eps_Range = range(-1,1000)
        print 'downloading ',AnimateList[id],'...'
        DownLoad(EPSInfo,Eps_Range,AnimateList[id])

    print "Finished"

def main(argv):
    if len(argv) == 1:
        print """
Usages:
========================================================
Single Animate:
    python zerodm.py AnimateName
Animate in file:
    python zerodm.py downloadlist.txt
========================================================
Learn more detail,please visit:   www.kylen314.com/archives/5729"""
        return

    dblist = GetAnimateList()
    if dblist == {}:
        print "Database Read Fail!"
        return

    command = argv[1][-4:].lower()
    if command == ".txt":
        downloadFile(dblist,argv[1])
    else:
        DownloadSingleAnimate(dblist,toUTF8(argv[1]))

if __name__ == '__main__':
    main(sys.argv)
