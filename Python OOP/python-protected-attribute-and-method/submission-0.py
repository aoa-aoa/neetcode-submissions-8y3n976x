class Account:
    def __init__(self,title:str,amount:int):
        self.title = title
        self._amount = amount
    
    def display_balance(self) -> None:
        print(f"Balance: ${self._amount}")


# Do not modify the code below this line
account = Account("John", 1000)
account.display_balance()
