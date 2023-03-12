class user:
    def __init__(self,name,email,balance):
        self.name=name
        self.email=email
        self.account_balance=balance 
        
    def withdrawal(self,amount):
        self.account_balance -=amount
        return self
        
    def deposit(self,amount):
        self.account_balance+=amount
        return self

    def transfer_money(self, other_user, amount):
        self.account_balance -=amount
        other_user.account_balance+=amount
        return self

    def display_user_balance(self):
        print(self.account_balance)
        return self

mahdi=user('mahdi','mahdi.saqqa@gmail.com',200)

mussa=user('mussa','mussa.yamak@gmail.comn',600)

hussam=user('husssam','hussam@gmail.com',4000)


mahdi.deposit(400).deposit(700).deposit(1200).withdrawal(2000).display_user_balance()

mussa.deposit(700).deposit(40000).withdrawal(32000).withdrawal(4000).display_user_balance()

hussam.deposit(40000).withdrawal(2000).withdrawal(4000).withdrawal(12000).display_user_balance()

mahdi.transfer_money(hussam,800).display_user_balance()

hussam.display_user_balance()
