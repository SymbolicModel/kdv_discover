# Dataset Description: `kdv_data.mat`

This dataset contains numerical data from the KdV equation.  

## Structure
- Data is organised sequentially over space and time.  
- Dimensions:  
  - Time (Nt): 51 snapshots  
  - Space (Nx): 401 points  
  
## Variables  

### t (size: 1 x 51)

### x (size: 1 x 401)

### u (size: 51 x 401)
- u = u( T, X )

# Dataset Description: `kdv_data_for_workshop.mat`

This dataset contains numerical data from the KdV equation, but with less sampling in time, making it more difficult!

## Structure
- Data is organised sequentially over space, time, and cases.  
- Dimensions:  
  - Cases (Ncase): 8 independent cases  
  - Time (Nt): 10 snapshots  
  - Space (Nx): 400 points  
  
- Overall shape: 8 x 10 x 400 = 32000 rows  

## Variables  

### u (size: 8 x 10 x 400)
- Contain the field u in the 8 cases
- u = u( CASE, T, X )

### u_x (size: 32000 × 5)  
- Each row corresponds to a point in space and time for a given case.  
- Each column contains one of the following values:  
  1. u — solution value  
  2. ux — first spatial derivative (∂u/∂x)  
  3. uxx — second spatial derivative (∂²u/∂x²)  
  4. uxxx — third spatial derivative (∂³u/∂x³)  
  5. uxxxx — fourth spatial derivative (∂⁴u/∂x⁴)  

### u_t (size: 32000 × 1)  
- Contains the time derivative:  
  - ut — ∂u/∂t  
- Follows the same row ordering as u_x.  

## Tensor Reshaping Illustration

Think of the data as a 3D tensor:

    [Cases = 8] x [Time = 10] x [Space = 400] = 32000 samples

Each row in u_x and u_t corresponds to one slice of this tensor, flattened into an 1D array.

**Flattening is done in Row Major manner, i.e. u= u( CASE, T, X ), the flatten array has the order **
```
u(0,0,0)
u(0,0,1)
u(0,0,2)
...
u(0,0,Nx-1)
u(0,1,0)
...
u(0,Nt-1,Nx-1)
u(1,0,0)
...
u(Ncase-1,Nt-1,Nx-1)
```

