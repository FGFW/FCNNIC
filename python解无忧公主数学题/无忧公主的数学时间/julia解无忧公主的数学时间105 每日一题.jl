#="""
julia解无忧公主的数学时间105 每日一题.jl
https://mp.weixin.qq.com/s?__biz=MzI5ODEwMDQyNw==&mid=402334147&idx=1&sn=b4d7342f4375d832cceb4de4ee74ecb3
2016年3月30日 05:36:56 codegay
参考资料 https://www.wolframcloud.com/objects/01b74b78-aef6-4413-b140-108e40b2068c
"""=#
function ff1()
#105结果:T==8
#  4.396985 seconds (40.01 M allocations: 2.762 GB, 3.43% gc time)
#[Finished in 8.3s]
    for h in permutations([r for r in 0:9])
        f,o,r,t,y,e,n,s,i,x=h
        if length(Set(h))==length(h)
            forty=f*10000+o*1000+r*100+t*10+y
            ten=t*100+e*10+n
            sixty=s*10000+i*1000+x*100+t*10+y
            if forty+ten*2==sixty
                println("105结果:T==",t)
            end
       end
    end
end
@time ff1()