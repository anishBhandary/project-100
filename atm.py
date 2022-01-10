class Atm:
    def __init__(self , cardnumber , pin) :
        self.cardnumber = cardnumber
        self.pin = pin


    def check_balance(self) :
        print("balance is 50,000")

    def withdrawl(self,amount) :
        new_amount = 50000 - amount
        print("amount is withdrawed"+str(amount)+"your remaining balance is "+str(new_amount))

def main():
    cardnumber = input("insert your card number")
    pin = input("insert your pin number")

    new_user = Atm(cardnumber , pin)

    print("choose your options")
    print("1.Balance Enquiry 2.WithDrawl")

    option = int(input("enter the option"))

    if(option == 1):
        new_user.check_balance()
    

    elif(option == 2):
        amount = int(input("enter the amount"))
        new_user.withdrawl(amount)
    
    else:
        print("enter the valid number")

main()

