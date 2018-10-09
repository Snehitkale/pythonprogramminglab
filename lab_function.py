def armn(x):                                #define a function
 sum=0                                      #then assign variables for values   
 t=x                                        #using while loop assign a condition
 while(t>0):                                #using a variable d assign a condition of input number to it
       d=t%10                               #then use the if....else function to get the output
       sum+=d**3                            #using return function and print the code.
       t=t//10
 if sum==x:
    return "amstrong number"
 else:
    return "not an amstrong number"


x=int(input("enter number"))
print(armn(x))
