"""
Data Visualization Dashboard
Covers: Bar, Line, Pie, Histogram, Scatter charts
Libraries: Matplotlib, Seaborn, Plotly
"""

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.ticker as mticker
import seaborn as sns
import warnings

warnings.filterwarnings("ignore")

# ── Shared color palette ──────────────────────────────────────────────────────
PALETTE = ["#4C72B0", "#DD8452", "#55A868", "#C44E52", "#8172B3", "#937860"]
sns.set_theme(style="whitegrid", palette=PALETTE)

# ── Sample dataset: Monthly sales by product category ────────────────────────
np.random.seed(42)
months = ["Jan", "Feb", "Mar", "Apr", "May", "Jun",
          "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"]
categories = ["Electronics", "Clothing", "Food", "Sports", "Books"]

sales_data = pd.DataFrame(
    np.random.randint(20_000, 120_000, size=(12, 5)),
    columns=categories,
    index=months,
)

# Scatter dataset: advertising spend vs revenue
ad_spend   = np.random.uniform(5_000, 50_000, 80)
revenue    = ad_spend * np.random.uniform(2.5, 4.5, 80) + np.random.normal(0, 15_000, 80)
product_cat = np.random.choice(categories, 80)

scatter_df = pd.DataFrame({"Ad Spend ($)": ad_spend,
                            "Revenue ($)": revenue,
                            "Category": product_cat})

# ─────────────────────────────────────────────────────────────────────────────
# 1.  BAR CHART  –  total annual sales per category
# ─────────────────────────────────────────────────────────────────────────────
fig, axes = plt.subplots(1, 2, figsize=(14, 5))
fig.suptitle("Annual Sales by Category", fontsize=16, fontweight="bold", y=1.02)

total_sales = sales_data.sum()

# Vertical bar
bars = axes[0].bar(total_sales.index, total_sales.values / 1_000,
                   color=PALETTE, edgecolor="white", linewidth=0.8)
axes[0].set_title("Total Sales (Vertical)", fontsize=13)
axes[0].set_xlabel("Category")
axes[0].set_ylabel("Revenue ($ thousands)")
axes[0].yaxis.set_major_formatter(mticker.FuncFormatter(lambda x, _: f"${x:.0f}K"))
for bar in bars:
    h = bar.get_height()
    axes[0].text(bar.get_x() + bar.get_width() / 2, h + 2,
                 f"${h:.0f}K", ha="center", va="bottom", fontsize=9)

# Horizontal bar
axes[1].barh(total_sales.index, total_sales.values / 1_000,
             color=PALETTE, edgecolor="white", linewidth=0.8)
axes[1].set_title("Total Sales (Horizontal)", fontsize=13)
axes[1].set_xlabel("Revenue ($ thousands)")
axes[1].xaxis.set_major_formatter(mticker.FuncFormatter(lambda x, _: f"${x:.0f}K"))
axes[1].invert_yaxis()

plt.tight_layout()
plt.savefig("1_bar_chart.png", dpi=150, bbox_inches="tight")
plt.close()
print("✓  Saved 1_bar_chart.png")

# ─────────────────────────────────────────────────────────────────────────────
# 2.  LINE CHART  –  monthly sales trends per category
# ─────────────────────────────────────────────────────────────────────────────
fig, ax = plt.subplots(figsize=(13, 6))

for i, cat in enumerate(categories):
    ax.plot(months, sales_data[cat] / 1_000, marker="o", linewidth=2.2,
            markersize=5, label=cat, color=PALETTE[i])

ax.set_title("Monthly Sales Trends by Category", fontsize=15, fontweight="bold")
ax.set_xlabel("Month", fontsize=11)
ax.set_ylabel("Revenue ($ thousands)", fontsize=11)
ax.yaxis.set_major_formatter(mticker.FuncFormatter(lambda x, _: f"${x:.0f}K"))
ax.legend(title="Category", bbox_to_anchor=(1.01, 1), loc="upper left")
ax.grid(axis="y", alpha=0.4)

