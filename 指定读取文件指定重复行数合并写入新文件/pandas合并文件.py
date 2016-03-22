"""
pandas合并文件.py
http://www.oschina.net/question/2649224_2159211
2016年3月22日 19:38:03 codegay
 
"""
import pandas
import glob
for r in glob.glob("test*.csv"):
        csv=pandas.read_csv(r)
        csv.to_csv("test.txt",mode="a+")
