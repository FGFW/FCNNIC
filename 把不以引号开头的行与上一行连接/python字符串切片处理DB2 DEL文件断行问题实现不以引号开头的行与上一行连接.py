"""
python字符串切片处理DB2 DEL文件断行问题实现不以引号开头的行与上一行连接.py
题目来源 http://www.bathome.net/thread-38164-1-1.html
依山居  17:47 2015/11/24
这个解决思路在脑子里绕了好几天~找到\n也就是换行符，同时切出它的下一位不为"号的字符。
也就是不以引号开头行的第一个字。然后再替换掉\n
感觉这个处理方法,不需要正则表达式可靠性也很高。
"""
import time
start=time.time()
print("运行中..."*3)

with open("a.txt") as f:
    txt=f.read()
#增加字符长度,取\n的下一位字符时就不用担心和考虑越界的问题
txt=txt+"###"
rn=len(txt)
#找到\n也就是换行符，同时切取出它的下一位不为"号的字符。
rs=[txt[r]+txt[r+1] for r in range(rn-3) if ("\n" in txt[r]) and ('\"' not in txt[r+1])]
#rs=['\n2', '\n5', '\n2', '\n3'...]
for r in rs:
    #设r为\n3,替换为r[1]也就是换为3，相当于删掉了\n。这个不以引开头的行就能与上行连接了。
    txt=txt.replace(r,r[1])
txt=txt.rstrip("###")+"\n"
with open("aa.txt","w+") as f:
    f.write(txt)

end=time.time()
pt=end-start
print("运行耗时：",pt)
try:
    input("按回车退出")
except SyntaxError:
    pass
