import matplotlib.pyplot as plt
import matplotlib.animation as animation
import numpy as np

def quick_sort(arr, start, end):
    if start >= end:
        return
    
    pivot_index = partition(arr, start, end)
    yield arr
    yield from quick_sort(arr, start, pivot_index-1)
    yield from quick_sort(arr, pivot_index+1, end)

def partition(arr, start, end):
    pivot = arr[end]
    i = start - 1
    
    for j in range(start, end):
        if arr[j] < pivot:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]
    arr[i+1], arr[end] = arr[end], arr[i+1]
    return i + 1

def visualize_sort():
    N = 30
    arr = np.random.rand(N)
    generator = quick_sort(arr, 0, N-1)

    fig, ax = plt.subplots()
    ax.set_title("Quick Sort Visualization")
    bar_rects = ax.bar(range(len(arr)), arr, align="edge")

    iteration = [0]
    def update_fig(arr, rects, iteration):
        for rect, val in zip(rects, arr):
            rect.set_height(val)
        iteration[0] += 1

    anim = animation.FuncAnimation(fig, func=update_fig,
        fargs=(bar_rects, iteration),cache_frame_data=False, frames=generator, interval=1,
        repeat=False)
    plt.show()

if __name__ == "__main__":
    visualize_sort()