from easygui import *
import sys
while 1:
  msgbox("Hello, everyone")
  msg ="What are you looking for?"
  title = "e-baazar"
  choices = ["Furniture", "Electronics", "Home Appliances","Fashion","Other"]
  choice = choicebox(msg, title, choices) 
  msgbox("You chose: " + choice, "Choice Result")
  if choice== "Furniture":
    msg1 ="here are some great deals"
    title1 = "best furniture options"
    choice1 =["Chairs","Dining Tables","Study Tables"]
    choice1 =choicebox(msg1,title1,choice1)
    if choice1== "Chairs":
      msg11 ="available brands are"
      title11 ="brand analysis"
      choice11 =["pepperfry-RS 9,500","nilkamal-RS 11,999","forzza-RS 15,999"]
      choice11 =choicebox(msg11,title11,choice11)
      msgbox("you chose:" + choice1 +"of" + choice11)
      msg= "is it your final choice(press continue to order)
      title ="please confirm"
      msgbox("thank you for shopping") 
    elif choice1=="Dining Tables":
      msg11 ="available brands are"
      title11 ="brand analysis"
      choice11 =["forzzo- RS 33,249","deckup- RS 30,999","royaloak- RS 32,249"]
      choice11 =choicebox(msg11,title11,choice11)
      msgbox("you chose:" + choice1 +"of" + choice11)
      msg= "is it your final choice(press continue to order)
      title ="please confirm"
      msgbox("thank you for shopping") 
    elif choice1== "Study Tables":
      msg11 ="available brands are"
      title11 ="brand analysis"
      choice11 =["deckup- RS 5,999","hometown- RS 8,999","royaloak- RS 7,500"]
      choice11 =choicebox(msg11,title11,choice11)
      msgbox("you chose:" + choice1 +"of" + choice11)
      msg= "is it your final choice(press continue to order)
      title ="please confirm"
      msgbox("thank you for shopping") 
  if choice== "Electronics":
    msg1 ="which electronics do you want?"
    title1 ="your choice"
    choice1 =["phone","laptop","speaker"]
    choice1 =choicebox(msg1,title1,choice1)
 
    if choice1== "phone":
      msg11 ="available brands are"
      title11 ="phone brands"
      choice11 =["oneplus -RS 35,000","vivo -RS 24,000","mi redmi -RS 12,000"]
      choice11 =choicebox(msg11,title11,choice11)
      msgbox("you chose:" + choice1 +"of" + choice11)
      msg= "is it your final choice(press continue to order)
      title ="please confirm"
      msgbox("thank you for shopping")   



    elif choice1== "laptop":
      msg11 ="available brands are"
      title11 ="laptop brands"
      choice11 =["acer -RS 55,000","hp -RS 36,000","dell -RS 61,000"]
      choice11 =choicebox(msg11,title11,choice11)
      msgbox("you chose:" + choice1 +"of" + choice11)

      msg= "is it your final choice(press continue to order)
      title ="please confirm"
      msgbox("thank you for shopping") 


    elif choice1== "speaker":
      msg11 ="available brands are"
      title11 ="speaker brands"
      choice11 =["bosch -RS 10,000","i ball -RS 9000","skullcandy -RS 5000"]
      choice11 =choicebox(msg11,title11,choice11)
      msgbox("you chose:" + choice1 +"of" + choice11)
      
      msg= "is it your final choice(press continue to order)
      title ="please confirm"
      msgbox("thank you for shopping")  
  if choices== "Home Appliances":
    msg1 ="which appliance are you looking for?"
    title1 ="your choice"
    choices1 =["tv","oven","fridge"]
    choice1 =choicebox(msg1,title1,choice1)
 
    if choice1== "tv":
     msg11 ="available brands are"
     title11 ="brand analysis"
     choices11 =["samsung -RS 35,000","stark -RS 28,000","sony -RS 37,500"]
     choice11 =choicebox(msg11,title11,choice11)
     msgbox("you chose:" +  choice1 + "of" +  choice11 )
     msg= "is it your final choice(press continue to order)
      title ="please confirm"
      msgbox("thank you for shopping") 
    elif choice1== "oven":
     msg11 ="available brands are"
     title11 ="brand analysis"
     choices11 =["bajaj -RS 4000","kent -RS 3600","onida -RS 3500"]
     choice11 =choicebox(msg11,title11,choice11)
     msgbox("you chose:" + choice1 +"of" + choice11)
     msg= "is it your final choice(press continue to order)
      title ="please confirm"
      msgbox("thank you for shopping")   
    elif choice1== "fridge":
     msg11 ="available brands are"
     title11 ="brand analysis"
     choices11 =["bajaj -RS 10,000","godrej-RS 16,000","samsung -RS 14,000"]
     choice11 =choicebox(msg11,title11,choice11)
     msgbox("you chose:" + choice1 +"of" + choice11)
     msg= "is it your final choice(press continue to order)
      title ="please confirm"
      msgbox("thank you for shopping") 
     
  if choices== "Fashion":
    msg1 ="which trendy fashion are you looking for?"
    title1 ="fashion choice"
    choices1 =["shoes","watches","jeans"]
    choice1 =choicebox(msg1,title1,choice1)
    
    if choice1== "shoes":
     msg11 ="available brands are"
     title11 ="brand analysis"
     choices11 =["sparx -RS 4999","woodland -RS 7999","bata -RS 3800"]
     choice11 =choicebox(msg11,title11,choice11)
     msgbox("you chose:" + choice1 +"of" + choice11)
     msg= "is it your final choice(press continue to order)"
      title ="please confirm"
      msgbox("thank you for shopping") 
    elif choice1== "watches":
     msg11 ="available brands are"
     title11 ="brand analysis"
     choices11 =["rado -RS 6000","ucb -RS 3500","fastrack -RS 2000"]
     choice11 =choicebox(msg11,title11,choice11)
     msgbox("you chose:" + choice1 +"of" + choice11)
     msg= "is it your final choice(press continue to order)"
      title ="please confirm"
      msgbox("thank you for shopping") 
    elif choice1== "jeans":
     msg11 ="available brands are"
     title11 ="brand analysis"
     choices11 =["denim -RS 2000","ben martin -RS 1200","wrangler -RS 3500"]
     choice11 =choicebox(msg11,title11,choice11)
     msgbox("you chose:" + choice1 +"of" + choice11)
     msg= "is it your final choice(press continue to order)
      title ="please confirm"
      msgbox("thank you for shopping")    
   
if choices== "Other":
 exit(0);
