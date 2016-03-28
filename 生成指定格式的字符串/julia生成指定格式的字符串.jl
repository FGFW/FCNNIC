"""
julia生成指定格式的字符串.jl
http://bbs.bathome.net/thread-39829-1-1.html
2016年3月29日 05:06:07 codegay
"""
#生成aabbcc格式的字符串
ss="abcdefghijklmnopqrstuvwxyz0123456789"
result=open("result.txt","w+")
for a in ss
    for b in ss
        for c in ss
            for d in ss
                for e in ss
                    for f in ss
                        if a==b&&c==e&&d==f
                            s=string(a,a,c,d,e,f,"\r\n")
                            write(result,s)
                            #@show s
                        end
                    end
                end
            end
        end
    end
end
close(result)

#[Finished in 369.3s]
