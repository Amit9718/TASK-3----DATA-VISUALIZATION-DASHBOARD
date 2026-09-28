# 📊 Data Visualization Dashboard

A Python-based data visualization project covering all major chart types using **Matplotlib**, **Seaborn**, and **Plotly**, plus an interactive browser dashboard.

---

## Project Structure

```
├── data_visualizations.py   # Static charts (Matplotlib + Seaborn)
├── plotly_dashboard.py      # Interactive HTML dashboard (Plotly)
├── dashboard.html           # Generated interactive dashboard
├── 1_bar_chart.png
├── 2_line_chart.png
├── 3_pie_chart.png
├── 4_histogram.png
├── 5_scatter_plot.png
├── 6_heatmap_boxplot.png
└── README.md
```

---

## Requirements

Python 3.8+ and the following libraries:

```bash
pip install matplotlib seaborn plotly pandas numpy
```

---

## Usage

### Static Charts
```bash
python data_visualizations.py
```
Generates 6 PNG chart files in the current directory.

### Interactive Dashboard
```bash
python plotly_dashboard.py
```
Generates `dashboard.html` — open it in any browser.

---

## Charts Included

| # | Chart | Library | Insight |
|---|-------|---------|---------|
| 1 | Bar Chart | Matplotlib | Annual sales per category (vertical + horizontal) |
| 2 | Line Chart | Matplotlib | Monthly sales trends with peak annotations |
| 3 | Pie / Donut | Matplotlib | Market share breakdown by category |
| 4 | Histogram | Seaborn | Revenue distribution with KDE, mean & median lines |
| 5 | Scatter Plot | Seaborn | Ad spend vs revenue with regression trend line |
| 6 | Heatmap + Boxplot | Seaborn | Category correlations and monthly spread |
| 7 | Interactive Dashboard | Plotly | All charts in one browser-based dashboard |

---

## Interactive Dashboard Features

- Hover tooltips on every data point
- Zoom, pan, and reset controls
- Legend toggle to show/hide categories
- Fully self-contained HTML (no server required)
- 6 panels: Bar, Line, Donut, Histogram, Scatter, Heatmap

---

## Dataset

Uses synthetically generated retail sales data:
- **12 months** × **5 categories** (Electronics, Clothing, Food, Sports, Books)
- Monthly revenue range: $20,000 – $120,000
- 80 data points for advertising spend vs revenue scatter analysis

---

## Customization

All charts share a consistent color palette defined at the top of each file:

```python
PALETTE = ["#4C72B0", "#DD8452", "#55A868", "#C44E52", "#8172B3"]
```

Swap in your own data by replacing the `sales_data` DataFrame and `scatter_df` with real datasets.
