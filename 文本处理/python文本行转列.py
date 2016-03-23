"""
python行转列.py
http://bbs.bathome.net/thread-39716-1-1.html
2016年3月17日 18:58:14 codegay
强行装B
"""
import subprocess
with open("a.txt") as f:
    #[subprocess.call(["echo",h+r.split(":")[0]+">>b.txt"]) for h in l.split(",") for l in r.split(":")[1] for r in f.readlines()]
    [subprocess.call(["echo",l+r.split(":")[0]+">>b.txt"]) for l in r.split(":")[1].split(",") for r in f.readlines()]

