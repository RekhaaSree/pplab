a="hello,how are you today?"
b=a.split()
c=set()
print("after split",b)
for i in range(len(b)):
    c.update(b[i])
print(c)
print(" ".join(b))
