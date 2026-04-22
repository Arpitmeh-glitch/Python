# Import libraries
import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd

# Set seaborn style
sns.set(style="whitegrid")

# Load dataset (make sure iris.csv is in same folder)
df = pd.read_csv("iris.csv")

# Display first few rows (optional)
print(df.head())

# -------------------------------
# 1. Line Plot (Matplotlib)
# -------------------------------
plt.figure()
plt.plot(df.index, df['sepal_length'], marker='o')
plt.title("Sepal Length Trend")
plt.xlabel("Index")
plt.ylabel("Sepal Length")
plt.show()

# -------------------------------
# 2. Bar Chart (Matplotlib)
# -------------------------------
# Average sepal length per species
avg_sepal = df.groupby('species')['sepal_length'].mean()

plt.figure()
plt.bar(avg_sepal.index, avg_sepal.values)
plt.title("Average Sepal Length per Species")
plt.xlabel("Species")
plt.ylabel("Average Sepal Length")
plt.show()

# -------------------------------
# 3. Scatter Plot (Seaborn)
# -------------------------------
plt.figure()
sns.scatterplot(x='sepal_length', y='petal_length', hue='species', data=df)
plt.title("Sepal vs Petal Length")
plt.show()

# -------------------------------
# 4. Histogram (Seaborn)
# -------------------------------
plt.figure()
sns.histplot(df['sepal_length'], kde=True)
plt.title("Distribution of Sepal Length")
plt.show()

# -------------------------------
# 5. Box Plot (Seaborn)
# -------------------------------
plt.figure()
sns.boxplot(x='species', y='petal_length', data=df)
plt.title("Petal Length Distribution by Species")
plt.show()

# -------------------------------
# 6. Heatmap (Seaborn)
# -------------------------------
corr = df.corr(numeric_only=True)

plt.figure()
sns.heatmap(corr, annot=True, cmap='coolwarm')
plt.title("Feature Correlation Heatmap")
plt.show()