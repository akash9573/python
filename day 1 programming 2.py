z=[]
x=int(input("enter the number of elements:"))
if x<=0:
    print("enter a positive number")
else:
    for i in range(1,x+1):
        n=int(input("enter the element:"))
        z.append(n)
    even=0
    odd=0
    for i in z:
        if(i%2==0):
            even=even+i**2
        else:
            odd=odd+i**2
    l=(even,odd)
print(l)
