"""
python解字迷abc+bcd+cde+def+efg==ghij.py
https://www.wolframcloud.com/objects/01b74b78-aef6-4413-b140-108e40b2068c
2016年3月30日 21:56:14 codegay

题目:
abc+bcd+cde+def+efg==ghij，每个字母代表0-9之中唯一数字。
例如 186+867+679+790+903==3425 
问满足条件的共有多少组解？ 最大的ghij是多少？
"""
def ff1():
#permutations()参考资料 https://docs.python.org/3.4/library/itertools.html
    from itertools import permutations
    result=[]
    for r in permutations(range(10)):
        a,b,c,d,e,f,g,h,i,j=r
        abc=a*100+b*10+c
        bcd=b*100+c*10+d
        cde=c*100+d*10+e
        def0=d*100+e*10+f
        efg=e*100+f*10+g 
        ghij=g*1000+h*100+i*10+j
        if ghij==abc+bcd+cde+def0+efg :
            if abc>=100 and bcd >=100 and cde>=100 and def0>=100 :
                if efg>=100 and 1000<=ghij<10000 :
                    if len(set(str(ghij)))==len(str(ghij)):
                        result.append(ghij)
    print("问题答案1:",len(result))
    print("最大的ghij是多少？",max(result))
#问题答案1: 108
#最大的ghij是多少？ 3425
#[Finished in 5.5s]
ff1()
