"""
python正则取一列数中连续最长的奇数个数.py
题目来源http://www.oschina.net/code/snippet_2519674_52255
大费周折地使用正则表达式来干这事~~只能处理个位数
如果输入有两位数以上如47...那完蛋。不具备实用性，只能玩耍和练习
依山居 8:20 2015/11/21
"""
a=[2,3,3,0,0,2,4,7,5,7]
import re
rn=[i for i in range(0,10) if (i%2!=0)]    #rn=[1, 3, 5, 7, 9]
res=str(rn).replace(",","")+"+"    #res='[1 3 5 7 9]+'
s=''.join([str(i) for i in a])    #s='2330024757'
rec=re.compile(res)
result=re.findall(rec,s)     #result=['33', '757']
print(max([len(s) for s in result]))

#模式匹配方法2 改进(= =折腾死了)，可以处理两位及正负号的情况
a=[2,3,3,0,0,2,4,7,5,7,24234,24234,5345,564,464,242,-34,-89,-67,-2341,999,9,9,99]
import re
a=' '.join([str(r) for r in a])
a=re.sub(r"[-+]?\d*[13579]","1",a)
a=re.sub(r"[-+]?\d*[24680]","0",a)
a=a.replace(" ","").split("0")
print(max([len(r) for r in a]))
