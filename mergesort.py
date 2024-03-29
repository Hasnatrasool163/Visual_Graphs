import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

def merge_sort(arr, l, r):
    if r <= l:
        return
    
    mid = l + (r - l) // 2
    yield from merge_sort(arr, l, mid)
    yield from merge_sort(arr, mid + 1, r)
    yield from merge(arr, l, mid, r)
    yield arr

def merge(arr, l, m, r):
    n1 = m - l + 1
    n2 = r - m
    L = arr[l:l + n1]
    R = arr[m + 1:m + 1 + n2]
    
    i = j = 0
    k = l

    while i < n1 and j < n2:
        if L[i] < R[j]:
            arr[k] = L[i]
            i += 1
        else:
            arr[k] = R[j]
            j += 1
        k += 1
        yield arr
    
    while i < n1:
        arr[k] = L[i]
        i += 1
        k += 1
        yield arr
    
    while j < n2:
        arr[k] = R[j]
        j += 1
        k += 1
        yield arr

def visualize_sort():
    N = 50
    arr = np.random.rand(N)
    generator = merge_sort(arr, 0, N-1)
    
    fig, ax = plt.subplots()
    ax.set_title("Merge Sort Visualization")
    bars = ax.bar(range(len(arr)), arr, align="edge")
    
    iteration = [0]
    def update_fig(arr, rects, iteration):
        for rect, val in zip(rects, arr):
            rect.set_height(val)
        iteration[0] += 1
    
    anim = animation.FuncAnimation(fig, func=update_fig,
        fargs=(bars, iteration),cache_frame_data=False, frames=generator, interval=1,
        repeat=False)
    plt.show()

if __name__ == "__main__":
    visualize_sort()