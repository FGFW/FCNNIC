# python版实现文本左右对齐排版
# 题目来源: http://www.bathome.net/thread-1246-1-1.html
# 依山居 7:17 2015/11/4

# str.format 字符串格式化参考：
# http://www.crifan.com/python_string_format_fill_with_chars_and_set_alignment/

# just()字符串对齐 参考：
# http://blog.csdn.net/u012515223/article/details/20463231
'''
1.txt内容：
111111111111111111111    98912 张三
222222222222222222    150020 李四四
  333333333333333333333    360000 王五
444444444444444444    2332 赵六六
  555555555555555555    222 田七
666666666666666666666    999999 舞吧
'''

#说明我的代码没按题目要求全部使用空格填充是为了让代码用法看起来直观一些。

#方法一 format格式化对齐
def f1():    
    with open("1.txt","r") as f:
        for s in f:
            l=s.rsplit ()
            t='{0:-<25} {1: >7} {2}'.format(l[0],l[1],l[2])    
            print(str(t))

'''
输出:
111111111111111111111----   98912 张三
222222222222222222-------  150020 李四四
333333333333333333333----  360000 王五
444444444444444444-------    2332 赵六六
555555555555555555-------     222 田七
666666666666666666666----  999999 舞吧
'''

#方法2 使用just()对齐
r=''
def f2():
    f=open("1.txt","r")
    for s in f:
        l=s.rsplit()
        print(l[0].ljust(25," "),l[1].rjust(10,"^"),l[2])

'''
输出：
111111111111111111111     ^^^^^98912 张三
222222222222222222        ^^^^150020 李四四
333333333333333333333     ^^^^360000 王五
444444444444444444        ^^^^^^2332 赵六六
555555555555555555        ^^^^^^^222 田七
666666666666666666666     ^^^^999999 舞吧
'''

#方法3
'''
思路是rsplit拆分成三列,l得到如['111111111111111111111', '98912', '张三']
算出列1,列2的最长，以此算出需要填充的长度，
'''
def f3():
    f=open("1.txt","r")
    txt=f.readlines()
    maxa=0
    maxb=0
    for line in txt:
        line=line.rsplit()
        la=len(line[0])
        lb=len(line[1])
        if la >maxa:
            maxa=la
        if lb > maxb:
            maxb=lb

    for line in txt:       
        line=line.rsplit()
        la=len(line[0])
        lb=len(line[1])
        if la ==maxa:
            tla=line[0]
        elif la<maxa:
            tla=line[0]+">"*(maxa-la)
        if lb ==maxb:
            tlb=line[1]
        elif lb<maxb:
            tlb=" "*(maxb-lb)+line[1]
        print(tla,tlb,line[2])
'''
输出：
111111111111111111111  98912 张三
222222222222222222>>> 150020 李四四
333333333333333333333 360000 王五
444444444444444444>>>   2332 赵六六
555555555555555555>>>    222 田七
666666666666666666666 999999 舞吧
'''
"""
#方法4 重用了方法3的上半部分代码算出列1列2最大长度，以此对齐顶点。
#这个方法的思路是不使用空格或者其它符号填充，而是在写入文件时，
#指针直接前移使字符对齐。空的字符位置会自动被\x00填充？
#
"""
def f4():
    
    f=open("1.txt","r")
    txt=f.readlines()
    maxa=0
    maxb=0
    for line in txt:
        line=line.rsplit()
        la=len(line[0])
        lb=len(line[1])
        if la >maxa:
            maxa=la
        if lb > maxb:
            maxb=lb

    w=open("temp.txt","w+")
    for line in txt: 
        line=line.rsplit()
        la=len(line[0])
        lb=len(line[1])
        w.write(line[0])
        #算出空白区域长度，指针跳过空白区再写入第二列。
        tw=maxa+maxb+1-la-lb
        w.seek(tw+w.tell())
        w.write(line[1])
        w.seek(w.tell()+1)
        w.write(line[2]+"\n")
    w.flush()
    w.seek(0)
    txt=w.read()
    print(txt)


