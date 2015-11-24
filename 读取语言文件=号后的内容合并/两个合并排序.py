

with open("en_US.lang",encoding="utf-8") as f:
    en=f.readlines()
 
print(en[0])

with open("zh_CN.lang",encoding="utf-8") as f:
    zh=f.readlines()

a=sorted(en+zh)

with open("2.txt","w+",encoding="utf-8") as f:
    f.writelines(a)
    f.close()
