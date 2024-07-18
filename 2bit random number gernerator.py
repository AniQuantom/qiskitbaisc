from qiskit import QuantumCircuit
from qiskit_aer import AerSimulator
import matplotlib.pyplot as plt

def generate_random_number(min_value=0, max_value=1000):
    # Create a quantum circuit with 2 qubits and 2 classical bits
    qc = QuantumCircuit(2, 2)
    
    # Apply Hadamard gates to both qubits to create superposition
    qc.h(0)
    qc.h(1)
    
    # Measure both qubits
    qc.measure([0, 1], [0, 1])
    
    # Create a simulator
    simulator = AerSimulator()
    
    # Run the circuit on the simulator
    job = simulator.run(qc, shots=1)
    result = job.result()
    
    # Get the measurement outcome
    counts = result.get_counts(qc)
    binary_result = list(counts.keys())[0]
    
    # Convert binary to decimal (0-3)
    quantum_random = int(binary_result, 2)
    
    # Scale and shift the result to fit the desired range
    scaled_random = min_value + (quantum_random / 3) * (max_value - min_value)
    
    return round(scaled_random)

# Generate 10 random numbers
num_samples = 10
min_value = 100
max_value = 1000

print(f"Generating {num_samples} random numbers between {min_value} and {max_value}:")
random_numbers = [generate_random_number(min_value, max_value) for _ in range(num_samples)]

# Print the generated numbers
for i, number in enumerate(random_numbers, 1):
    print(f"Number {i}: {number}")

# Plot histogram of generated numbers
plt.figure(figsize=(10, 6))
plt.hist(random_numbers, bins=10, range=(min_value, max_value), align='mid', rwidth=0.8)
plt.title(f'Distribution of {num_samples} Quantum Random Numbers ({min_value}-{max_value})')
plt.xlabel('Number')
plt.ylabel('Frequency')
plt.show()