# highlight peak month per category
for i, cat in enumerate(categories):
    peak_idx = sales_data[cat].idxmax()
    peak_val = sales_data[cat].max() / 1_000
    ax.annotate(f"Peak\n{peak_idx}",
                xy=(months.index(peak_idx), peak_val),
                xytext=(months.index(peak_idx), peak_val + 4),
                arrowprops=dict(arrowstyle="->", color=PALETTE[i], lw=1.2),
                fontsize=7, color=PALETTE[i], ha="center")

plt.tight_layout()
plt.savefig("2_line_chart.png", dpi=150, bbox_inches="tight")
plt.close()
print("✓  Saved 2_line_chart.png")

# ─────────────────────────────────────────────────────────────────────────────
# 3.  PIE CHART  –  market share breakdown
# ─────────────────────────────────────────────────────────────────────────────
fig, axes = plt.subplots(1, 2, figsize=(14, 6))
fig.suptitle("Market Share by Category", fontsize=15, fontweight="bold")

explode = [0.05] * len(categories)

# Standard pie
wedges, texts, autotexts = axes[0].pie(
    total_sales,
    labels=categories,
    autopct="%1.1f%%",
    colors=PALETTE,
    explode=explode,
    startangle=140,
    pctdistance=0.82,
    wedgeprops=dict(edgecolor="white", linewidth=1.5),
)
for autotext in autotexts:
    autotext.set_fontsize(9)
axes[0].set_title("Pie Chart", fontsize=12)

# Donut chart
wedges2, _, autotexts2 = axes[1].pie(
    total_sales,
    autopct="%1.1f%%",
    colors=PALETTE,
    explode=explode,
    startangle=140,
    pctdistance=0.82,
    wedgeprops=dict(width=0.5, edgecolor="white", linewidth=1.5),
)
for autotext in autotexts2:
    autotext.set_fontsize(9)
axes[1].legend(wedges2, categories, title="Category",
               loc="lower center", bbox_to_anchor=(0.5, -0.12),
               ncol=3, fontsize=9)
axes[1].set_title("Donut Chart", fontsize=12)

plt.tight_layout()
plt.savefig("3_pie_chart.png", dpi=150, bbox_inches="tight")
plt.close()
print("✓  Saved 3_pie_chart.png")

# ─────────────────────────────────────────────────────────────────────────────
# 4.  HISTOGRAM  –  revenue distribution
# ─────────────────────────────────────────────────────────────────────────────
fig, axes = plt.subplots(1, 2, figsize=(14, 5))
fig.suptitle("Revenue Distribution", fontsize=15, fontweight="bold")

all_sales = sales_data.values.flatten() / 1_000

# Seaborn histogram + KDE
sns.histplot(all_sales, bins=20, kde=True, color=PALETTE[0],
             edgecolor="white", ax=axes[0])
axes[0].set_title("All Categories Combined", fontsize=12)
axes[0].set_xlabel("Monthly Revenue ($ thousands)", fontsize=10)
axes[0].set_ylabel("Frequency", fontsize=10)
axes[0].axvline(np.mean(all_sales), color=PALETTE[3], linestyle="--",
                linewidth=1.8, label=f"Mean: ${np.mean(all_sales):.1f}K")
axes[0].axvline(np.median(all_sales), color=PALETTE[2], linestyle=":",
                linewidth=1.8, label=f"Median: ${np.median(all_sales):.1f}K")
axes[0].legend()

# Overlapping histograms per category
for i, cat in enumerate(categories):
    sns.histplot(sales_data[cat] / 1_000, bins=8, kde=False,
                 color=PALETTE[i], alpha=0.55, label=cat, ax=axes[1])
axes[1].set_title("Per Category Overlay", fontsize=12)
axes[1].set_xlabel("Monthly Revenue ($ thousands)", fontsize=10)
axes[1].set_ylabel("Frequency", fontsize=10)
axes[1].legend(title="Category", fontsize=8)

