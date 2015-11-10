
#python字符串切片,拼接字符串处理文本.py
#依山居  17:40 2015/11/10
#题目来源： http://www.bathome.net/thread-38085-1-1.html

#相关资料：Python 序列的切片操作与技巧
#http://www.cnblogs.com/ifantastic/archive/2013/04/15/3021845.html

out=open("out.txt","a+")#处理结果将以追加的模式输出到这个文件。

tdstr="UJ137000000001560000000"

with open("test.txt") as f:
    for l in f:
        line=l.rstrip() #统一去掉行尾回车换行符，这样可以比较方便直接截取到后四位2799。
        line=line[1:17]+tdstr+","+line[-4:]+","+line[1:5]+" "+line[5:9]+" "+line[9:13]+" "+line[13:17]+"\n"
        out.write(line) #结果写入文件
        print(line)
out.close()
