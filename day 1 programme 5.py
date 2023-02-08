a=float(input("enter the number of new breads purchased:"))
b=float(input("enter the number of old breads purchased:"))
c=a*185
d=b*185
f=float(d*40/100)
e=185
if(a<=0 and b<=0):
   print("enter a positive number")
else:
   print("regular price:",e)
   print("amount of new bread:",c)
   print("amount of old bread:",f)
   print("total price:",c+f)
      
