s1=input("enter s1:")
s2=input("enter s2:")
c=""
if len(s1)==len(s2):
    print("length is same")
for i in range(len(s2)):
    c=c+s1[i]+s2[i]
else:
    print("enter appropriate")
print(c)    
