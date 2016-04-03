#=
julia统计0到n之间1的个数.jl
codegay 2016年4月1日 09:29:23
写个julia版和python对比下时间
参考资料:http://www.cnblogs.com/lazycoding/archive/2011/04/08/count-one.html
↑↑↑论算法的重要性
=#
function ff1(n)
result=[length(split(string(r),"1"))-1 for r in 0:n]
#juia群254087649的曲晓峰同志提供的方法
result=sum(result)
println(result)
return result
end
ff1(99999999)
#没有找到julia像python count那样直接统计某个字符串数量的方法,吐槽!
#80000000
#[Finished in 24.5s] python版是56s


function ff2(n)
result=[count(x->x==1,digits(r,10)) for r in 0:n]
#参考手册:digits()可以把数字变成可以迭代的数组.
result=sum(result)
println(result)
return result
end
#ff2(99999999)
#julia0.4.3:
#80000000
#[Finished in 44.7s]
#julia0.4.5
#80000000
#[Finished in 43.2s]

function ff3(n)
result=[count(x->x=='1',string(r)) for r in 0:n]
#juia群254087649的水牛同志提供的方法
result=sum(result)
println(result)
return result
end
#ff3(99999999)
#julia0.4.3:
#80000000
#[Finished in 30.3s]
#julia0.4.5:
#80000000
#[Finished in 36.0s]
