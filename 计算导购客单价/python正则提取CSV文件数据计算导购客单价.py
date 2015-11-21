'''
python正则提取CSV文件数据计算导购客单价.py
依山居 4:36 2015/11/22
看了看python自带的csv库貌似也没能解决啥问题，
干脆就自己用正则来写了代码量出乎意料的少
'''
import re
rec=re.compile("\((.+)\)小计.+,.+,(\d+.\d+),.*")
with open("0914零售数据.csv") as f:
    cf=f.read()
    f.close()
dglist=re.findall(rec,cf) #得到格式如[('顾意珍', '480.00'), ('张彩菊', '505.00'),..]
for d,t in dglist:
    rec=re.compile("%s,\d+-\d+-\d+,(\w+-\d+),"%d)
    多少单=len({l for l in re.findall(rec,cf)}) #相同的单号只算一个单,正则查找的结果放在集合，
                                            #集合中元素不重复所以len长度可以得到该导购的单量
    客单价=float(t)/多少单
    print("导购:%s 日销售额: %s 日客单价:%3.2f  日单量:%s" %(d,t,客单价,多少单))

