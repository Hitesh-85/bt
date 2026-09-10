# py -3.12 -m venv venv
# venv\Scripts\activate
# python -m pip install web3
# python -m pip install eth-tester
# notepad wallet_shell.py


import cmd
from web3 import Web3

class Wallet(cmd.Cmd):
    intro = "Welcome to ClassCrypto! Type help for commands."
    prompt = "(crypto) > "

    def __init__(self):
        super().__init__()
        self.w3 = Web3(Web3.EthereumTesterProvider())

        a = self.w3.eth.accounts
        self.users = {
            "bank": a[0],
            "alice": a[1],
            "bob": a[2],
            "charlie": a[3]
        }

        print("Blockchain initialized with 4 users.")

    def do_balance(self, arg):
        user = arg.lower().strip()

        if user not in self.users:
            print("Invalid user!")
            return

        address = self.users[user]
        balance = self.w3.from_wei(
            self.w3.eth.get_balance(address), "ether"
        )

        print("User:", user.capitalize())
        print("Address:", address)
        print("Balance:", balance, "ETH")

    def do_send(self, arg):
        x = arg.split()

        if len(x) != 3:
            print("Usage: send <from> <to> <amount>")
            return

        sender, receiver, amount = x

        if sender not in self.users or receiver not in self.users:
            print("Invalid user!")
            return

        try:
            tx = self.w3.eth.send_transaction({
                "from": self.users[sender],
                "to": self.users[receiver],
                "value": self.w3.to_wei(float(amount), "ether"),
                "gas": 21000,
                "gasPrice": 0
            })

            receipt = self.w3.eth.wait_for_transaction_receipt(tx)

            print("Transaction successful!")
            print("Block:", receipt.blockNumber)
            print("Gas Used:", receipt.gasUsed)
            print("Transaction Hash:", tx.hex())

        except Exception as e:
            print("Transaction failed:", e)

    def do_chain(self, arg):
        block = self.w3.eth.get_block("latest")

        print("\n--- LATEST BLOCK ---")
        print("Block Number:", block.number)
        print("Block Hash:", block.hash.hex())
        print("Transactions:", len(block.transactions))

    def do_exit(self, arg):
        print("Exiting...")
        return True


if __name__ == "__main__":
    Wallet().cmdloop()


# python wallet_shell.py