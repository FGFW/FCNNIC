sf=open("test.txt","rb")
txt=sf.read()
time=5

def rw(txt,time):
    for t in range(0,time):
        fn="F%05d" % t+".txt"
        open(fn,"wb").write(txt)

rw(txt,time)
