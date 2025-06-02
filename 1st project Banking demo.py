balance=10



def user():
    print("Hello! Welcome to demo of banking service.\n")
    
    while True:
        user_name = input("Enter your name please: ")
        if user_name.isalpha():
            print(f"Hi! {user_name}\n")
            break
        else:
            print("Enter your real name! \n")
    return user_name

def pin():
    count = 0
    while True:
        code = (input("Enter your Pin! "))
        if code.isdigit():
            code=int(code)
            if code == 1234:
                print("Log in sucessfully! \n")
                return True
            else:
                print("Wrong pin")
                count+=1
                if count ==3:
                    print("Too many failed attempts. Restarting...\n")
                    return False 
        else:
            print("Only numbers allowed! ")
            

def acc_info(name,balance):
    print("Info: ")
    print("Name = ", name)
    print("Account no = 0041-4589-54568")
    print(f"Amount = ${balance}")
    print("Address = California\n")
    qom(name,balance)
    

def balcheck(name,balance):
    print(f"You have ${balance} in your account\n")
    qom(name,balance)
    

def deposit(name,balance):
    print("Hi! sir")
    while True:
        input_sum=input("How much sum you want to Deposit? $")
        print()
        if input_sum.isdigit():
            input_sum=int(input_sum)
            break
        else:
            print("Please enter the number not letters\n")
        
    
    balance = balance + input_sum
    print(f"${input_sum} is deposited.")
    print(f"Your new balance is ${balance}\n")
    qom(name,balance)
    return balance

def withdraw(name,balance):
    print("Hi! sir")
    print(f"Your Balance is {balance}")
    while True:
        input_sum=input("How much sum you want to Withdraw? $")
        print()
        if input_sum.isdigit():
            input_sum=int(input_sum)
            break
        else:
            print("Please enter the number not letters\n")
            print(f"Your Balance is {balance}")
    
            
    while True:
        if balance >= input_sum:
            balance = balance - input_sum
            print("Withdrawing...")
            print(f"Your new balance is ${balance}\n")
            qom(name,balance)
            break
        else:
            print(f"You have ${balance}. You cannot withdraw ${input_sum}.\n")
            while True:
                ask=input("Press 0 for exit. 1 for menu. 2 for retry. ")
                if ask.isdigit():
                    ask=int(ask)
                    if ask in [0,1,2]:
                            if ask==0:
                                quit()
                            elif ask==1:
                                menu(name,balance)
                                break
                            elif ask==2:
                                withdraw(name,balance)
                                break
                    else:
                        print("Enter the valid number! \n")
            
            
    return balance
    
    
        
def menu(name,balance):
    print("You can perform following activies: ")
    print("Click 1 for account info")
    print("Click 2 for Balance check")
    print("Click 3 for Deposit")
    print("Click 4 for Withdraw")
    print("Click 5 for exit\n")
    
    while True:
        command = input("Enter the number! ")
        print()
        if command.isdigit():
            command = int(command)
            if command in [1,2,3,4,5]:
                break
            else:
                print("Enter the valid number")
        
        else:
            print("Only number is valid!")
            
    while True:
        if command == 1:
            acc_info(name,balance)
            break
        elif command == 2:
            balcheck(name,balance)
            break
        elif command == 3:
            balance=deposit(name,balance)
            break
        elif command == 4:
            balance=withdraw(name,balance)
            break
        elif command == 5:
            quit()
        else:
            print("Enter the valid number:\n" )
            
def qom(name,balance):
    while True:
        x = input("Enter 0 for exit or 1 for menu: ")
        if x.isdigit():
            x = int(x)
            if x in [1, 0]:
                break
            else:
                print("1 or 0")
        else: 
            print("Only 0 and 1 are valid\n")
    
    if x == 0:
        quit()
    else:
        menu(name,balance)

        
            
def quit():
    print("Closing...")
    exit()
                
    
    
def main():
    
    
    while True:
        name = user()
        if pin():
            break 
    menu(name,balance)

    
    
       
main()