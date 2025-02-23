class Account:
    def __init__(self):
        self._balance = 0

    @property  #getter
    def balance(self):
        return self._balance
    

    def deposite(self, n):
        self._balance += n

    
    def withdrow(self, n):
        self._balance -= n


def main():
    account = Account()
    print("Balance: ", account.balance)
    account.deposite(100)
    account.withdrow(50)
    print("Balance: ",account.balance)


if __name__ == "__main__":
    main()
