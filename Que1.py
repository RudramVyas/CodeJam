#Question 1

T=input()
T=int(T)
for i in range(0,T):
    N=input()
    N=int(N)
    dg=0
    cr=0
    cc=0
    mx=[]
    chk=[]
    for j in range(1,N+1):
        chk.append(j)
    for j in range(0,N):
        sr=[]
        l=input()
        l=l.split()
        mx.append(l)
        dg+=int(l[j])
        for k in l:
            sr.append(int(k))
        sr.sort()
        if(sr!=chk):
            cr+=1;
    for j in range(0,N):
        sc=[]
        for k in range(0,N):
            sc.append(int(mx[k][j]))
        sc.sort()
        if(sc!=chk):
            cc+=1;
    print('Case #%d:'%(i+1),dg,cr,cc)