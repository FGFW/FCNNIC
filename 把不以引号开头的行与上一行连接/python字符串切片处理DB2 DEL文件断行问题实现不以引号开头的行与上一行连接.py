"""
python字符串切片处理DB2 DEL文件断行问题实现不以引号开头的行与上一行连接.py
题目来源 http://www.bathome.net/thread-38164-1-1.html
依山居  17:47 2015/11/24
这个解决思路在脑子里绕了好几天~找到\n也就是换行符，同时切出它的下一位不为"号的字符。
也就是不以引号开头行的第一个字。然后再替换掉\n
感觉这个处理方法,不需要正则表达式可靠性也很高。
2:18 2015/11/25 补充：见文件尾部分测试总结，这个方法效率非常低。
处理数M的文件已经慢得不行了。
"""
import time
start=time.time()
print("运行中..."*3)

with open("a.txt") as f:
    txt=f.read()
#增加字符长度,取\n的下一位字符时就不用担心和考虑越界的问题
txt=txt+"###"
rn=len(txt)
print("长度：",rn)
end=time.time()
pt=end-start
print("运行耗时：",pt)

#找到\n也就是换行符，同时切取出它的下一位不为"号的字符。
rs=[txt[r]+txt[r+1] for r in range(rn-3) if ("\n" in txt[r]) and ('\"' not in txt[r+1])]
print("多少行不以引开头:",len(rs))
end=time.time()
pt=end-start
print("运行耗时：",pt)

#rs=['\n2', '\n5', '\n2', '\n3'...]
for r in rs:
    #设r为\n3,替换为r[1]也就是换为3，相当于删掉了\n。这个不以引开头的行就能与上行连接了。
    txt=txt.replace(r,r[1])

end=time.time()
pt=end-start
print("运行耗时：",pt)

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

"""
测试总结:
与直觉相反，并不是逐字扫描慢，而是在进行迭代replace慢。非常非常非常非常慢~
经测试慢在这个部分，测试生成测试文件3M 三百万个字符。8万个字符需要替换，
需要180秒才能完成替换:
for r in rs:
    txt=txt.replace(r,r[1])
所以大量的字符替换不能使用这个方法。
仅逐字扫描出1.3G的文件所有\n*就需要耗时一百40秒左右。
而使用正则替换完成处理则只需要一百50秒左右。
"""
