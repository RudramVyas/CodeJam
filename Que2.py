#Question 2

T=int(input())
for i in range(0,T):
    s=list(input())
    cdp=0
    ans=[]
    for j in s:
        if(int(j)>cdp):
            for k in range(0,(int(j)-cdp)):
                ans.append('(')
                cdp+=1;
        elif(int(j)<cdp):
            for k in range(0,(cdp-int(j))):
                ans.append(')')
                cdp-=1;
        ans.append(int(j))
    for j in range(0,cdp):
        ans.append(')')
    ast=""
    for j in ans:
        ast+=str(j)
    print('Case #%d:'%(i+1),ast)