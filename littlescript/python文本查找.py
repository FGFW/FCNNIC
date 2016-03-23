"""python文本查找.py
http://bbs.bathome.net/thread-39743-1-1.html
2016年3月20日 08:43:25 codegay
"""

with open("大秦帝国1黑色裂变 (1).txt",encoding="cp936") as f:
    ini=[r for r in f if r.startswith("第") and "章" in r and "节" in r]
with open("result.ini","w+") as f:
    f.writelines(ini)

