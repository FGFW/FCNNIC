"""
依山居 2016年1月7日 13:18:56
"""
with open("IP.txt") as f:
    txt=f.readlines()
print("文件总行数:",len(txt))
ip={'.'.join(r.split(".")[:3]+["0-20\n"]) for r in txt}
ip=sorted(ip)
print("处理后的行数:",len(ip))

with open("ipresult.txt","w+") as f:
    f.writelines(ip)

