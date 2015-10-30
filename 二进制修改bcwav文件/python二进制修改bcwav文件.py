#python二进制修改bcwav文件

# 批处理BAT以十六进制方式修改文件内容
# http://www.bathome.net/thread-37858-1-1.html

# 相关: Nintendo 3DS Banner Wave / .BCWAV file format
# https://gbatemp.net/threads/nintendo-3ds-banner-wave-bcwav-file-format.320705/

# python str与bytes之间的转换
# http://blog.csdn.net/yatere/article/details/6606316

import os
#方法一 只处理单个文件
#"r+b"选项开启二进制读写文件模式
f=open("01.bcwav","r+b")
f.seek(9)#指针移动到这个位置进行写操作会覆盖这个地址的数据。
f.write(b'\x00')
f.close()

#方法二 历遍当前目录批量处理
extension=".bcwav" #需要处理的文件后缀

for l in os.listdir(): #默认仅list当前目录
    l=l.lower()
    #把文件名转成小写进行判断
    lext=os.path.splitext(l)
    if extension in lext[1] and os.path.isfile(l):
        f=open(l,"r+b")
        f.seek(9)
        f.write(b'\x00')
        f.flush()
        f.close()
        print(l,"文件已经修改")



        
        
  
    
   
    

