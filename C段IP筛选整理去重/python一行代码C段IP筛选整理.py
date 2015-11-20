"""
python集合C段IP筛选整理.py
题目来源 http://www.bathome.net/thread-38037-1-2.html
依山居 7:51 2015/11/20
相关资料 Python 3语法小记（三） 集合set
http://blog.csdn.net/jcjc918/article/details/9359503

集合中的值唯一，可以用来去重
"""

with open("a.txt") as f:
    txt=f.readlines()
    f.close()

#改成集合解析的写法~语法与列表解析一样的。
ip={'.'.join(r.split(".")[0:3]+['1']) for r in txt}
[print(r) for r in ip]

try:
    input("回车退出")
except SyntaxError:
    pass

"""
输出：
192.168.6.1
192.168.5.1
192.169.3.1
192.168.9.1
192.168.2.1
192.168.1.1
"""
