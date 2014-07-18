# -*- coding: utf-8 -*-
"""
Created on Sun Mar 16 19:16:27 2014

@author: Vespa
"""

import urllib2
from zerocommon import *

if __name__ == '__main__':
#    main(sys.argv);
    url = "http://dmxz.zerodm.net/top/all/";
    headers = {'User-Agent':'Mozilla/5.0 (Windows; U; Windows NT 6.1; en-US; rv:1.9.1.6) Gecko/20091201 Firefox/3.5.6'}
    req = urllib2.Request(url = url,headers = headers);   
    content = urllib2.urlopen(req).read();
    
    regexp = r'<a title="[^>]*" href="http://dmxz.zerodm.net/xiazai/([^>]+)">([^>]+)</a>'
    animatelist = GetRE(content,regexp);
        
    f = open("database.dat","r");
    Existlist = [];
    for line in f:
        line = line.split("::");
        Existlist.append(line[0]);
    f.close();
    
    f = open("database.dat",'w');
    newcounter = 0;
    for (animateIdx,animateName) in animatelist:
        animateIdx = animateIdx.split(".html");
        animateIdx = animateIdx[0];
        animateName = animateName.decode('utf8','ignore').encode('gbk','ignore')
        f.write('%s::%s\n'%(animateIdx,animateName));
        if animateIdx not in Existlist:
            print "Add",animateName
            newcounter += 1
    f.close();
    print "Finished!! Add",newcounter,"new Animates!!"