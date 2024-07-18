from qiskit import QuantumCircuit, QuantumRegister, ClassicalRegister
from qiskit_aer import AerSimulator
import hashlib

def quantum_encrypt(username, key):
    # Convert username to binary
    binary_username = ''.join(format(ord(char), '08b') for char in username)
    
    # Ensure the key is at least as long as the binary username
    while len(key) < len(binary_username):
        key += key
    key = key[:len(binary_username)]
    
    # Create quantum registers
    qr = QuantumRegister(len(binary_username))
    cr = ClassicalRegister(len(binary_username))
    qc = QuantumCircuit(qr, cr)
    
    # Encode the username into quantum states
    for i, bit in enumerate(binary_username):
        if bit == '1':
            qc.x(qr[i])
    
    # Apply the key
    for i, bit in enumerate(key):
        if bit == '1':
            qc.h(qr[i])  # Apply Hadamard gate if key bit is 1
    
    # Measure the qubits
    qc.measure(qr, cr)
    
    # Simulate the circuit
    simulator = AerSimulator()
    result = simulator.run(qc, shots=1).result()
    counts = result.get_counts(qc)
    encrypted = list(counts.keys())[0]
    
    return encrypted

def quantum_decrypt(encrypted, key):
    # Create quantum registers
    qr = QuantumRegister(len(encrypted))
    cr = ClassicalRegister(len(encrypted))
    qc = QuantumCircuit(qr, cr)
    
    # Encode the encrypted message into quantum states
    for i, bit in enumerate(encrypted):
        if bit == '1':
            qc.x(qr[i])
    
    # Apply the key (decryption is the same as encryption for this method)
    for i, bit in enumerate(key):
        if bit == '1':
            qc.h(qr[i])  # Apply Hadamard gate if key bit is 1
    
    # Measure the qubits
    qc.measure(qr, cr)
    
    # Simulate the circuit
    simulator = AerSimulator()
    result = simulator.run(qc, shots=1).result()
    counts = result.get_counts(qc)
    decrypted_binary = list(counts.keys())[0]
    
    # Convert binary back to text
    decrypted = ''.join(chr(int(decrypted_binary[i:i+8], 2)) for i in range(0, len(decrypted_binary), 8))
    
    return decrypted

# Example usage
username = "Alice123"
key = hashlib.sha256(b"secret_key").hexdigest()

print(f"Original username: {username}")

encrypted = quantum_encrypt(username, key)
print(f"Encrypted: {encrypted}")

decrypted = quantum_decrypt(encrypted, key)
print(f"Decrypted: {decrypted}")