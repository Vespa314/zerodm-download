import urllib2
import re
import time
 
def GetUrl(content,regexp):
    return re.findall(regexp, content)
 
#��ȡ��������
def GetDownLoadURL(pageurl):
    content = urllib2.urlopen(pageurl).read()
    regexp = r"href=['\"](http.+?sendfile.+?)['\"].*?>"
    for url in GetUrl(content,regexp):
        print url+"\n\n"
 
#��ȡ������������ҳ��URL    
def GetXuneliURL(idx):
    url = "http://dmxz.zerodm.net/xiazai/"+str(idx)+".html"
    content = urllib2.urlopen(url).read()
    regexp = r"<a\s*href=['\"](.+?xunlei.+?)['\"].*?>"
    for download_page in GetUrl(content,regexp):
        GetDownLoadURL(download_page)
        time.sleep(1)
 
map(GetXuneliURL,[2000,2029]) 