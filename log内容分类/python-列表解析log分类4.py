"""
python-列表解析log分类4.py
http://stackoverflow.com/questions/36182906/regex-matching-of-numbers-and-redirecting-them-to-different-output-files/36185163
2016年3月26日 01:27:19 codegay
"""
with open("event_1.log") as f,open("0.log","w+") as f0, open("1.log","w+") as f1:
    isad=lambda r:r.split()[0] in ['a','d']
    #is0=lambda r:f0.write(r) if r.split()[1]=='0' else 0
    is0=lambda r:r.split()[1]=='0' and f0.write(r)
    #is1=lambda r:f1.write(r) if r.split()[1]=='1' else 0
    is1=lambda r:r.split()[1]=='1' and f1.write(r)
    [is0(r) or is1(r) for r in f if isad(r)]
