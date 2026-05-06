import matplotlib.pyplot as plt

x = [1, 2, 3, 4]

y1 = [10, 20, 30, 40]
y2 = [40, 30, 20, 10]

plt.plot(x, y1, label="Line 1")
plt.plot(x, y2, label="Line 2")

plt.legend()   # shows legend
plt.show() 