"""
python批量获取网页的TITLE和Description节点文本.py
问题来源: http://www.bathome.net/thread-38114-1-1.html
依山居 13:38 2015/11/27

"""
import urllib
import urllib.request
import re
titlerec=re.compile("<(title)>(.*)</\\1?>")
desrec=re.compile('meta name=\"description\" content=\"(.*)\"')
charsetrec=re.compile('''<meta .*charset=.*"''',re.I)

with open("a.txt") as f:
    txt=[r.rstrip("\n") for r in f.readlines()]
    txt=["http://www.bathome.net/index.php"]
    for r in txt:
        url=urllib.request.urlopen(r)
        d=url.info()
        print(d)
        stat=url.getcode()
        print(stat)
        html=url.read()

        
        
