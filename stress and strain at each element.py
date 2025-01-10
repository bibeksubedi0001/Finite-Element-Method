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
# Check if U is properly calculated
if U is None:
    raise ValueError("Displacement vector 'U' is not defined. Check the solver implementation.")
# Initialize lists to store results
element_strains = []
element_stresses = []

# Loop through each element to calculate strain and stress
for e in element_nodes:
    node_start, node_end = e
    length = node_coords[node_end] - node_coords[node_start]  # Element length
    # Calculate strain
    strain = (U[node_end] - U[node_start]) / length
    # Calculate stress
    stress = E * strain
    
    # Store results
    element_strains.append(strain)
    element_stresses.append(stress)

# Print Results
print("Element Strains:", element_strains)
print("Element Stresses:", element_stresses)
# Calculate element midpoints for plotting
element_midpoints = [(node_coords[e[0]] + node_coords[e[1]]) / 2 for e in element_nodes]
# Normalize data to the 10^-9 scale
element_strains_scaled = np.array(element_strains) * 1e9  # Convert strain to 10^-9 scale
element_stresses_scaled = np.array(element_stresses) * 1e9  # Convert stress to 10^-9 scale

# Strain Plot with Specific Range
plt.figure(figsize=(12, 6))  # Increase figure size for clarity

# Plot the strain values
plt.plot(
    element_midpoints,
    element_strains, 
    '-o', 
    label='Strain', 
    markersize=8, 
    linewidth=2, 
    color='blue'
)

# Add title and axis labels
plt.title("Strain Distribution in Each Element", fontsize=18)
plt.xlabel("Position along the beam (m)", fontsize=14)
plt.ylabel("Strain (10^-21 m)", fontsize=14)

# Add grid for better visualization
plt.grid(True, linestyle='--', alpha=0.7)

# Set axis tick font size
plt.xticks(fontsize=12)
plt.yticks(fontsize=12)

# Add legend
plt.legend(fontsize=12, loc='upper right')

# Adjust Y-axis to the specific range with buffer for annotation
y_min = 4.7619047619047e-07
y_max = 4.7619047619047647e-07
plt.ylim(y_min, y_max)

# Add descriptive note about the range
plt.text(
    element_midpoints[0], 
    y_max - 1e-9, 
    "Strain range zoomed in for clarity", 
    fontsize=12, 
    color='purple'
)

# Display the plot
plt.show()

# Stress Plot with Scale 10^-9
plt.figure(figsize=(10, 6))
plt.plot(element_midpoints, element_stresses_scaled, '-o', label='Stress (10^-9 Pa)', markersize=8, linewidth=2, color='orange')
plt.title("Stress in Each Element (Scale: 10^-9)", fontsize=16)
plt.xlabel("Position along the beam (m)", fontsize=14)
plt.ylabel("Stress (10^-9 Pa)", fontsize=14)
plt.grid(True, linestyle='--', alpha=0.7)
plt.xticks(fontsize=12)
plt.yticks(fontsize=12)
plt.legend(fontsize=12)

# Adjust Y-axis limits for stress
plt.ylim(min(element_stresses_scaled) - 1, max(element_stresses_scaled) + 1)

# Annotate Maximum Stress
max_stress_idx = np.argmax(element_stresses_scaled)
plt.annotate(
    f"Max Stress: {element_stresses_scaled[max_stress_idx]:.2f} (10^-9 Pa)",
    (element_midpoints[max_stress_idx], element_stresses_scaled[max_stress_idx]),
    xytext=(element_midpoints[max_stress_idx] - 0.15, element_stresses_scaled[max_stress_idx] - 1),
    arrowprops=dict(arrowstyle="->", color='red'),
    fontsize=12,
    color='red'
)
plt.show()
