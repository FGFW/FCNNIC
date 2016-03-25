"""
python-列表解析log分类5.py
http://stackoverflow.com/questions/36182906/regex-matching-of-numbers-and-redirecting-them-to-different-output-files/36185163
2016年3月26日 07:23:32 codegay
"""
with open("event_1.log") as f,open("0.log","w+") as f0, open("1.log","w+") as f1:
    isad=lambda x:x.split()[0] in ['a','d'] and x.split()[1] in ['0','1']
    [f0.write(r) if r.split()[1]=='0' else f1.write(r) for r in f if isad(r)]
