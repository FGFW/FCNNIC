#一行内容分行输出
#依山居 18:14 2015/11/4
a="aA1一bB2二cC3三dD4四eE5五fF6六gG7七hH8八iI9九"
for r in range(0,4):
    t=''
    for s in range(0+r,len(a),4):
        t=t+a[s]
    print(t)

l=list(a)
for r in range(0,4):
    t=''
    for s in range(0,9):
        t=t+l.pop()
    print(t)
