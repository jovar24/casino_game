money_in_wallet = []
def roullete():
    def deposit():
        cash = input("Welcome to roulette to start enter amount of cash:  ")
        money_in_wallet.append(int(cash))    
        print (f"your current balance is ${float(sum(money_in_wallet)):.2f}")

    def bet():
        minus = input("what is the amount you would like to bet?:  ")
        print(f"${minus}")

    def guess():
        import random
        random_num = random.randrange(0,12)
        choice =input("what is the number you would like to place your bet on? number must be between 0 and 11 ")    
        print (f"${choice} that is a great choice spinning the wheel now.....")
        if random_num == choice:
            print(f"${random_num}")
            you_won()
        elif random_num != choice:
            print(f"${random_num}")
            you_lose()

    def you_won():
        print("you won!!!")
        money_in_wallet.append(int(minus))
        print (f"your current balance is ${float(sum(money_in_wallet)):.2f}")

    def you_lose():
        print("you lost :(")
        money_in_wallet.append(int(minus)) 
        print (f"your current balance is ${float(sum(-money_in_wallet)):.2f}")            

    

        