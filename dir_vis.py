import numpy as np
import matplotlib.pyplot as plt
import direction_functions


def plot_path(cur, nxt, ax):
    num = 10
    dif = (nxt - cur) / num
    for i in range(1, num + 1):
        ax.scatter(cur[0] + dif[0] * i, cur[1] + dif[1] * i, cur[2] + dif[2] * i, color='k')
        plt.pause(1)


trails = 10
head = np.zeros(3)
last = np.zeros(3)
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

for _ in range(trails):
    ax.scatter(head[0], head[1], head[2], color='r')
    print(head)
    dirs, upper_bound, _ = direction_functions.fibonacci_sphere(last, np.pi / 5)
    next_dir = dirs[np.random.choice(upper_bound)]
    plot_path(head, next_dir, ax)
    head += next_dir
    last = -next_dir
    plt.pause(0.5)

plt.show()
