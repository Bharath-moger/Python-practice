import argparse
import os
from hello import Account

BALANCE_FILE = "balance.txt"

def load_balance():
    if not os.path.exists(BALANCE_FILE) or os.path.getsize(BALANCE_FILE) == 0:
        save_balance(1000)
        return 1000
    with open(BALANCE_FILE, "r") as f:
        return int(f.read().strip())

def save_balance(balance):
    with open(BALANCE_FILE, "w") as f:
        f.write(str(balance))

def main():
    parser = argparse.ArgumentParser(description="Bank Account CLI Tool")

    subparsers = parser.add_subparsers(dest="command", help="Available commands")

    # Check balance
    subparsers.add_parser("status", help="Check bank account status")

    # Deposit
    deposit_parser = subparsers.add_parser("deposite", help="Deposit money")
    deposit_parser.add_argument("amount", type=int, help="Amount to deposit")

    # Withdraw
    withdraw_parser = subparsers.add_parser("withdraw", help="Withdraw money")
    withdraw_parser.add_argument("amount", type=int, help="Amount to withdraw")

    args = parser.parse_args()

    account = Account(load_balance())

    # Run commands
    if args.command == "status":
        account.bankStatus()
    elif args.command == "deposite":
        account.deposite(args.amount)
    elif args.command == "withdraw":
        account.withdraw(args.amount)
    else:
        parser.print_help()

    save_balance(account.balance)

if __name__ == "__main__":
    main()