plt.tight_layout()
plt.savefig("4_histogram.png", dpi=150, bbox_inches="tight")
plt.close()
print("✓  Saved 4_histogram.png")

# ─────────────────────────────────────────────────────────────────────────────
# 5.  SCATTER PLOT  –  ad spend vs revenue
# ─────────────────────────────────────────────────────────────────────────────
fig, axes = plt.subplots(1, 2, figsize=(14, 5))
fig.suptitle("Advertising Spend vs Revenue", fontsize=15, fontweight="bold")

# Seaborn scatter with regression line per category
sns.scatterplot(data=scatter_df, x="Ad Spend ($)", y="Revenue ($)",
                hue="Category", palette=PALETTE, s=70, alpha=0.8,
                edgecolor="white", ax=axes[0])
axes[0].set_title("By Category", fontsize=12)
axes[0].xaxis.set_major_formatter(mticker.FuncFormatter(lambda x, _: f"${x/1000:.0f}K"))
axes[0].yaxis.set_major_formatter(mticker.FuncFormatter(lambda x, _: f"${x/1000:.0f}K"))
axes[0].legend(title="Category", fontsize=8)

# Scatter with trend line (all data)
sns.regplot(data=scatter_df, x="Ad Spend ($)", y="Revenue ($)",
            scatter_kws={"alpha": 0.5, "color": PALETTE[0], "s": 60},
            line_kws={"color": PALETTE[3], "linewidth": 2},
            ax=axes[1])
corr = scatter_df[["Ad Spend ($)", "Revenue ($)"]].corr().iloc[0, 1]
axes[1].set_title(f"Trend Line  |  r = {corr:.2f}", fontsize=12)
axes[1].xaxis.set_major_formatter(mticker.FuncFormatter(lambda x, _: f"${x/1000:.0f}K"))
axes[1].yaxis.set_major_formatter(mticker.FuncFormatter(lambda x, _: f"${x/1000:.0f}K"))

plt.tight_layout()
plt.savefig("5_scatter_plot.png", dpi=150, bbox_inches="tight")
plt.close()
print("✓  Saved 5_scatter_plot.png")

# ─────────────────────────────────────────────────────────────────────────────
# 6.  BONUS  –  Seaborn heatmap (correlation / monthly matrix)
# ─────────────────────────────────────────────────────────────────────────────
fig, axes = plt.subplots(1, 2, figsize=(14, 5))
fig.suptitle("Advanced Seaborn Charts", fontsize=15, fontweight="bold")

# Correlation heatmap
corr_matrix = sales_data.corr()
mask = np.triu(np.ones_like(corr_matrix, dtype=bool))
sns.heatmap(corr_matrix, annot=True, fmt=".2f", cmap="RdYlGn",
            center=0, mask=mask, linewidths=0.5, ax=axes[0],
            cbar_kws={"shrink": 0.8})
axes[0].set_title("Category Correlation Heatmap", fontsize=12)

# Boxplot – monthly revenue spread
melted = sales_data.reset_index().melt(id_vars="index",
                                       var_name="Category",
                                       value_name="Revenue")
melted["Revenue"] /= 1_000
sns.boxplot(data=melted, x="Category", y="Revenue",
            palette=PALETTE, width=0.5, ax=axes[1])
axes[1].set_title("Monthly Revenue Spread per Category", fontsize=12)
axes[1].set_ylabel("Revenue ($ thousands)")
axes[1].yaxis.set_major_formatter(mticker.FuncFormatter(lambda x, _: f"${x:.0f}K"))
axes[1].tick_params(axis="x", rotation=15)

plt.tight_layout()
plt.savefig("6_heatmap_boxplot.png", dpi=150, bbox_inches="tight")
plt.close()
print("✓  Saved 6_heatmap_boxplot.png")

print("\nAll static charts saved. Run plotly_dashboard.py for the interactive dashboard.")
