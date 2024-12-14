s1=input("enter 1 string:")
s2=input("enter 2 string:")
ms=" "
l1=len(s1)
l2=len(s2)
for i in range(min(l1,l2)):
    
    ms+=s1[i]+s2[i]
if l1>l2:
    ms+=s1[l2:]
elif l2>l1:
    ms+=s2[l1:]
print("ms",ms)

    
