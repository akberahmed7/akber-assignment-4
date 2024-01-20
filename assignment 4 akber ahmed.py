balance=int(input("enter your balance"))


while True:
   print("Welcome to ATM ")
   print("please select an option ")
   print("1:check your balance ")
   print("2:withdraw money")
   print("3:deposite money")
   print("4:exit")
option=(input("enter your option"))
if option == '1':
   print("print your balance",balance,"dollar")
elif option== '2' :
   Amount=float(input("enter withdraw"))
   if Amount > balance:
    print("unsufficient balance")
   else Amount == balance
    print("withdraw successful")
elif option =='3':
    Amount=float(input("enter deposite money"))
    balance==amount
    print("successfully deposite")
elif option =='4':
   print("thank you For using ATM")
   breakpoint
else:
   print("Invalid option.please try again")