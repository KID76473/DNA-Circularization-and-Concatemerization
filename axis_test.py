import numpy as np

table = [[[1, 2],
         [3, 4]],
         [[5, 6],
          [7, 8]]]

print(np.shape(table))
print(np.sum(table, axis = -1))

# axis = 0
# 1 + 5, 2 + 6, 3 + 7, 4 + 8

# axis = 1
# 1 + 3, 2 + 4, 5 + 7, 6 + 8

# axis = 2 equal to axis = -1
# 1 + 2, 3 + 4, 5 + 6, 7 + 8