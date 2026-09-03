import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# 1. Load data
file_path = 'F:\\Downloads\\Affle_3i_Cleaned_Profit_Loss.csv'
df = pd.read_csv(file_path)

year_cols = [col for col in df.columns if col not in ('Narration', 'Trailing')]

# 2. Prepare series data
opm_values = pd.to_numeric(df[df['Narration'] == 'OPM'][year_cols].iloc[0].astype(str).str.replace('%', ''), errors='coerce')
eps_values = pd.to_numeric(df[df['Narration'] == 'EPS'][year_cols].iloc[0].astype(str).str.replace(',', ''), errors='coerce')
pe_values = pd.to_numeric(df[df['Narration'] == 'Price to earning'][year_cols].iloc[0].astype(str).str.replace(',', ''), errors='coerce')

# 3. Create a 1-row, 2-column figure layout
fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(16, 5))

# --------------------------------------------------
# LEFT CHART: OPM Trend (ax1)
# --------------------------------------------------
ax1.plot(year_cols, opm_values, marker='o', color='#2b5c8f', linewidth=2, markersize=7)
ax1.set_title('Operating Profit Margin (OPM %) Trend', fontsize=12, fontweight='bold', pad=12)
ax1.set_xlabel('Financial Year', fontsize=10, fontweight='bold')
ax1.set_ylabel('OPM (%)', fontsize=10, fontweight='bold')
ax1.grid(True, linestyle='--', alpha=0.4)
ax1.set_ylim(np.nanmin(opm_values) - 2, np.nanmax(opm_values) + 3)

for year, val in zip(year_cols, opm_values):
    if not np.isnan(val):
        ax1.annotate(f'{val:.1f}%', (year, val), textcoords="offset points", xytext=(0, 8), ha='center', fontsize=8, fontweight='bold')

# --------------------------------------------------
# RIGHT CHART: EPS vs P/E Dual Axis (ax2)
# --------------------------------------------------
color_eps = '#2b5c8f'
bars = ax2.bar(year_cols, eps_values, color=color_eps, alpha=0.75, width=0.45)
ax2.set_title('EPS vs. Price to Earning (P/E) Trend', fontsize=12, fontweight='bold', pad=12)
ax2.set_xlabel('Financial Year', fontsize=10, fontweight='bold')
ax2.set_ylabel('EPS', color=color_eps, fontsize=10, fontweight='bold')
ax2.tick_params(axis='y', labelcolor=color_eps)
ax2.set_ylim(0, np.nanmax(eps_values) * 1.25)

for bar in bars:
    height = bar.get_height()
    if not np.isnan(height) and height > 0:
        ax2.annotate(f'{height:.1f}', xy=(bar.get_x() + bar.get_width() / 2, height), xytext=(0, 3), textcoords="offset points", ha='center', va='bottom', fontsize=8, fontweight='bold', color=color_eps)

# Secondary axis for P/E on right chart
ax_pe = ax2.twinx()
color_pe = '#e74c3c'
ax_pe.plot(year_cols, pe_values, color=color_pe, marker='o', linewidth=2, markersize=6)
ax_pe.set_ylabel('Price to Earning (P/E)', color=color_pe, fontsize=10, fontweight='bold')
ax_pe.tick_params(axis='y', labelcolor=color_pe)
ax_pe.set_ylim(0, np.nanmax(pe_values) * 1.2)

for year, val in zip(year_cols, pe_values):
    if not np.isnan(val):
        ax_pe.annotate(f'{val:.1f}', (year, val), textcoords="offset points", xytext=(0, 6), ha='center', fontsize=8, fontweight='bold', color=color_pe)

ax2.grid(True, linestyle='--', alpha=0.4)

fig.tight_layout()
plt.show()