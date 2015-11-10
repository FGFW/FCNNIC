"""
python汉字随机组合.py
依山居 7:07 2015/11/11
相关资料
Python random模块
http://my.oschina.net/cuffica/blog/33336
题目来源： http://www.bathome.net/viewthread.php?tid=37773
"""

import time
import random
start=time.time()

s="圣诚杰安博彬宝斌超盛畅灿纯恩帆福富贵桂瀚豪翰皓弘\
恒海宏洪涵慧荷蕙航嘉俊君峻健和禾佳静娇娟净睛善康坤兰\
岚莲丽立亮伶俪明名铭美宁朋鹏琪芹清晴胜思顺舒森升潭婷\
伟文益宜韵阳运乐怡芸盈园翊智哲志振展忠昭真正雅悦莹娅欣勋轩旭新熙金真"

for r in range(5):
    print(random.sample(s,2))
end=time.time()
pt=end-start
print("程序运行时间：",pt)
try:
    input("按回车退出")
except SyntaxError:
    pass

"""
输出：
['睛', '明']
['兰', '正']
['园', '婷']
['福', '雅']
['顺', '亮']
程序运行时间： 0.0260009765625
按回车退出
"""
