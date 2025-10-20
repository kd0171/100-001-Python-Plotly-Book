import plotly.graph_objects as go

# ------------------------------------------------------------

# # Figureオブジェクトの表示（showメソッド）
# fig = go.Figure()
# fig.show()


# ------------------------------------------------------------

# # traceオブジェクト（グラフ本体に関する情報）をFigureのdataとして登録
# scatter_trace = go.Scatter(x=[1,2,3], y=[3,1,6])
# scatter_fig = go.Figure(data=scatter_trace)
# scatter_fig.show()

# # 複数のtraceオブジェクトを一つのFigureオブジェクト上に表示
# bar_trace = go.Bar(x=[1,2,3], y=[5,3,1])
# scatter_bar_fig = go.Figure(data=[scatter_trace,bar_trace]) # dataに複数のtraceオブジェクトを渡す場合は、[]を用いる
# scatter_bar_fig.show()

# ------------------------------------------------------------

# # layoutによるスタイルの変更
# layout = go.Layout(width=300,height=300)
# scatter_trace = go.Scatter(x=[1,2,3], y=[3,1,6])
# fix_size_fig = go.Figure(data=scatter_trace, layout=layout)
# fix_size_fig.show()


# ------------------------------------------------------------

# #　（chatgpt）様々なレイアウトの設定
# layout = go.Layout(
#     width=600,
#     height=600,
#     title="Sample Graph",
#     title_font=dict(size=16, color="blue"),
#     title_x=0.5,  # タイトル位置（0=左, 0.5=中央, 1=右）
#     plot_bgcolor="lightblue",   # グラフ内（プロット領域）
#     paper_bgcolor="rgb(255,255,255)",   # 外側（余白・タイトル部分）
#     showlegend=True,
#     legend=dict(
#         x=0.05, y=0.95,  # 位置（相対座標）
#         bgcolor="rgba(255,255,255,0.5)",  # 半透明背景
#         bordercolor="black",
#         borderwidth=2
#     ),
#     xaxis=dict(showgrid=True, gridcolor="green"), # 縦のグリッド線
#     yaxis=dict(zeroline=True, zerolinecolor="red")
#     )
# scatter_trace = go.Scatter(x=[1,2,3], y=[-3,1,6])
# fix_size_fig = go.Figure(data=scatter_trace, layout=layout)
# fix_size_fig.show()


# ------------------------------------------------------------

# # テンプレートを用いたグラフの表示
# layout = go.Layout(template="seaborn")
# scatter_trace = go.Scatter(x=[1,2,3], y=[3,1,6])
# fix_size_fig = go.Figure(data=scatter_trace, layout=layout)
# fix_size_fig.show()

# テンプレートには "plotly", "plotly_dark", "ggplot2", "seaborn" などが用意

# ------------------------------------------------------------



