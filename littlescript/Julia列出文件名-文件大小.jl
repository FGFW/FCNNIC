#Julia列出文件名-文件大小.jl
#http://bbs.bathome.net/thread-39660-2-1.html
#julia 版 codegay 2016年3月13日 13:35:54
for r=readdir()
    f=stat(r).size
    println("文件名:$r $f  字节");
end