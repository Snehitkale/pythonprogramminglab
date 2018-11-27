def arm(x) :
    sum=0
    t=x
    while(t>0):
         d=t%10
 	 sum+=d**3
 	 t=t//10
    if sum==x:
       print("armstrong number")
    else:
       print("not a armstrong number")	

