import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

# Initialize parameters
grid_size = 100  # Size of the grid
diffusion_rate = 0.1  # Diffusion rate
num_steps = 200  # Number of steps in the simulation

# Initialize the grid
grid = np.zeros((grid_size, grid_size))
middle = grid_size // 2
grid[middle-5:middle+5, middle-5:middle+5] = 100  # Initial concentration in the center

def diffuse(grid):
    # Apply diffusion to the grid
    new_grid = grid.copy()
    for i in range(1, grid_size-1):
        for j in range(1, grid_size-1):
            new_grid[i, j] = grid[i, j] + diffusion_rate * (
                grid[i-1, j] + grid[i+1, j] +
                grid[i, j-1] + grid[i, j+1] - 4 * grid[i, j])
    return new_grid

# Set up the figure and axis for animation
fig, ax = plt.subplots()
im = ax.imshow(grid, cmap='plasma', interpolation='bilinear')

def update(frame):
    global grid
    grid = diffuse(grid)
    im.set_data(grid)
    return [im]

# Create animation
ani = animation.FuncAnimation(fig, update, frames=num_steps, interval=50, blit=True)

plt.show()