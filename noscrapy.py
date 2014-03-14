import urllib2
import re
import time

def GetUrl(content,regexp):
    return re.findall(regexp, content)

def GetDownLoadURL(pageurl):
    content = urllib2.urlopen(pageurl).read()
    regexp = r"href=['\"](http.+?sendfile.+?)['\"].*?>"
    urllist = GetUrl(content,regexp);
    if len(urllist) == 0:
        print "Get Url Fail\n\n";
        return -1;
    for url in urllist:
            print url+"\n\n"
    return 1

def GetXuneliURL(idx,eps_range):
    url = "http://dmxz.zerodm.net/xiazai/"+str(idx)+".html"
    content = urllib2.urlopen(url).read();
    regexp = r"<a\s*href=['\"](.+?xunlei.+?)['\"].*?>";
    url_list = GetUrl(content,regexp);
    eps_regexp = r"<a\s*href=['\"].+?xunlei.+?['\"].*?>(\d\d)</a>";
    eps_list = GetUrl(content,eps_regexp);
    fail_list = []
    for i in range(0,len(url_list)):
        if int(eps_list[i]) in eps_range:
            print "EP",int(eps_list[i]),":"
            if -1 == GetDownLoadURL(url_list[i]):
                fail_list.append(int(eps_list[i]))
                continue;
            time.sleep(3);
    if len(fail_list) != 0:
        print "fail list:", fail_list

GetXuneliURL(2035,range(1,1000))
