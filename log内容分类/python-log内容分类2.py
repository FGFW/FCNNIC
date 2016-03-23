"""
python正则log内容分类.py
http://stackoverflow.com/questions/36182906/regex-matching-of-numbers-and-redirecting-them-to-different-output-files/36185163#36185163
2016年3月24日 00:54:44 codegay
"""
with open("event_1.log") as f,open("0.log","w+") as f0, open("1.log","w+") as f1:
    for line in f:
        sl=line.split()
        result0=sl[1]=="0" and sl[0]=="a" or sl[1]=="d"
        result1=sl[1]=="1" and sl[0]=="a" or sl[1]=="d"
        if result0:
            f0.write(line)
            print(line)
        if result1:
            f1.write(line)
