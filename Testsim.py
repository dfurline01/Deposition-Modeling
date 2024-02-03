

import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

deposition_rate = 0.1
diffusion_coefficient = 0.01
time_steps = 100
substrate_dimensions = (10, 10, 10) #x,y,z

substrate = np.zeros(substrate_dimensions)

def deposition_model_3d(substrate, deposition_rate, diffusion_coefficient, time_steps):
    for _ in range(time_steps):
        #Deposition
        substrate[0, 0, 0] += deposition_rate

        #Diffusion in x-direction
        substrate[1:, :, :] += diffusion_coefficient * (substrate[:-1, :, :] - substrate[1:, :, :])

        # Diffusion in y-direction
        substrate[:, 1:, :] += diffusion_coefficient * (substrate[:, :-1, :] - substrate[:, 1:, :])

        # Diffusion in z-direction
        substrate[:, :, 1:] += diffusion_coefficient * (substrate[:, :, :-1] - substrate[:, :, 1:])

def visualize_3d_coating(substrate):
    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')

    x, y, z = np.meshgrid(range(substrate.shape[0]), range(substrate.shape[1]), range(substrate.shape[2]))
    ax.scatter(x, y, z, c=substrate.flatten(), cmap='viridis', s=50, alpha=0.5)

    ax.set_xlabel('X')
    ax.set_ylabel('Y')
    ax.set_zlabel('Z')
    ax.set_title('3D Coating Deposition Model')

    plt.show()

visualize_3d_coating(substrate)