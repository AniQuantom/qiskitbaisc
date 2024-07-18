from qiskit import QuantumCircuit

# Create a Quantum Circuit with 2 qubits
qc = QuantumCircuit(2)

# Apply some gates
qc.h(0)  # Hadamard gate on qubit 0
qc.cx(0, 1)  # CNOT gate with control qubit 0 and target qubit 1

# Add measurement
qc.measure_all()

# Print the circuit
print(qc)

# Print the circuit depth
print(f"Circuit depth: {qc.depth()}")

# Print the number of qubits
print(f"Number of qubits: {qc.num_qubits}")