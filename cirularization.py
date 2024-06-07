import numpy as np


def get_directions(num):
    directions = np.zeros((num_dir ** 2, 3))
    angles = np.linspace(0, 2 * np.pi, num, endpoint=False)
    # print(np.shape(directions))
    for i in range(num):  # angle of xy plane
        for j in range(num):  # angle of z plane
            directions[i * num + j, 2] = np.sin(angles[j])
            directions[i * num + j, 1] = np.cos(angles[j]) * np.sin(angles[i])
            directions[i * num + j, 0] = np.cos(angles[j]) * np.cos(angles[i])
    # print(np.shape(directions))
    return directions


num = 100000
length = 1000
num_dir = 360
cir = 0
error = 1
# head = np.zeros(3)
directions = get_directions(num_dir)

i = 0
while i < num:
    head = np.zeros(3)
    for _ in range(length):
        head += directions[np.random.choice(num_dir ** 2)]
    if (np.abs(head) < error).all():
        cir += 1
    i += 1

print(cir / num)
