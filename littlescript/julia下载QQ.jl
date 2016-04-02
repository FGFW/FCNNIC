#="""
julia下载QQ.jl
从http://im.qq.com/pcqq/页面中提取出QQ的下载地址,并下载.
2016年4月1日 19:16:15 codegay
"""=#
url=string("http://im.qq.com/pcqq/","?",time())
download(url,"qq.html")
f=open("qq.html")
txt=readall(f)
m=matchall(r"(?P<test>http://.*?.exe)",txt)
fn=split(m[1],"/")
download(m[1],fn[end])
