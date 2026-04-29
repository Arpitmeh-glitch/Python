import matplotlib.pyplot as plt

# Sample data
x = [1, 2, 3, 4, 5]
y = [10, 20, 25, 30, 40]

# Line plot
plt.figure()
plt.plot(x, y)
plt.title("Line Plot")
plt.xlabel("X")
plt.ylabel("Y")
plt.show()

# Bar chart
plt.figure()
plt.bar(x, y)
plt.title("Bar Chart")
plt.show()

# Scatter plot
plt.figure()
plt.scatter(x, y)
plt.title("Scatter Plot")
plt.show()

# Histogram
plt.figure()
plt.hist(y)
plt.title("Histogram")
plt.show()