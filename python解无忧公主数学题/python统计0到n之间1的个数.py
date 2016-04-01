"""
python统计0到n之间1的个数.py
http://www.acmerblog.com/count-ones-6202.html
codegay 2016年4月1日 09:08:10
傻傻暴力算
"""
def ff1(n):
    #数字转成字符串,然后统计字符串的数量,最后sum相加得到结果
    result=sum([str(r).count("1") for r in range(n+1)])
    print(result)
    return result
ff1(99999999)
#80000000
#[Finished in 56.1s]
