a=["inches","yards","miles","milli","centi"]
for i in range(len(a)):
    print(i,"-",a[i])
f=int(input("length in feet:")
g=int(input("enter choice:"))      
match g:
    case 0:
      print(f*12,"inches")
    case 1:
      print(f/3,"yards")
    case 2:
      print(f/5280,"miles")
    case 3:
      print(f*304.8,"milli")
    case 4:
      print(f*30.48",centi")  
