"""
python个位数统计.py
http://www.nowcoder.com/questionTerminal/a2063993dd424f9cba8246a3cf8ef445
codegay 2016年4月1日 11:02:20
"""
def ff1(n):
    kv={k:str(n).count(k) for k in set(str(n))}
    [print(r,":",kv[r]) for r in sorted(kv.keys())]
ff1(24242424567)