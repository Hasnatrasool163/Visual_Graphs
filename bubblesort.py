import matplotlib.pyplot as plt
import numpy as np
import time
import  matplotlib.animation as animation 

def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        for j in range(0, n-i-1):
            if arr[j] > arr[j+1] :
                arr[j], arr[j+1] = arr[j+1], arr[j]
            yield arr

def visualize_sort():
    N = 30
    arr = np.random.rand(N)
    generator = bubble_sort(arr)

    fig, ax = plt.subplots()
    bar_rects = ax.bar(range(len(arr)), arr, align="edge")
    ax.set_xlim(0, N)
    ax.set_ylim(0, int(1.1 * max(arr)))

    text = ax.text(0.02, 0.95, "", transform=ax.transAxes)

    iteration = [0]
    def update_fig(arr, rects, iteration):
        for rect, val in zip(rects, arr):
            rect.set_height(val)
        iteration[0] += 1
        text.set_text(f"# of operations: {iteration[0]}")

    anim = animation.FuncAnimation(fig, func=update_fig,
        fargs=(bar_rects, iteration),cache_frame_data=False, frames=generator, interval=1,
        repeat=False)
    plt.show()

if __name__ == "__main__":
    visualize_sort()