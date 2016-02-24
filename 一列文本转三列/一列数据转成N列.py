"""
一列数字转成N列.py
2016年2月24日 05:45:58 codegay

"""
#生成测试数据,得到a.txt为1列1-999的内容
with open("a.txt","w+") as f:
    [f.write(str(r).zfill(4)+"\n") for r in range(1,999)]

#一列数字转成N列.py
N=50
with open("a.txt","r+") as f:
    #脱掉数据后面的换行符,如果能被N整除则保留
    txt=f.readlines()
    sn=[txt[r] if (r>1 and (r+1)%N==0) else txt[r].replace("\n",",") for r in range(0,len(txt)) ]
    print(sn)
    #指针回到文件头部清空文件
    f.seek(0)
    f.truncate()
    f.writelines(sn)
    
    

