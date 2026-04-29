import pandas as pd

data = {'X': [7, 5, 6, 8, 6],
        'Y': [8, 4, 9, 3, 8],
        'Z': [8, 9, 6, 2, 3]}

df = pd.DataFrame(data)
power_result = df['X'] ** df['Y']

print("Original DataFrame:\n", df)
print("\nX raised to power Y:\n", power_result)