import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

# Constants
g = 9.81  # acceleration due to gravity (m/s^2)

# Initial conditions
angle_deg = 45  # launch angle in degrees
v0 = 20  # initial velocity (m/s)
angle_rad = np.radians(angle_deg)  # convert angle to radians

# Time
t_max = 2 * v0 * np.sin(angle_rad) / g  # total flight time
dt = 0.01  # time step
t = np.arange(0, t_max, dt)  # time array

# Projectile motion equations (ignoring air resistance)
x = v0 * np.cos(angle_rad) * t  # x = v0*cos(theta)*t
y = v0 * np.sin(angle_rad) * t - 0.5 * g * t**2  # y = v0*sin(theta)*t - 1/2*g*t^2

def animate(i):
    # This function is called at each frame of the animation
    ln.set_data(x[:i], y[:i])
    point.set_data(x[i], y[i])
    return ln, point,

# Plot
fig, ax = plt.subplots()
ax.set_xlim(0, max(x)*1.1)
ax.set_ylim(0, max(y)*1.1)
ax.set_xlabel('Distance (m)')
ax.set_ylabel('Height (m)')
ax.set_title('Projectile Motion')

ln, = plt.plot([], [], 'r-', linewidth=2)
point, = plt.plot([], [], 'bo')

ani = FuncAnimation(fig, animate, frames=len(t), interval=dt*1000, blit=True)

plt.show()