def roullete():
    money_in_wallet = []
    bet = []
    def deposit():
        cash = input("Welcome to roulette to start enter amount of cash:  ")
        money_in_wallet.append(int(cash))    
        print (f"your current balance is ${float(sum(money_in_wallet)):.2f}")
        offer = input("what is the amount you would like to bet?:  ")
        bet.append(int(offer))
        

    def guess():
        import random
        random_num = random.randrange(0,12)
        choice =input("what is the number you would like to place your bet on? number must be between 0 and 11 ")    
        print (f"{choice} that is a great choice spinning the wheel now.....")
        if random_num == choice:
            print(f"{random_num}")
            you_won()
        elif random_num != choice:
            print(f"{random_num}")
            you_lose()

    def you_won():
        print("you won!!!")
        print (f"your current balance is ${float(sum(money_in_wallet)):.2f}")
        retry_win()
        
    def retry_win():
        decision = input("great job if you would like to bet again type \"again\" if you would like to cash out type \"done\" ")
        if decision == "again":
            bet()
        elif decision == "done":
            cashout()    

    def you_lose():
        print("you lost :(") 
        print (f"your current balance is ${float(sum(money_in_wallet)):.2f}")
        retry_lose()
    
    def retry_lose():
          decision = input("looks like you lost if you would like to bet again type \"again\" if you would like to cash out type \"done\" ")
        if decision == "again":
            bet()
        elif decision == "done":
            cashout()    
    def cashout():
        print(f"your current balance is ${float(sum(money_in_wallet)):.2f}") 
        quit
    
    deposit()
    guess()

roullete()    
        