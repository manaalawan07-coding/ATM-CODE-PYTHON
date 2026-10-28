print("welcome to ATM")

balance = 100

run_code = True

while run_code:

    options = ["1.show balance", "2.withdraw", "3.deposit"]
    print(options)

    ask = int(input("Choose your options from 1-3: "))


    match ask:

        case 1:
              print(f"this is your balance: {balance}")
              more = input("would you like to continue ")
              if more == 'YES':
                   run_code = True
              else:
                run_code = False
        case 2:
              cash =  int(input("how much cash you want to withdraw"))
              balance = cash - balance
              print(balance)
              more = input("would you like to continue ")
              if more == 'YES':
                   run_code = True
              else:
                    run_code = False
        case 3:
              money = int(input("how much money u want to deposit into ur bank account"))
              balance = balance + money
              print(balance)
              more = input("would you like to continue ")
              if more == 'YES':
                     run_code = True
              else:
                      run_code = False


print("Thank You !!")


        




    


      
      
     
                 
