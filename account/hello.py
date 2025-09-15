# CLI USING SYS MODULE
# import sys
# print("hello",sys.argv[1])

# CLI USING ARGSPARSE
# import argparse

# parser = argparse.ArgumentParser(description="Demo Cli")
# parser.add_argument("--name",required=True,help="name")
# args = parser.parse_args()
# print(f"hello {args.name}")

# CLI USING LIBRARY TYPER
# import typer

# def greet(name: str):
#     print(f"Hello {name}")

# if __name__ == "__main__":
#     typer.run(greet)


# import sys
# def main():
#     if len(sys.argv) > 1:
#         name = sys.argv[1]
#         print(f"Hello, {name}!")
#     else:
#         print("Hello, World!")

# if __name__ == "__main__":
#     main()

class Account:
    def __init__(self,balance):
        self.balance = balance
        self.status = "sufficient balance"
    
    def withdraw(self,amt):
        if amt <= 0:
            print(f"You Entered {amt} amount is not valid")
            self.balance = self.balance-amt
        elif self.balance > amt:
            print(f"withdrawal succesfully of rupess {amt}")
        else:
            print(f"Insufficient balance to withdrawal")
    def deposite(self,amt):
        if amt <= 0:
            print(f"You Entered {amt} amount is not valid")
        else:
            self.balance+=amt
            print(f"deposite succesful of rupess {amt}")
    
    def bankStatus(self):
        if self.balance > 0:
            self.status = "sufficient balance"
        else:
            self.status = "Insufficient balance";
        print(f"Your Bank account has {self.status} of rupees {self.balance}")

# account = Account(100)
# obj.bankStatus()
# obj.withdraw(300)
# obj.bankStatus()
# obj.deposite(500)
# obj.bankStatus()

   


