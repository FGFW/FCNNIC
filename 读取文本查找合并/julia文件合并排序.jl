"""
julia文件合并排序.jl
http://bbs.bathome.net/thread-39841-1-1.html
2016年3月29日 17:29:48 codegay
思路如crlf所说,找出不存target中id,合并然后sort排序就可以.
"""

indexio=open("index2.txt")
targetio=open("target2.txt")
indtxt=[strip(r) for r in readlines(indexio)]
#@show indtxt
tartxt=readlines(targetio)
tarind=[split(r)[1] for r in tartxt]
#@show tarind
notin=filter(x -> !(x in tarind),indtxt)
@show notin
notin=[string(r,"\r\n") for r in notin]
#@show sort([tartxt;notin])
result=open("out.txt","w+")
write(result,sort([tartxt;notin]))

close(indexio)
close(targetio)
close(result)
#[Finished in 4.3s]