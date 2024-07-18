from qiskit import QuantumCircuit
from qiskit_aer import AerSimulator
from qiskit.visualization import plot_histogram
import matplotlib.pyplot as plt

# Create a quantum circuit with 2 qubits and 2 classical bits
qc = QuantumCircuit(2, 2)

# Apply Hadamard gate to qubit 0
qc.h(0)

# Apply CNOT gate with control qubit 0 and target qubit 1
qc.cx(0, 1)

# Measure both qubits
qc.measure([0, 1], [0, 1])

# Create a simulator
simulator = AerSimulator()

# Run the circuit on the simulator
job = simulator.run(qc, shots=1000)

# Get the results
result = job.result()
counts = result.get_counts(qc)

print("Circuit:")
print(qc)
print("\nMeasurement results:")
print(counts)

# Plot the histogram
plot_histogram(counts)
plt.show()