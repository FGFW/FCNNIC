import shutil
sf="test.txt" 
time=5
def shutilcp(sf,t):
    for t in range(1,t,1):
        fn="F%05d" % t + ".txt"
        shutil.copyfile(sf,fn)
shutilcp(sf,time)
