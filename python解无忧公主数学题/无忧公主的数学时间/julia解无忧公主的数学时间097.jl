#="""
julia解无忧公主的数学时间097.jl
http://mp.weixin.qq.com/s?__biz=MzI5ODEwMDQyNw==&mid=402225879&idx=1&sn=6ea8e1d5e6a2520ad65eb2713a98af6e&3rd=MzA3MDU4NTYzMw==&scene=6#rd
2016年3月29日 21:42:46 codegay
木有想法傻傻暴力算
"""=#
using Iterators
n=[r for r in 1:7]
f=x->length(Set(x))==5&&x[1]<x[2]>x[3]&&x[3]<x[4]>x[end];
result=[]
for r in filter(f,product(n,n,n,n,n))
push!(result,string(r))
end
lenresult=length(result)
println("097结果:$lenresult")
#097结果:336
#[Finished in 5.2s]