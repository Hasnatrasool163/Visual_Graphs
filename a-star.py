import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation
from queue import PriorityQueue

# Grid setup
n = 10  # Grid size
grid = np.zeros((n, n))
start = (0, 0)
goal = (n-1, n-1)
obstacles = [(1, 2), (1, 3), (2, 3), (3, 3), (4, 5), (5, 4), (5, 5)]

# Adding obstacles to the grid
for obstacle in obstacles:
    grid[obstacle] = 1

def heuristic(a, b):
    return abs(a[0] - b[0]) + abs(a[1] - b[1])

def a_star_search(start, goal):
    frontier = PriorityQueue()
    frontier.put(start, 0)
    came_from = {}
    cost_so_far = {}
    came_from[start] = None
    cost_so_far[start] = 0

    while not frontier.empty():
        current = frontier.get()

        if current == goal:
            break

        for next in get_neighbors(current):
            new_cost = cost_so_far[current] + 1
            if next not in cost_so_far or new_cost < cost_so_far[next]:
                cost_so_far[next] = new_cost
                priority = new_cost + heuristic(goal, next)
                frontier.put(next, priority)
                came_from[next] = current
        yield current, came_from, cost_so_far

def get_neighbors(pos):
    neighbors = []
    for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]:  # 4-way connectivity
        x, y = pos[0] + dx, pos[1] + dy
        if 0 <= x < n and 0 <= y < n and grid[(x, y)] == 0:
            neighbors.append((x, y))
    return neighbors

def visualize_search():
    fig, ax = plt.subplots()
    ax.set_title("A* Pathfinding")
    cmap = plt.cm.viridis
    cmap.set_under('red')
    cmap.set_over('blue')

    generator = a_star_search(start, goal)

    def update(frame):
        current, came_from, cost_so_far = next(generator, (None, None, None))
        ax.clear()
        ax.imshow(grid, cmap=cmap, vmin=0, vmax=1.5)

        # Highlight the current node and start/goal
        if current:
            ax.scatter(current[1], current[0], color='red', s=100)
        ax.scatter(start[1], start[0], marker='*', color='blue', s=100)
        ax.scatter(goal[1], goal[0], marker='*', color='green', s=100)

        # Draw path
        if came_from:
            for key in came_from:
                if came_from[key]:
                    next_step = came_from[key]
                    ax.plot([key[1], next_step[1]], [key[0], next_step[0]], color="black")

    ani = animation.FuncAnimation(fig, update, frames=range(n*n), repeat=False, interval=100)
    plt.axis('off')
    plt.show()

if __name__ == "__main__":
    visualize_search()