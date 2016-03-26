"""
python字典列表写入csv.py
http://stackoverflow.com/questions/36186513/write-a-dictionary-of-lists-to-csv-in-python
2016年3月24日 03:09:59 codegay
"""

d={'a': [1, 2, 3],'b': [4, 5, 6], 'c': [7, 3, 2]}
with open("result.txt","w+") as f:
    for k,v in d.items():
            alist=[k]+[str(r) for r in v]#alist=['a','1','2','3']
            line=' '.join(alist)+"\n"#line="a  1 2 3\n"
            f.write(line)
            
