import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# 1. Read the cleaned CSV file
file_path = 'F:\\Downloads\\Affle_3i_Cleaned_Profit_Loss.csv'
df = pd.read_csv(file_path)

# 2. Extract year columns dynamically
year_cols = [col for col in df.columns if col not in ('Narration', 'Trailing')]

# 3. Extract EPS and Price to Earning rows
eps_series = df[df['Narration'] == 'EPS'][year_cols].iloc[0]
pe_series = df[df['Narration'] == 'Price to earning'][year_cols].iloc[0]
print(eps_series)
print(pe_series)
# 4. Clean numeric data safely
eps_values = pd.to_numeric(
    eps_series.astype(str).str.replace(',', '', regex=False).str.strip(), 
    errors='coerce'
)
pe_values = pd.to_numeric(
    pe_series.astype(str).str.replace(',', '', regex=False).str.strip(), 
    errors='coerce'
)

# 5. Create figure and primary axis (for EPS bars)
fig, ax1 = plt.subplots(figsize=(10, 5))

color_eps = '#2b5c8f'
bars = ax1.bar(year_cols, eps_values, color=color_eps, alpha=0.75, width=0.45, label='EPS')
ax1.set_xlabel('Financial Year', fontsize=12, fontweight='bold')
ax1.set_ylabel('EPS', color=color_eps, fontsize=12, fontweight='bold')
ax1.tick_params(axis='y', labelcolor=color_eps)
ax1.set_ylim(0, np.nanmax(eps_values) * 1.25)

# Add numeric annotations on top of EPS bars
for bar in bars:
    height = bar.get_height()
    if not np.isnan(height) and height > 0:
        ax1.annotate(
            f'{height:.2f}',
            xy=(bar.get_x() + bar.get_width() / 2, height),
            xytext=(0, 3),
            textcoords="offset points",
            ha='center', va='bottom', fontsize=8, fontweight='bold', color=color_eps
        )

# 6. Create secondary Y-axis (for Price to Earning line)
ax2 = ax1.twinx()

color_pe = '#e74c3c'
ax2.plot(year_cols, pe_values, color=color_pe, marker='o', linewidth=2.5, markersize=7, label='Price to Earning')
ax2.set_ylabel('Price to Earning (P/E)', color=color_pe, fontsize=12, fontweight='bold')
ax2.tick_params(axis='y', labelcolor=color_pe)
ax2.set_ylim(0, np.nanmax(pe_values) * 1.2)

# Add numeric annotations for Price to Earning line
for year, val in zip(year_cols, pe_values):
    if not np.isnan(val):
        ax2.annotate(
            f'{val:.1f}', 
            (year, val), 
            textcoords="offset points", 
            xytext=(0, 8), 
            ha='center', fontsize=8, fontweight='bold', color=color_pe
        )

# Graph styling
plt.title('EPS vs. Price to Earning (P/E) Trend', fontsize=14, fontweight='bold', pad=15)
ax1.grid(True, linestyle='--', alpha=0.4)

fig.tight_layout()
plt.show()