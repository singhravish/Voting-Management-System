import hashlib
import json
from time import time

class Voter:
    def __init__(self, voter_id, name):
        self.voter_id = voter_id
        self.name = name
        self.has_voted = False


class Candidate:
    def __init__(self, candidate_id, name):
        self.candidate_id = candidate_id
        self.name = name

class Block:
    def __init__(self, index, timestamp, transactions, previous_hash):
        self.index = index
        self.timestamp = timestamp
        self.transactions = transactions
        self.previous_hash = previous_hash
        self.hash = self.calculate_hash()

    def calculate_hash(self):
        block_data = json.dumps({
            "index": self.index,
            "timestamp": self.timestamp,
            "transactions": self.transactions,
            "previous_hash": self.previous_hash
        }, sort_keys=True).encode()

        return hashlib.sha256(block_data).hexdigest()

class Blockchain:
    def __init__(self):
        self.chain = [self.create_genesis_block()]

    def create_genesis_block(self):
        return Block(0, time(), [], "0")

    def get_latest_block(self):
        return self.chain[-1]

    def add_block(self, transactions):
        previous_block = self.get_latest_block()

        new_block = Block(
            index=len(self.chain),
            timestamp=time(),
            transactions=transactions,
            previous_hash=previous_block.hash
        )

        self.chain.append(new_block)

    def is_chain_valid(self):
        for i in range(1, len(self.chain)):
            current = self.chain[i]
            previous = self.chain[i - 1]

         
            if current.hash != current.calculate_hash():
                return False

           
            if current.previous_hash != previous.hash:
                return False

        return True

    def print_chain(self):
        for block in self.chain:
            print("\n")
            print(f"Block Index: {block.index}")
            print(f"Timestamp  : {block.timestamp}")
            print(f"Transactions:")
            for tx in block.transactions:
                print(f"  Voter {tx['voter_id']} voted for Candidate {tx['candidate_id']}")
            print(f"Previous Hash: {block.previous_hash}")
            print(f"Hash         : {block.hash}")
            print("")


class VotingSystem:
    def __init__(self):
        self.voters = {}
        self.candidates = {}
        self.blockchain = Blockchain()

  
    def add_candidate(self):
        candidate_id = input("Enter Candidate ID: ")

        if candidate_id in self.candidates:
            print("Candidate ID already exists.")
            return

        name = input("Enter Candidate Name: ")

        self.candidates[candidate_id] = Candidate(candidate_id, name)

        print("Candidate added successfully.")

   
    def add_voter(self):
        voter_id = input("Enter Voter ID: ")

        if voter_id in self.voters:
            print("Voter ID already exists.")
            return

        name = input("Enter Voter Name: ")

        self.voters[voter_id] = Voter(voter_id, name)

        print("Voter added successfully.")



    def cast_vote(self):
        voter_id = input("Enter Voter ID: ")

        if voter_id not in self.voters:
            print("Voter not found.")
            return

        voter = self.voters[voter_id]

        if voter.has_voted:
            print("This voter has already voted.")
            return

        candidate_id = input("Enter Candidate ID: ")

        if candidate_id not in self.candidates:
            print("Candidate not found.")
            return

        transaction = {
            "voter_id": voter_id,
            "candidate_id": candidate_id
        }

        self.blockchain.add_block([transaction])

        voter.has_voted = True

        print("Vote cast successfully.")

    # Print Blockchain
    def print_blockchain(self):
        self.blockchain.print_chain()

    # Validate Blockchain
    def validate_blockchain(self):
        if self.blockchain.is_chain_valid():
            print("Blockchain is valid.")
        else:
            print("Blockchain is NOT valid.")

# Main Menu

def main():
    system = VotingSystem()

    while True:
        print("\n Blockchain voting system )
        print("1. Add Candidate")
        print("2. Add Voter")
        print("3. Cast Vote")
        print("4. Print Blockchain")
        print("5. Validate Chain")
        print("6. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            system.add_candidate()

        elif choice == "2":
            system.add_voter()

        elif choice == "3":
            system.cast_vote()

        elif choice == "4":
            system.print_blockchain()

        elif choice == "5":
            system.validate_blockchain()

        elif choice == "6":
            print("Exiting program")
            break

        else:
            print("Invalid choice. Please try again.")



if __name__ == "__main__":
    main()
