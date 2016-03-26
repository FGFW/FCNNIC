#julia product函数练习
#2016年3月23日 18:11:59 codegay

#Pkg.add("Iterators")
using Iterators

p=[r for r in 1:3]
@show p[1]
@show p[2:end]
prod=product(p[1],((p[2:end])))
for r in prod
@show r
end
result=[r for r in prod]
@show result
 [println(r) for r in product(1,3,4)]
 s=[r for r in product(1:2,22)]
 println(s)

 for r in 1:100

print("Download progress: $(r)%   \r")
flush(STDOUT)
end
run(`cmd /c pause`)