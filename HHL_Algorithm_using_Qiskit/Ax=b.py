"""
A = [[1, 1],
     [1, -1]]

b = [1, 0]
"""

from qiskit import QuantumCircuit
from qiskit_aer import AerSimulator

qc = QuantumCircuit(2)

qc.h(0)        # Hadamard -> superposition
qc.cx(0,1)     # CNOT -> entanglement
qc.ry(1.2,1)   # rotation gate

qc.measure_all()

sim = AerSimulator()
result = sim.run(qc).result()

print(result.get_counts())
