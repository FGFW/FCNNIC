#=julia排除目录调用命令备份文件.jl
2016年3月15日 16:54:34 codegay

julia是一门很年轻的科学计算语言，
综合很了很多语言的特性，号称有很好的性能。
灵活，上手快，这门语言将来应用范围可能比较广。
=#

d=readdir("d:/")
f=["快盘","AV","\$RECYCLE.BIN","temp","System Volume Information"]
#$是特殊字符，需要加\转义

#使用filter过滤排除目录
for r in f
  d=filter(x -> x!=r,d)
end

#使用run（）执行命令
[run(`cmd /c copyw.exe "$r" g:/备份`) for r in d]
