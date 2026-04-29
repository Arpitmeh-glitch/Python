import numpy as np
arr2 = np.array([[10, 20, 30],
                 [40, 50, 60],
                 [70, 80, 90]])


row_sum = np.sum(arr2, axis=1)

col_sum = np.sum(arr2, axis=0)

second_max = np.sort(arr2.flatten())[-2]

print("Array:\n", arr2)
print("Row sums:", row_sum)
print("Column sums:", col_sum)
print("Second maximum element:", second_max)