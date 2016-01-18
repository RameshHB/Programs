for letter in 'python':
    print 'Current Letter:',letter

fruits = ['banana','apple','mango']
for fruit in fruits:
    print 'Current fruit:', fruit

print "Good bye!"

for num in range(10,20):
   for i in range(2,num):
       if num%i == 0:
          j=num/i
          print '%d equals %d * %d' %(num,i,j)
	  break
       else:
         print num,'is a prime number'

i = 2
while(i < 100):
   j = 2
   while(j <= (i/j)):
     if not(i%j): break
     j = j + 1
   if(j > i/j) : 
    print i, " is prime"
   i = i+1

print "Good bye!"
