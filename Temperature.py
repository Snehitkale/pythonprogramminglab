import easy gui
import sys
input temp=enterbox("enter temperature")
input_temp=float(input temp)
a=choicebox(msg="please select choice you want in units",title="temp conversations",choices=["celcius","farenheit"])
if a=="celcius":
     celcius temp=(input_temp-32)/1.8
      msgbox(" Your required temperature is +celcius temp+ "Celcius")
elif a=="farenheit":
          farenheit temp=(input_temp*1.8  )+32   
          msgbox("Your required temperature is"+farenheit temp+"Farenheit")

