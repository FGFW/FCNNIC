"""
python列表切片处理DEL文件断行.py
这版的代码是之前列表切片版的改进，目的是把DEL文件中不以引号开头的行与上一行连接
下一行不以引号开头则清除行后的空白字符，包括\n，在写入的时候就自动与上一行连接了。
http://www.bathome.net/thread-38164-1-1.html
"""

import time
start=time.time()
print("运行中..."*3)

txt=[]
with open("a.txt") as f:
    txt=f.readlines()

    end=time.time()
    pt=end-start
    print("readlines运行耗时：",pt)

    ln=len(txt)
    print("需要处理的文件行数：",ln)

    end=time.time()
    pt=end-start
    print("len(txt)运行耗时：",pt)
    #为了防指针越界，所以rn需要减1
    #flines=[txt[r] if ('\"' in txt[r+1][0]) else txt[r].rstrip() for r in range(ln-1)]
    #与上一行等效写法
    flines=[txt[r] if (txt[r+1].startswith('\"')) else txt[r].rstrip() for r in range(ln-1)]
	
end=time.time()
pt=end-start
print("flines运行耗时：",pt)

with open("out.txt","w+") as f:
    f.writelines(flines)
    #补上最后一行
    f.write(txt[-1])
    f.close()
    
txt[:]=[]
flines[:]=[]

end=time.time()
pt=end-start
print("运行耗时：",pt)
try:
    input("按回车退出")
except SyntaxError:
    pass

"""
测试结果，列表切片和模式匹配处理速度相当，670M的文本，大约60-70秒左右，
包括写入时间,算出处理速度大约是每秒处理10M左右。
实际发现内存占用峰值会高出好几倍，python 进程会短时占用好几个G内存的情况。

"""
