"""
相关资料:
Python fetching <title> 
http://stackoverflow.com/questions/1660302/python-fetching-title
How can I retrieve the page title of a webpage using Python?
http://stackoverflow.com/questions/51233/how-can-i-retrieve-the-page-title-of-a-webpage-using-python#51242

"""
import lxml.html
import urllib
title=[]
des=[]
with open("a.txt") as f:
    a=f.read()
    a=a.rsplit()
    for l in a:
        print(l)
        html=lxml.html.parse(l)
        title.append(html.find(".//title").text+"\n")
        #des.append(html.find(".//meta").get("name")+"\n")
        des=html.find(".//meta").drop_tag()
        print(help(des))
        print(des)


