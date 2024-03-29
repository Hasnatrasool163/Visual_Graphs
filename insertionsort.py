import matplotlib.pyplot as plt
import matplotlib.animation as animation
import numpy as np

def insertion_sort(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i-1
        while j >=0 and key < arr[j] :
                arr[j + 1] = arr[j]
                j -= 1
                yield arr
        arr[j + 1] = key
        yield arr

def visualize_sort():
    N = 30
    arr = np.random.rand(N)
    generator = insertion_sort(arr)

    fig, ax = plt.subplots()
    ax.set_title("Insertion Sort Visualization")
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