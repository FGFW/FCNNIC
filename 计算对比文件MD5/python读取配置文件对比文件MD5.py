"""
python读取配置对比文件MD5.py
http://www.oschina.net/question/2635041_2151586
2016年2月26日 21:09:52 codegay
"""
import re
import hashlib

def configmd5(file="file.md5"):
    configdict={r.rstrip("\n").split(":")[0]:r.rstrip("\n").split(":")[1] for r in open(file).readlines()}
    return configdict

def configmd51(file="file.md5"):
    configdict={}
    for r in open(file):
        fmd5=r.rstrip("\n").split(":")
        configdict[fmd5[0]]=fmd5[1]
    return configdict

def reconfigmd5(file="file.md5"):
    import re
    txt=open(file).read()
    result=re.findall(r"(.*/?.+):([a-fA-F0-9]{32})",txt)
    configdict={k:v for k,v in result}
    return configdict
#以上三个函数功能目的输出结果一样,只是写法不一样。都是读取配置文件file.md5数据成对格式化为字典。

def md5(seq):
    results={}
    for s in seq:
        #如果考虑处理超大的文件或者控制内存的占用量,
        #不能使用一次性读取文件的写法
        fb=open(s,"rb").read()
        fmd5=hashlib.md5(fb).hexdigest()
        results[s]=[cmd5[s],fmd5,cmd5==fmd5]
        #字典存储结果，{文件名作为键名:[配置文件中的MD5值,实际文件的MD5，对比结果]
    print(results)
    return results
                
cmd5=reconfigmd5()
md5(cmd5.keys())
