#%%

import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import numpy as np
from sklearn.linear_model import Lasso
from scipy.io import loadmat
from sklearn.metrics import mean_squared_error
from scipy.integrate import solve_ivp
 
import pysr
from scipy.ndimage import gaussian_filter, convolve
from scipy.signal import hilbert, chirp

import matplotlib.pyplot as plt

# Ignore matplotlib deprecation warnings
import warnings
warnings.filterwarnings("ignore", category=UserWarning)

# Seed the random number generators for reproducibility
# np.random.seed(100)
#%%
# Load the data stored in a matlab .mat file
KdV_data = loadmat('./kdv_data_for_workshop.mat')

#%%
def grad1(in1, h):
    """
    This function takes the gradient in the x direction. h is the spatial step.
    """
    out1 = np.zeros_like(in1)
    noy1, nox1 = in1.shape
    in_ = np.zeros((noy1, nox1 + 4))
    noyz, noxz = in_.shape
    
    in_[:, 0] = in1[:, nox1 - 2]  # Adjusted index by -1 for 0-based indexing in Python
    in_[:, 1] = in1[:, nox1 - 1]  # Adjusted index by -1 for 0-based indexing in Python
    in_[:, 2:nox1 + 2] = in1
    in_[:, noxz - 2] = in_[:, 1]
    in_[:, noxz - 1] = in_[:, 0]
    
    out_ = np.zeros_like(in_)
    out_[:, 2:noxz - 2] = (-in_[:, 0:noxz - 4] + 8 * in_[:, 1:noxz - 3] - 8 * in_[:, 3:noxz - 1] + in_[:, 4:noxz]) / (12 * h)
    out1 = out_[:, 2:nox1 + 2]
    
    return out1
#%%
jl = pysr.julia_helpers.init_julia(julia_kwargs={"threads": 5, "optimize": 3})
#%%

u_in = KdV_data['u_mat'];
tar_eta_t = KdV_data['u_tar'];

tar_eta_t = tar_eta_t.reshape((u_in.shape[0], 1));
print('Data Loading and success\n')
#%%
u = KdV_data['u_mat'][:, 0]
u_reshape = u.reshape(8, 10, 400)
x = KdV_data['x_vec'].transpose()
#%%
t = KdV_data['t_vec'].transpose()
t.shape
#%%
plt.plot(x, u_reshape[0, 7, :])

#%%
u_case = u_reshape[0, 7, :]

u_x = grad1(u_case, 0.1)
u_xx = grad1(u_x, 0.1)
u_xxx = grad1(u_xx, 0.1)
#%%

u_t = u_case*u_x + u_xxx

#%%
#Plot the equation

plt.plot(u_t)

#%%
model_real = pysr.PySRRegressor(binary_operators=["+", "*" ], 
                                complexity_of_operators={"+": 5}, 
                                nested_constraints={"*": {"*" : 3} }, 
                                maxsize = 10, 
                                batching=True,
                                populations=30,
                                population_size=57,
                                ncyclesperiteration = 1000,
                                )
#%%
model_real.fit(u_in,np.real(tar_eta_t))
print('KdV Train Test \n')
print(model_real.get_best().equation)

