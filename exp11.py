import random
n=[]
s=0
c=0
l=sl=-1
s=ss=101
for i in range(20):
    a=random.randrange(1,100)
    n.append(a)
    s=s+n[i]
print(n)
avg=s/20;
print(avg)
for i in n:
    if i%2==0:
        c+=1
    if i>l:
        sl=l
        l=i
    elif i>l and i!=l:
        sl=i
    if i<s:
        ss=s
        s=i
    elif i<s and i!=s:
        ss=i
print(l,s,ss,sl)
print(c)

