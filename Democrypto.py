from qiskit import QuantumCircuit, QuantumRegister, ClassicalRegister
from qiskit_aer import AerSimulator
import hashlib
import random

class QuantumCoin:
    def __init__(self):
        self.blockchain = []
        self.pending_transactions = []

    def quantum_hash(self, data):
        # Convert data to binary
        binary_data = ''.join(format(ord(char), '08b') for char in str(data))
        
        # Create quantum circuit
        qr = QuantumRegister(len(binary_data))
        cr = ClassicalRegister(len(binary_data))
        qc = QuantumCircuit(qr, cr)
        
        # Encode data into quantum states
        for i, bit in enumerate(binary_data):
            if bit == '1':
                qc.x(qr[i])
        
        # Apply quantum operations
        for i in range(len(binary_data)):
            qc.h(qr[i])
        qc.cx(qr[0], qr[1])
        
        # Measure
        qc.measure(qr, cr)
        
        # Simulate
        simulator = AerSimulator()
        result = simulator.run(qc, shots=1).result()
        counts = result.get_counts(qc)
        quantum_hash = list(counts.keys())[0]
        
        return quantum_hash

    def create_transaction(self, sender, recipient, amount):
        transaction = {
            'sender': sender,
            'recipient': recipient,
            'amount': amount
        }
        self.pending_transactions.append(transaction)
        return transaction

    def mine_block(self, miner):
        if not self.pending_transactions:
            return None

        last_block = self.blockchain[-1] if self.blockchain else {'hash': '0'*64}
        new_block = {
            'transactions': self.pending_transactions,
            'previous_hash': last_block['hash'],
            'nonce': 0
        }

        while True:
            new_block['nonce'] += 1
            block_hash = self.quantum_hash(str(new_block))
            if block_hash.startswith('0000'):  # Simple proof of work
                new_block['hash'] = block_hash
                break

        self.blockchain.append(new_block)
        self.pending_transactions = [
            self.create_transaction("System", miner, 1)  # Mining reward
        ]
        return new_block

    def get_balance(self, address):
        balance = 0
        for block in self.blockchain:
            for transaction in block['transactions']:
                if transaction['recipient'] == address:
                    balance += transaction['amount']
                if transaction['sender'] == address:
                    balance -= transaction['amount']
        return balance

# Usage example
coin = QuantumCoin()

# Create some transactions
coin.create_transaction("Alice", "Bob", 50)
coin.create_transaction("Bob", "Charlie", 30)

# Mine a block
mined_block = coin.mine_block("Miner1")
print("Mined block:", mined_block)

# Check balances
print("Alice's balance:", coin.get_balance("Alice"))
print("Bob's balance:", coin.get_balance("Bob"))
print("Charlie's balance:", coin.get_balance("Charlie"))
print("Miner1's balance:", coin.get_balance("Miner1"))