#=
julia统计0到n之间1的个数.jl
codegay 2016年4月1日 09:29:23
写个julia版和python对比下时间
=#
function ff1(n)
result=[length(split(string(r),"1"))-1 for r in 1:n]
result=sum(result)
println(result)
return result
end
ff1(99999999)
#没有找到julia像python count那样直接统计某个字符串数量的方法,吐槽!
#80000000
#[Finished in 24.5s] python版是56s