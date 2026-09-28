"""
Interactive Plotly Dashboard
Opens in your default browser as a self-contained HTML file.
"""

import numpy as np
import pandas as pd
import plotly.graph_objects as go
import plotly.express as px
from plotly.subplots import make_subplots
import warnings

warnings.filterwarnings("ignore")

np.random.seed(42)

# ── Dataset ───────────────────────────────────────────────────────────────────
months     = ["Jan", "Feb", "Mar", "Apr", "May", "Jun",
              "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"]
categories = ["Electronics", "Clothing", "Food", "Sports", "Books"]
PALETTE    = ["#4C72B0", "#DD8452", "#55A868", "#C44E52", "#8172B3"]

sales_data = pd.DataFrame(
    np.random.randint(20_000, 120_000, size=(12, 5)),
    columns=categories,
    index=months,
)
total_sales = sales_data.sum()

ad_spend    = np.random.uniform(5_000, 50_000, 80)
revenue     = ad_spend * np.random.uniform(2.5, 4.5, 80) + np.random.normal(0, 15_000, 80)
product_cat = np.random.choice(categories, 80)
scatter_df  = pd.DataFrame({"Ad Spend ($)": ad_spend,
                             "Revenue ($)": revenue,
                             "Category": product_cat})

# ── Dashboard layout: 3 rows × 2 cols ────────────────────────────────────────
fig = make_subplots(
    rows=3, cols=2,
    subplot_titles=(
        "📊 Annual Sales — Bar Chart",
        "📈 Monthly Trends — Line Chart",
        "🍩 Market Share — Donut Chart",
        "📉 Revenue Distribution — Histogram",
        "⚡ Ad Spend vs Revenue — Scatter",
        "🔥 Category Correlation — Heatmap",
    ),
    specs=[
        [{"type": "xy"},   {"type": "xy"}],
        [{"type": "pie"},  {"type": "xy"}],
        [{"type": "xy"},   {"type": "xy"}],
    ],
    vertical_spacing=0.12,
    horizontal_spacing=0.10,
)

# ── 1. Bar chart ──────────────────────────────────────────────────────────────
for i, (cat, color) in enumerate(zip(categories, PALETTE)):
    fig.add_trace(
        go.Bar(
            name=cat,
            x=[cat],
            y=[total_sales[cat] / 1_000],
            marker_color=color,
            text=[f"${total_sales[cat]/1_000:.0f}K"],
            textposition="outside",
            showlegend=False,
        ),
        row=1, col=1,
    )

# ── 2. Line chart ─────────────────────────────────────────────────────────────
for i, (cat, color) in enumerate(zip(categories, PALETTE)):
    fig.add_trace(
        go.Scatter(
            name=cat,
            x=months,
            y=sales_data[cat] / 1_000,
            mode="lines+markers",
            line=dict(color=color, width=2),
            marker=dict(size=5),
        ),
        row=1, col=2,
    )

# ── 3. Donut chart ────────────────────────────────────────────────────────────
fig.add_trace(
    go.Pie(
        labels=categories,
        values=total_sales.values,
        hole=0.45,
        marker=dict(colors=PALETTE, line=dict(color="white", width=2)),
        textinfo="percent+label",
        showlegend=False,
    ),
    row=2, col=1,
)

# ── 4. Histogram ──────────────────────────────────────────────────────────────
all_sales = sales_data.values.flatten() / 1_000
fig.add_trace(
    go.Histogram(
        x=all_sales,
        nbinsx=20,
        marker_color=PALETTE[0],
        opacity=0.8,
        name="Revenue Dist",
        showlegend=False,
    ),
    row=2, col=2,
)
mean_val = np.mean(all_sales)
# Mean line as a scatter trace (add_vline doesn't work alongside pie subplots)
fig.add_trace(
    go.Scatter(
        x=[mean_val, mean_val],
        y=[0, 12],
        mode="lines",
        line=dict(color=PALETTE[3], dash="dash", width=2),
        name=f"Mean ${mean_val:.1f}K",
        showlegend=False,
    ),
    row=2, col=2,
)

# ── 5. Scatter plot ───────────────────────────────────────────────────────────
for i, (cat, color) in enumerate(zip(categories, PALETTE)):
    mask = scatter_df["Category"] == cat
    fig.add_trace(
        go.Scatter(
            name=cat,
            x=scatter_df.loc[mask, "Ad Spend ($)"] / 1_000,
            y=scatter_df.loc[mask, "Revenue ($)"] / 1_000,
            mode="markers",
            marker=dict(color=color, size=8, opacity=0.75,
                        line=dict(color="white", width=0.5)),
            showlegend=True,
        ),
        row=3, col=1,
    )

# ── 6. Heatmap ────────────────────────────────────────────────────────────────
corr_matrix = sales_data.corr().round(2)
fig.add_trace(
    go.Heatmap(
        z=corr_matrix.values,
        x=categories,
        y=categories,
        colorscale="RdYlGn",
        zmin=-1, zmax=1,
        text=corr_matrix.values,
        texttemplate="%{text}",
        showscale=True,
        showlegend=False,
    ),
    row=3, col=2,
)

# ── Axis labels ───────────────────────────────────────────────────────────────
fig.update_yaxes(title_text="Revenue ($ thousands)", row=1, col=1)
fig.update_yaxes(title_text="Revenue ($ thousands)", row=1, col=2)
fig.update_yaxes(title_text="Frequency",             row=2, col=2)
fig.update_xaxes(title_text="Monthly Revenue ($ K)", row=2, col=2)
fig.update_xaxes(title_text="Ad Spend ($ thousands)", row=3, col=1)
fig.update_yaxes(title_text="Revenue ($ thousands)", row=3, col=1)

# ── Global layout ─────────────────────────────────────────────────────────────
fig.update_layout(
    title=dict(
        text="<b>📊 Sales Analytics Dashboard</b>",
        x=0.5,
        font=dict(size=22),
    ),
    height=1050,
    paper_bgcolor="#F8F9FA",
    plot_bgcolor="#FFFFFF",
    font=dict(family="Segoe UI, Arial", size=11),
    legend=dict(
        orientation="h",
        yanchor="bottom",
        y=-0.06,
        xanchor="center",
        x=0.5,
        bgcolor="rgba(255,255,255,0.8)",
        bordercolor="#ddd",
        borderwidth=1,
    ),
    hoverlabel=dict(bgcolor="white", font_size=12),
    barmode="group",
)

# ── Export ────────────────────────────────────────────────────────────────────
output_file = "dashboard.html"
fig.write_html(
    output_file,
    include_plotlyjs="cdn",
    full_html=True,
    config={"responsive": True, "displayModeBar": True},
)
print(f"✓  Interactive dashboard saved → {output_file}")
print("   Open it in any browser to explore all charts.")
