"""
python解无忧公主的数学时间编程题002.py
http://mp.weixin.qq.com/s?__biz=MzI5ODEwMDQyNw==&mid=402648727&idx=4&sn=4eb3c8692db7d51bdc123d52aa236603&3rd=MzA3MDU4NTYzMw==&scene=6#rd
2016年3月31日 07:08:35 codegay
参考资料 http://www.mathblog.dk/project-euler-34-factorial-digits/
题目:
145 is a curious number, as 1! + 4! + 5! = 1 + 24 + 120 = 145. 
Find the sum of all numbers which are equal to the sum of the factorial of their digits. 
Note: as 1! = 1 and 2! = 2 are not sums they are not included.
"""
from itertools import permutations
