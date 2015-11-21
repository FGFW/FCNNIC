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
