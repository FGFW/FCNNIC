"""
如何将一组字符串打乱原有顺序
http://bbs.bathome.net/thread-39382-1-1.html
2016年2月16日 11:25:56 依山居
"""

#方法1 利用集合无序的特性乱序，每次程序重新运行输出的序是不一样的。
#同理可以字典键唯一且无序的也是可以的。
s="爱民 玉伟 伟博 如祥 良智 富强 光耀 智博 来德 金吉 李松海"
print(set(s.split()))

#方法2 优先推荐python内置random.sample()
import random
ss="爱民 玉伟 伟博 如祥 良智 富强 光耀 智博 来德 金吉 李松海"
ns=ss.split()

#运行可见下面相同的代码输出内容的顺序不一样。
rs=random.sample(ns,len(ns))
print(rs)

rs=random.sample(ns,len(ns))
print(rs)

try:
    input("回车退出")
except SyntaxError:
    pass


