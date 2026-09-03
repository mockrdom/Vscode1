import pandas as pd

file_path = 'F:\\Downloads\\Affle 3i.xlsx - Profit & Loss.csv'

# 1. Read CSV using header row index 2 (line 3 in file)
df = pd.read_csv(file_path, header=2)

# 2. Clean up unnamed helper or empty columns
df = df.dropna(how='all', axis=1)
print("Uncleaned Data")
print(df.head(18))
df = df.drop(df.columns[[1,13,12]],axis=1)

# 3. Clean up empty rows
df = df.dropna(subset=['Narration']).reset_index(drop=True)
value_cols = [col for col in df.columns if col != 'Narration']

# Drop rows where ALL data columns are NaN
df = df.dropna(subset=value_cols, how='all').reset_index(drop=True)
print("Cleaned Data")
# Display loaded data
print(df)

df.to_csv('F:\\Downloads\\Affle_3i_Cleaned_Profit_Loss.csv', index=False)

