class mpesaAccount(object):
    def deposit(self, amount):
        pass
    def withdraw(self, amount):
        pass

    def _init_(self, holder, number, balance):
        self.holder = holder
        self.number = number
        self.balance = balance

class mshwari(mpesaAccount):
    def _init_(self)
    self.balance = 1000

    def deposit(self, deposit):
        if type(deposit) == int and deposit >= 1:
            self.balance +=deposit
            return self.balance
        else:
            return'Failed transaction'

    def withdraw(self,amount):
        if type(amount) == int and amount > 0:
            if (self.balance - amount) > 0:
            if (self.balance - amount) > 1000:
                self.balance -=amount
                return self.balance
            else:
                return 'Failed' 
