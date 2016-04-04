"""
python移动文本第A行到第N行.py
http://bbs.bathome.net/thread-39853-2-1.html
2016年4月4日 18:50:06 codegay
这个问题本质等于把列表元素第A个移动到第N....
"""
with open("22.txt") as f:
    txt=f.readlines()
    txt.insert(4,txt[1])#第二行插入第五行的位置
    del(txt[1])#删除原来的第二行
    print(txt)

#方法2
a=list("1234567")
a.insert(3,a.pop(1))#弹出第二行插入到第四行
print(a)