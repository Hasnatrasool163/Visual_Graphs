import numpy as np
import matplotlib.pyplot as plt

def mandelbrot(c, max_iter):
    z = c
    for n in range(max_iter):
        if abs(z) > 2:
            return n
        z = z*z + c
    return max_iter

def mandelbrot_set(xmin, xmax, ymin, ymax, width, height, max_iter):
    r1 = np.linspace(xmin, xmax, width)
    r2 = np.linspace(ymin, ymax, height)
    return (r1, r2, np.array([[mandelbrot(complex(r, i), max_iter) for r in r1] for i in r2]))

def plot_mandelbrot(xmin, xmax, ymin, ymax, width=10, height=10, max_iter=256):
    global mandelbrot_set
    dpi = 80
    img_width = dpi * width
    img_height = dpi * height
    x, y, mandelbrot_set = mandelbrot_set(xmin, xmax, ymin, ymax, img_width, img_height, max_iter)
    
    fig, ax = plt.subplots(figsize=(width, height), dpi=dpi)
    ax.imshow(mandelbrot_set.T, origin='lower', cmap='hot', extent=(xmin, xmax, ymin, ymax))
    ax.set_title("Mandelbrot Set")
    plt.xlabel("Re")
    plt.ylabel("Im")
    plt.show()

plot_mandelbrot(-2.0, 1.0, -1.5, 1.5, width=10, height=10, max_iter=256)