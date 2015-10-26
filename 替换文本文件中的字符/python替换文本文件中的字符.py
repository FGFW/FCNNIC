#python3替换文本文件中的字符.py
#努力把论坛变成一个花样编程论坛~哈哈~~~
f="a.txt"
s="*.cn"
t="FFF空格FFF"
#方法1 字符替换
def f1(f,s,t):
    a=open(f,"r")
    txt=a.read()
    a=open(f,"w")
    txt=txt.replace(s,t)
    a.write(txt)
    a.close()
    print("f1:\n",txt)
#f1(f,s,t)

#方法2 正则替换
import re
s="\*\.cn"
def f2(f,s,t):
    a=open(f,"r")
    txt=a.read()
    a=open(f,"w")
    s=re.compile(s)
    txt=re.sub(s,t,txt)
    a.write(txt)
    a.close()
    print("\r\nf2:",txt)
#f2(f,s,t)

#方法3 split切分再join
txt=open(f,"r").read()
txt=txt.split("*.cn")
txt=t.join(txt)
print(txt)

'''
output:
23423回来日3咽螺距3是啊kljsdfsjf;ajs;fdjsafjsklfjklsdjfklsjfklj3klFFF空格FFFkljdsflkklfsjFFF空格FFFkljdfkjdfjdlkjkl*.com
'''
