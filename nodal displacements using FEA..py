import numpy as np
import scipy.sparse as sp
import scipy.sparse.linalg as spla
import matplotlib.pyplot as plt

# Problem Parameters
L = 1.0  # Length of the beam (m)
E = 210e9  # Young's Modulus (Pa)
A = 0.01  # Cross-sectional Area (m^2)
num_elements = 10  # Number of elements
num_nodes = num_elements + 1  # Nodes = Elements + 1
force = 1000  # Force applied at the free end (N)

# Generate Node Coordinates
node_coords = np.linspace(0, L, num_nodes)

# Connectivity (which nodes form each element)
element_nodes = [(i, i + 1) for i in range(num_elements)]

# Print Mesh Info
print("Node Coordinates:", node_coords)
print("Element Connectivity:", element_nodes)
# Initialize Global Stiffness Matrix
K = np.zeros((num_nodes, num_nodes))

# Element Stiffness Matrix Assembly
for e in element_nodes:
    node_start, node_end = e
    length = node_coords[node_end] - node_coords[node_start]  # Element length
    k_local = (E * A / length) * np.array([[1, -1], [-1, 1]])  # Local stiffness matrix
    # Assemble into global stiffness matrix
    K[np.ix_(e, e)] += k_local
# Initialize Force Vector
F = np.zeros(num_nodes)
F[-1] = force  # Apply force at the last node

# Apply Dirichlet Boundary Condition (Fixed at node 0)
K[0, :] = 0
K[:, 0] = 0
K[0, 0] = 1  # Set diagonal to 1 for fixed node
F[0] = 0  # No displacement at fixed node
# Solve the System
U = spla.spsolve(sp.csr_matrix(K), F)

# Print Displacements
print("Nodal Displacements:", U)
# Plot Results
plt.plot(node_coords, U, '-o', label='Displacement')
plt.title("Displacement of a Cantilever Beam")
plt.xlabel("Position along the beam (m)")
plt.ylabel("Displacement (m)")
plt.grid()
plt.legend()
plt.show()
