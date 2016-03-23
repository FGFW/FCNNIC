"""
python算无忧公主数学题109.py
2016年3月7日 06:19:56 codegay
http://python.jobbole.com/81213/

"""
from fractions import Fraction

a=[1-Fraction(1,2)]+[Fraction(1,r) for r in range(3,100+1)]

b=[Fraction(1,r) for r in range(50,99+1)]
print(b)
aa=sum(a)
bb=sum(b)
print(bb)
if aa>=bb:
    print("aa",aa,bb)
else:
    print("b",bb,aa)
    
