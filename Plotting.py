import pandas as pd
import matplotlib.pyplot as plt

# 1. Load the CSV file starting at line 3 (header=2)
file_path = 'F:\\Downloads\\Affle_3i_Cleaned_Profit_Loss.csv'
df = pd.read_csv(file_path)

# 2. Extract the OPM row


# Define financial year columns to plot
year_cols = [col for col in df.columns if col not in ('Narration', 'Trailing')]

# 3. Clean percentage strings into numeric values
opm_values = pd.to_numeric(df[df['Narration'] == 'OPM'][year_cols].iloc[0].astype(str).str.replace('%', ''), errors='coerce')
# 4. Generate line plot
plt.figure(figsize=(10, 5))
plt.plot(year_cols, opm_values, marker='o', color='#2b5c8f', linewidth=2, markersize=8)

# Styling and labels
plt.title('Operating Profit Margin (OPM %) Trend', fontsize=14, fontweight='bold', pad=15)
plt.xlabel('Financial Year', fontsize=12)
plt.ylabel('OPM (%)', fontsize=12)
plt.grid(True, linestyle='--', alpha=0.6)
plt.ylim(15, 40)

# Add value labels above each data point
for year, val in zip(year_cols, opm_values):
    plt.annotate(f'{val:.2f}%', (year, val), textcoords="offset points", xytext=(0, 10), ha='center', fontsize=9, fontweight='bold')

plt.tight_layout()
plt.show()