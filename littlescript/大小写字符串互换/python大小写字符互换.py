"""
python大小写字符互换.py
http://www.bathome.net/thread-2740-1-1.html
依山居 4:47 2015/12/15
"""
s="sD8F8S88f899f9DiIujUUuj JhHUuH hH$%"
def fn(x):
    if x.islower():
        return x.upper()
    elif x.isupper():
        return x.lower()
    else:
        return x
result=''.join([fn(r) for r in list(s)])
print(result)

"""
输出:
Sd8f8s88F899F9dIiUJuuUJ jHhuUh Hh$%
"""
