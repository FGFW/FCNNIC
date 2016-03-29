"""
julia生成指定格式的字符串-优化2.jl
http://bbs.bathome.net/thread-39829-1-1.html
2016年3月29日 05:06:07 codegay
"""
#生成aabbcc格式的字符串

ss="abcdefghijklmnopqrstuvwxyz0123456789"
result=open("result.txt","w+")
#方法1 
function ff1()
#julia多层for 迭代可以写成一行
    for a in ss,b in ss,c in ss
            s=string(a,a,b,c,b,c,"\r\n")
            write(result,s)
            #@show s
    end
    #[Finished in 4.2s]
end

#方法2 使用Iterators库的product
using Iterators
function ff2()
#参考资料 https://www.zhihu.com/question/36049062/answer/65775426
list=[ss,ss,ss]
    for r in product(list...)
        write(result,string(r[1],r[1],r[2],r[3],r[2],r[3],"\r\n"))
        #@show string(r[1],r[1],r[2],r[3],r[2],r[3],"\r\n")
    end
    #[Finished in 5.6s] #time   0.287181 seconds (1.16 M allocations: 37.426 MB, 17.36% gc time)
end
@timev ff2() 

close(result)
