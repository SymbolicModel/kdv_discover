# Dataset Description: kdv_data_for_workshop_PySINDy.mat
## Variables  
### u_only_mat_reshaped (size: 50 x 4800) 
- only contains the u variable
- First dimension is the number of times snapshots (50)
- The second dimension corresponds to the number of space points (4800)
- 
#### Structure
- Data is organised sequentially over space, time and only for one case.  
- Dimensions:  
  - Space (N): 4800 points  
  - Time (Nt): 50 snapshots  

# Dataset Description: kdv_data_for_workshop.mat

This dataset contains numerical data from the KdV equation. A working example with PySR is given in Test_KdV.py, but you are encouraged to write your own. 

## Variables  

### u_only_mat_reshaped (size: 8 x 10 x 400) 
- only contains the u variable
- First dimension is the number of cases (8)
- The second dimension is the number of time snapshots (10)
- The third dimension corresponds to the number of space points (400)

### u_mat (size: 32000 × 5)  
- Each row corresponds to a point in space and time for a given case.  
- Each column contains one of the following values:  
  1. u — solution value  
  2. ux — first spatial derivative (∂u/∂x)  
  3. uxx — second spatial derivative (∂²u/∂x²)  
  4. uxxx — third spatial derivative (∂³u/∂x³)  
  5. uxxxx — fourth spatial derivative (∂⁴u/∂x⁴)  


#### Structure
- Data is organised sequentially over space, time, and cases.  
- Dimensions:  
  - Space (N): 400 points  
  - Time (Nt): 10 snapshots  
  - Cases (N_case): 8 independent cases  
- Overall shape: 8 × 10 × 400 = 32000 rows  

Row ordering follows:  

Case 1
u(x0,t0)   ux(x0,t0)   uxx(x0,t0)   uxxx(x0,t0)   uxxxx(x0,t0)
u(x1,t0)   ux(x1,t0)   uxx(x1,t0)   uxxx(x1,t0)   uxxxx(x1,t0)
...
u(x399,t0) ...
u(x0,t1)   ...
...
u(x399,t9) ...
Case 2
...
Case 8
...

---

### u_tar (size: 32000 × 1)  
- Contains the time derivative:  
  - ut — ∂u/∂t  
- Follows the same row ordering as u_mat.  

---

✅ In short:  
- u_mat provides the state (u and spatial derivatives).  
- u_tar provides the target (time derivative).  
- Together, they represent spatio-temporal samples from 8 cases of the KdV equation.  

---

## Tensor Reshaping Illustration

Think of the data as a 3D tensor:

    [Space = 400] × [Time = 10] × [Cases = 8] = 32000 samples

Each row in u_mat and u_tar corresponds to one slice of this tensor, flattened into a 2D matrix.
