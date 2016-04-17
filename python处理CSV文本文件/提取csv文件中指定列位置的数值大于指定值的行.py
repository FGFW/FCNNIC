"""
提取csv文件中指定列位置的数值大于指定值的行.py
http://bbs.bathome.net/thread-40087-1-1.html
2016年4月17日 09:10:03 codegay
"""

import csv

with open("Inspection00002.txt",encoding="utf-8") as f:
    txt=csv.reader(f)

    with open("result.txt","w",encoding="utf-8") as csvw:
        result=csv.writer(csvw)
        result.writerow(['Chip No.', 'Chip ID', 'bump No.', 
            'Core No.', 'SRO', 'bump group', 'CAD X', 'CAD Y', 
            'X coordinate', 'Y coordinate', 'alignment', 
            'total height', 'plane height', 'bump height', 
            'bump coplanarity', 'bump caw', 'bump diameter', 'Judge'])#表头
        for r in txt:
            if "." in r[13] and float(r[13])>45:
                print(r)
                result.writerow(r)
"""
['7', 'A019', '1', '1', '0', '2', '-4152.32', '431.57', '-44147.51', '40431.56', '2.37', '108.95', '66.28', '56.67', '1.53', '-0.36', '46.41', 'OK  ']
['7', 'A019', '4', '1', '0', '2', '-4150', '-56.49', '-44144.57', '39941.83', '2.7', '108.66', '66.82', '55.84', '1.05', '0.06', '46.41', 'OK  ']
['7', 'A019', '9', '1', '0', '2', '-4150', '-710.21', '-44148.43', '39288.81', '3.04', '109.1', '67.33', '55.77', '1.19', '0.37', '47.24', 'OK  ']
['7', 'A019', '21', '1', '0', '1', '-4150', '-2279.12', '-44146.79', '37718.52', '3.44', '110.48', '66.99', '55.49', '1.92', '-0.38', '44.73', 'OK  ']
[Finished in 0.1s]
"""