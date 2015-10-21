import string
lowercase=string.ascii_lowercase
uppercase=string.ascii_uppercase
f=open("a.txt","r")
def l2u():
    txt=f.read()
    for r in range(0,26,1):
        txt=txt.replace(lowercase[r],uppercase[r])
    return(txt)

def u2l():
    txt=f.read()
    for r in range(0,26,1):
        txt=txt.replace(uppercase[r],lowercase[r])
    return(txt)


#print(l2u())

print(u2l())
