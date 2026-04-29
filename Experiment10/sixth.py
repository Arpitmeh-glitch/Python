import numpy as np
from fifth import df2 
df_filled = df2.fillna(0)

print("DataFrame after replacing missing values:\n", df_filled)

df_dropped = df2.dropna()

print("\nDataFrame after dropping missing values:\n", df_dropped)