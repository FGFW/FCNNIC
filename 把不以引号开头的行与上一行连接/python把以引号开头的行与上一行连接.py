
newtxt=[]
with open("a.txt") as f:
    txt=f.read().rsplit()
    rn=len(txt)
    for r in range(rn):
        if r+1<rn and r>0:
            if txt[r][0] == "\"":
                newtxt.append(txt[r-1]+txt[r])
            else:
                newtxt.append(txt[r])
        else:
            newtxt.append(txt[r])

print(newtxt)
    
