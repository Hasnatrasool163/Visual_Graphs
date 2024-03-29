import matplotlib.pyplot as plt

def binary_search_visual(arr, x):
    low, high = 0, len(arr) - 1
    fig, ax = plt.subplots()
    iteration = 1
    
    while low <= high:
        mid = (low + high) // 2
        
        # Clear the previous plot
        ax.clear()
        
        # Plot the array and highlight the search area and mid element
        ax.bar(range(len(arr)), arr, color='gray')
        ax.bar(range(low, high+1), arr[low:high+1], color='blue')
        ax.bar(mid, arr[mid], color='red')
        
        ax.text(mid, arr[mid], f'{arr[mid]}', ha='center', va='bottom')
        
        # Setting titles and labels
        plt.title(f'Iteration: {iteration}')
        ax.set_xlabel('Index')
        ax.set_ylabel('Value')
        plt.xticks(range(len(arr)), range(len(arr)))
        
        # Display the plot
        plt.pause(1)
        
        if arr[mid] == x:
            plt.title(f'Element found at index {mid}')
            plt.show()
            return mid
        elif arr[mid] < x:
            low = mid + 1
        else:
            high = mid - 1
        
        iteration += 1
        
    plt.title("Element not found")
    plt.show()
    return -1

# Example usage
arr = [1, 3, 4, 5, 7, 8, 9, 10, 12, 14, 16, 18, 20]
# print("Enter Number to find (1,3,4,5,7,8,9,10,12,14,16,18,20)")
# x=int(input("Enter Number to find (1,3,4,5,7,8,9,10,12,14,16,18,20)"))
x=10
# x = 7
binary_search_visual(arr, x)