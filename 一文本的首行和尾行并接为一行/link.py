f=open("a.txt","r")
txt=f.readlines()
f.close()
l=txt[0].rstrip()+txt[-1]
print(l)
