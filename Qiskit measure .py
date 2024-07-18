# Import necessary libraries
from qiskit import QuantumCircuit, transpile, Aer, execute
from qiskit.visualization import plot_histogram
import matplotlib.pyplot as plt

# Create a Quantum Circuit with 3 qubits and 3 classical bits
qc = QuantumCircuit(3, 3)

# Create entanglement between qubit 1 and qubit 2
qc.h(1)
qc.cx(1, 2)

# Prepare state to be teleported on qubit 0
qc.cx(0, 1)
qc.h(0)

# Measure qubits 0 and 1
qc.measure([0, 1], [0, 1])

# Apply conditional operations based on measurements
qc.cx(1, 2)
qc.cz(0, 2)

# Measure the teleported qubit
qc.measure(2, 2)

# Simulate the quantum circuit using QASM simulator
backend = Aer.get_backend('qasm_simulator')
transpiled_qc = transpile(qc, backend)
result = execute(transpiled_qc, backend, shots=1024).result()
counts = result.get_counts()

# Plot the results
plot_histogram(counts)
plt.show()

