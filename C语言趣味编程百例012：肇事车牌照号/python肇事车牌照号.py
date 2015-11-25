"""
python计算肇事车牌照号
http://www.bathome.net/thread-16242-1-1.html
依山居 4:28 2015/11/25
"""
#方法1 思路是先生成所有的aabb和aaaa的数字组合.再判断乘方结果是否在其中。没有判断a!=b，但是能出结果...
aabb=[str(r)+str(r)+str(s)+str(s) for r in range(1,10) for s in range(1,10)]
[print("号码:",r*r) for r in range(1,100) if (str(r*r) in aabb)]
#上一种方法的改进，排除a=b，不再使用类型转换
aabb=[r*1000+r*100+s*10+s for r in range(1,10) for s in range(1,10) if (r!=s)]
[print("号码:",r*r) for r in range(1,100) for ab in aabb if r*r==ab]

print(aabb)
#方法2 不以结婚为目的地把代码写成一行就是耍流氓
print("号码：",[r*r for r in range(1,100) if ((r*r>999) and (r*r<10000) and (int(r*r/1000)==int(r*r/100%10) and int(r*r/1000)!=int(r*r/10%10) and int(r*r/10%10)==r*r%10))])
[print("号码:",r*r) for r in range(1,100) if ((r*r>999) and (r*r<10000) and (int(r*r/1000)==int(r*r/100%10)!=int(r*r/10%10) and int(r*r/10%10)==r*r%10))]


"""
输出:
号码: 7744
号码： [7744]
"""
