"""
python对齐日志的日期时间.py
http://bbs.bathome.net/thread-39867-1-1.html
2016年4月1日 06:04:16 codegay
"""
with open("result.log","w+") as f:
    for r in open("log.log"):
        line=r.split("|||")
        line[3]=line[3].ljust(26,"0")
        line[5]=line[5].ljust(26,"0")
        f.write('|||'.join(line))
