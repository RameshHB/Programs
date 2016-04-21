var1=100
if var1:
   print("1 - Got a true expression value")
   print var1

var2=0
if var2:
   print("2 - Got a true expression value")
   print var2
print "Good bye!"

var=100
if(var == 100): 
   print ("Value of expression is 100")
print ("Good bye!")

#import pdb;
#pdb.set_trace()
amount=int(input("Enter the Amount1: "))
if amount<1000:
   discount=amount*0.05
   print ("Discount", discount)
else:
   discount=amount*0.10
   print("Discount", discount)
print ("Net payable:", amount-discount)

#import pdb;
#pdb.set_trace()
amount=int(input("Enter the Amount2: "))
if amount<1000:
   discount=amount*0.05
   print("Discount:", discount)
elif amount<5000:
     discount=amount*0.10
     print("Discount:", discount)
else:
   discount=amount*0.15
   print("Discount:", discount)
print("Net payable:", amount-discount)

import pdb; pdb.set_trace()
num=int(input("Enter the number:"))
if num%2==0:
   if num%3==0:
      print("Divisible by 2 and 3")
   else:
      print("Divisible by 2 not divisible by 3")
else:
   if num%3==0:
      print("Divisible by 3 not divisible by 2")
   else:
      print("not divisible by 2 not divisible by 3")
