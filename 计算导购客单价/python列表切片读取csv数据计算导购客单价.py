"""
python列表切片读取csv数据计算导购客单价.py
题目来源 https://github.com/FGFW/FCNNIC
依山居 19:44 2015/11/22
计算公式为:
导购日客单价=导购日成交金额/日客单数
每个相同的单据编号为1单,也就是去重后得到该导购的日客单数
导购日成交金额=导购完成的日所有单总和，也可以小计中倒数第二列直接提取
要求：计算出CSV表格中每位导购每天的客单价.
总结:这个版本要计算多个日期，逻辑复杂度多了一层，
忍不住写很了很多列表解析过滤,代码行数少，但是可读性和维护性应该差。
"""
with open("2014.08.01-2014.09.30零售数据.csv") as f:
    txt=[r.rstrip("\n").split(",") for r in f.readlines()]
dg={r[0] for r in txt if (r[0]!='') and ("普通零售" in r[5])}
dg=sorted(dg)
for d in dg:
    date={r[1] for r in txt if (d in r[0]) and ("-" in r[1])}
    date=sorted(date)
    for t in date:
        导购成交金额=sum([float(s[-2]) for s in txt if (d in s[0] and (t in s[1]) and s[-2]!='')])
        日单数=len({s[2] for s in txt if (d in s[0] and (t in s[1]) and s[-4])})
        导购客单价=导购成交金额/日单数
        print(d,"%s 成交额:%4.2f 客单价:%2.2f 日单数:%2d" %(t,导购成交金额,导购客单价,日单数))


try:
    input("按回车退出")
except SyntaxError:
    pass

"""
输出：
...
顾意珍 2014-09-13 成交额:539.00 客单价:26.95 日单数:20
顾意珍 2014-09-14 成交额:397.00 客单价:22.06 日单数:18
黎丽群 2014-08-15 成交额:489.00 客单价:19.56 日单数:25
...
"""
