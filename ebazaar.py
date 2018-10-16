msgbox("Hello, everyone")
 msg ="What are you looking for?"
    title = "e-baazar"
    choices = ["Furniture", "Cosmetics", "Electronics", "Home Appliances","Fashion", "Sports Accessories"]
    choice = choicebox(msg, title, choices) 
 msgbox("You chose: " + choices, "Choice Result")


if choices==furniture:
 msg ="here are some great deals"
    title = "best furniture options"
    choice1 =["Chairs","Dining Tables","Study Tables","Benches"]
 msgbox("You chose: " + choice1, "Choice Result")
elif choices==Cosmetics:
  msg ="here are some great deals"
     title = "best cosmetics options"
     choice2 =["Deodrants", "Fairness creams", "Talcum Powder","Soaps"]
