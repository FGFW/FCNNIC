#=
julia替换TND.jl
http://bbs.bathome.net/thread-2462-1-1.html
2016年4月1日 06:18:12 codegay
=#
txt=open(readall,"test.txt")
txt=replace(txt,"他娘的","TND")
println(txt)
txt=replace(txt,"TND","")
print(txt)