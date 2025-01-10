# **Finite Element Analysis (FEA) Solver**

A Python-based Finite Element Analysis (FEA) solver to compute **displacements**, **strains**, and **stresses** in 1D structures (beams). The project demonstrates key concepts of FEA with visualization of results for enhanced understanding.

---

## **Features**
- Solve 1D structural problems using the FEA method.
- Compute **nodal displacements**, **element strains**, and **element stresses**.
- Visualize results with high-quality 2D plots:
  - Displacement distribution.
  - Strain distribution.
  - Stress distribution.

---

## **Technologies Used**
- **Python**: Programming language.
- **NumPy**: Efficient numerical computations.
- **SciPy**: Sparse matrix handling and equation solving.
- **Matplotlib**: Data visualization.

---

## **Project Overview**
This solver computes the deformation and internal forces of a cantilever beam under specified loading and material properties using the Finite Element Method.

### **Steps in the Solver**:
1. **Mesh Generation**:
   - Divide the beam into finite elements.
2. **Stiffness Matrix Assembly**:
   - Compute local and global stiffness matrices.
3. **Apply Boundary Conditions**:
   - Handle fixed and free ends.
4. **Solve System of Equations**:
   - Compute nodal displacements.
5. **Post-Processing**:
   - Calculate strains and stresses for each element.
6. **Visualization**:
   - Generate plots for displacement, strain, and stress.

---

## **Usage**

### **1. Prerequisites**
Ensure you have Python installed along with the required libraries:
```bash
pip install numpy scipy matplotlib
```

### **2. Clone the Repository**
```bash
git clone https://github.com/bibeksubedi0001/Finite-Element-Method.git
cd Finite-Element-Method
```

### **3. Run the Code**
Execute the Python script to compute and visualize results:

## **Input Parameters**
You can modify the following parameters in the script to test different scenarios:
- **Beam Length (`L`)**
- **Young's Modulus (`E`)**
- **Cross-sectional Area (`A`)**
- **Number of Elements (`num_elements`)**
- **Applied Force (`force`)

---

## **Output**
The solver generates:
- **Numerical Results**:
  - Nodal displacements.
  - Strains and stresses in each element.
- **Graphs**:
  - Displacement along the beam.
  - Strain distribution.
  - Stress distribution.

---

## **Contributing**
Contributions are welcome! Please follow these steps:
1. Fork the repository.
2. Create a new branch: `git checkout -b feature-name`.
3. Commit your changes: `git commit -m 'Add feature-name'`.
4. Push to the branch: `git push origin feature-name`.
5. Open a Pull Request.

---

## **Contact**
For questions or suggestions, feel free to reach out:
- **Email**: 078bce035.bibek@pcampus.edu.np
