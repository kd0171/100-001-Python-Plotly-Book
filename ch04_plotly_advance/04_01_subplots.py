import plotly.graph_objects as go
from plotly.subplots import make_subplots

line_trace = go.Scatter(
    x=[0, 1, 2],
    y=[5, 3, 4], 
    name="line" # 凡例 (legend) に表示される名前
)
scatter_trace = go.Scatter(
    x=[1, 2, 3], y=[2, 1, 5], mode="markers", name="scatter"
)
bar_trace = go.Bar(x=[1, 2, 3], y=[1, 2, 3], name="bar")
area_trace = go.Scatter(
    x=[3, 4, 5],
    y=[5, 3, 4],
    mode="none",
    fillcolor="#1f77b4",
    fill="tozeroy",
    name="area",
)

# ------------------------------------------------------------
# サブプロットの表示

# subplots_fig = make_subplots(rows=2, cols=2)
# # specs を指定しなくても動作します。
#     # 異なるタイプを同一Figure内に混在させる場合、specs の明示指定が必須
#     # Plotly は各 trace（トレース） の種類から、どんなサブプロット（subplot）軸が必要かを自動で推定してくれます。
#     # ただし、完全に自動判定に頼ると限界もあります。
#     # specs を指定しないと、Plotly は自動的に "xy" と判断
# subplots_fig.add_trace(line_trace, row=1, col=1)
# subplots_fig.add_trace(scatter_trace, row=1, col=2)
# subplots_fig.add_trace(bar_trace, row=2, col=1)
# subplots_fig.add_trace(area_trace, row=2, col=2)
# subplots_fig.show()


# ------------------------------------------------------------

# # 複雑なサブプロットの表示
# complex_fig = make_subplots(
#     rows=4,
#     cols=2,
#     # ❶
#     specs=[
#         # 1行目
#         [{}, {"rowspan": 2}],  # ❷ 行結合
#         # 2行目
#         [{}, None],
#         # 3行目
#         [{"colspan": 2}, None],  # ❸ 列結合
#         [{"colspan": 2}, None],  # ❸ 列結合
#     ],
#     shared_xaxes=True,  # 同じ col にあるサブプロット同士で X軸を共有する（列結合の場合はmatchesでグループ化する必要）
#     column_widths=[0.6, 0.4],  # 幅に割り当てる割合を指定
#     row_heights=[0.3, 0.3, 0.2, 0.2],  # 高さに割り当てる割合を指定
# )
# complex_fig.add_trace(line_trace, row=1, col=1)
# complex_fig.add_trace(scatter_trace, row=1, col=2)
# complex_fig.add_trace(bar_trace, row=2, col=1)
# complex_fig.add_trace(area_trace, row=3, col=1)

# area_trace_sharedX = go.Scatter(
#     x=[1, 3, 4],
#     y=[2, 6, 1],
#     mode="none",
#     fillcolor="red",
#     fill="tozeroy",
#     name="area",
# )
# complex_fig.add_trace(area_trace_sharedX, row=4, col=1)
# complex_fig.update_xaxes(matches='x', row=3, col=1)  # 3行目ワイドのX軸をグループ'x'に（matches は 'x' / 'x2' / 'x3' ... だけ有効、自由に命名できない）
# complex_fig.update_xaxes(matches='x', row=4, col=1)  # 4行目ワイドも同じグループに
# complex_fig.show()


# ------------------------------------------------------------
# 座標系を指定したサブプロット

barpolar_trace = go.Barpolar(theta=[0, 60, 180], r=[6, 5, 3], name="barpolar") # Plotlyがデータ点間の角度差から自動的にバーの幅を決定します。
pie_trace = go.Pie(values=[30, 60, 10], labels=["a", "b", "c"], name="pie")
scatter3d_trace = go.Scatter3d(
    x=[1, 2, 3],
    y=[5, 3, 4],
    z=[2, 5, 1],
    mode="markers",
    marker={"size": 2},
    name="3D scatter",
)
multiple_types_fig = make_subplots(
    rows=2,
    cols=2,
    specs=[
        [{"type": "xy"}, {"type": "polar"}],
        [{"type": "domain"}, {"type": "scene"}],
    ],
)
multiple_types_fig.add_trace(scatter_trace, row=1, col=1)
multiple_types_fig.add_trace(barpolar_trace, row=1, col=2)
multiple_types_fig.add_trace(pie_trace, row=2, col=1)
multiple_types_fig.add_trace(scatter3d_trace, row=2, col=2)
multiple_types_fig.show()

# | `specs["type"]` | 座標系の種類        | 主な対応トレース                         |
# | --------------- | ----------         | -------------------------------- |
# | `"xy"`          | 2D 直交座標         | Scatter, Bar, Box, Heatmap, etc. |
# | `"domain"`      | 軸なし（ドメイン型） | Pie, Treemap, Sunburst, Sankey   |
# | `"polar"`       | 極座標              | Scatterpolar, Barpolar           |
# | `"scene"`       | 3D 座標             | Scatter3d, Surface, Mesh3d       |
# | `"ternary"`     | 三角座標            | Scatterternary                   |
# | `"geo"`         | 地理座標（平面投影） | Scattergeo, Choropleth           |
# | `"mapbox"`      | Mapbox地図上        | Scattermapbox, Choroplethmapbox  |
# | `"carpet"`      | 非直交座標          | Scattercarpet, Contourcarpet     |


# ------------------------------------------------------------




# ------------------------------------------------------------




# ------------------------------------------------------------




# ------------------------------------------------------------




# ------------------------------------------------------------




# ------------------------------------------------------------




# ------------------------------------------------------------




# ------------------------------------------------------------




# ------------------------------------------------------------




# ------------------------------------------------------------




# ------------------------------------------------------------




# ------------------------------------------------------------



