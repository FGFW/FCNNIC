#="""
julia文本文件合并去重.jl
http://bbs.bathome.net/thread-39822-1-1.html
2016年3月27日 01:02:58 codegay
"""=#
f1=open("1.txt")
txt1=readlines(f1)
txt2=readlines(open("2.txt"))
txt=vcat(txt1,txt2) #以readlines取读文件流,vcat连接两个Array,julia不支持+号连接字符串和数组,支持$符内插
@show length(txt)
result=unique(txt) #内置函数unique去重
#result=Set(txt) Set()方法把数组转为集合,集合中的元素唯一,Set是首字母大写的!
@show length(result)
write(open("result.txt","w+"),result) #与python不同,julia把数组写入文件不需要wirtelines

#装B代码一行流
write(open("result.txt","w+"),unique(vcat(readlines(open("1.txt")),readlines(open("2.txt")))))

#julia管道一行流
union("1.txt"|>open|>readlines,"2.txt"|>open|>readlines)|>write("result.txt");
