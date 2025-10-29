import plotly.graph_objects as go
import numpy as np

# ------------------------------------------------------------
# # traceによるテキストの描画
#     # インデックスごとに座標を指定してテキストを描画
# go.Figure(
#     go.Scatter(
#         x=[1,2,3],
#         y=[3,5,2],
#         text=["A","B","C"],
#         mode="text",
#         textfont={"size":20},
#     )
# ).show()

# ------------------------------------------------------------

# # テキスト位置の調整

# textpositions = [
#     "top left",
#     "top center",
#     "top right",
#     "middle left",
#     "middle center",
#     "middle right",
#     "bottom left",
#     "bottom center",
#     "bottom right",
# ]
# fix_text_position_fig = go.Figure(layout={"showlegend":False}) # 凡例（legend） を非表示にする設定
# for i, textposition in enumerate(textpositions):
#     fix_text_position_fig.add_trace(
#         go.Scatter(
#             x=[1,2,3],
#             y=[i,i,i],
#             text=[None, textposition, None],
#             mode="lines+markers+text",
#             textposition=textposition,
#         )
#     )
# # 散布図（Scatter plot） を作るオブジェクト。
# # ただし、mode を "lines+markers+text" にしているので、
#     # lines（線）
#     # markers（点）
#     # text（文字）
# # の3要素を同時に表示

# fix_text_position_fig.show()

# ------------------------------------------------------------

# # アノテーション（テキストとある特定の位置を矢印で結ぶ）
# annotate_text_fig = go.Figure()
# annotate_text_fig.add_trace(go.Scatter(x=[1,2,3],y=[3,5,2],mode="lines"))
# annotate_text_fig.update_layout(
#     annotations=[   # annotations は アノテーションのリスト（list of annotations） 
#         go.layout.Annotation(
#             x=2, y=5, # 矢印の先が示す位置
#             text="max=5", # テキスト内容
#             showarrow=True,  # 矢印を表示
#             arrowhead=1,  # 矢印の形状
#             bgcolor="midnightblue",  # テキスト部分の塗りつぶし色
#             font={"size": 15, "color": "white"},  # フォントサイズと色
#         ),
#         go.layout.Annotation(
#             x=3,
#             y=2,
#             text="min=2",
#             showarrow=True,
#             arrowhead=1,
#             bgcolor="mediumvioletred",
#             font={"size": 15, "color": "white"},
#         ),
#     ]
# ).show()

# ------------------------------------------------------------

# # アノテーションのメリット

# paper_fig = go.Figure()
# paper_fig.update_layout(
#     annotations=[     # アノテーションリストにアノテーションオブジェクトを格納
#         go.layout.Annotation(
#             # 描画領域を基準
#             xref="paper",
#             yref="paper",
#             x=0.5,
#             y=0.5,
#             showarrow=False,
#             text="領域内に描画",
#         ),
#         go.layout.Annotation(
#             xref="paper",
#             yref="paper",
#             x=0.25,
#             y=-0.1,
#             showarrow=False,
#             text="領域外に描画",
#         ),
#     ]
# )
# paper_fig.show()

# テキストをトレースで書くのが望ましくない理由
    # | 特徴           | 内容                                                      |
    # | ------------ | ------------------------------------------------------- |
    # | **レイアウト基準**  | 軸のスケールやデータ値に関係なく、常に同じ位置に描画可能（例：タイトル横）                   |
    # | **装飾が豊富**    | `arrow`, `bgcolor`, `bordercolor`, `font` など細かい見た目を指定可能 |
    # | **データと独立**   | データが変わっても位置が固定される（補助説明・注釈に向く）                           |
    # | **配置基準が選べる** | `xref="x"`, `yref="y"` にすればデータ座標基準に変更も可能                |

# アノテーションならズームインやズームアウトといった操作とも独立して動かない

# ------------------------------------------------------------

# # 図形の描画

# rect_fig = go.Figure()
# rect_fig.add_trace(go.Scatter(x=[1, 2, 3], y=[3, 5, 2]))
# rect_fig.update_layout(
#     shapes=[
#         go.layout.Shape(
#             type="rect",  # 長方形
#             xref="x",  # X座標
#             yref="paper",  # 描画領域からの相対位置（0-1までで指定）
#             x0=1.8,  # X座標の開始位置
#             x1=2.2,  # X座標の終了位置
#             y0=0,  # Y座標の開始位置
#             y1=1,  # Y座標の終了位置
#             fillcolor="LightSalmon",  # 塗りつぶし色
#             opacity=0.5,  # 不透明度
#             layer="below",  # traceの背面に描画
#             line={"width": 0},  # 枠線を表示しない
#             # line={"width": 3, "color":"red"},  # 枠線を表示
#         )
#     ]
# )
# rect_fig.show()

# ------------------------------------------------------------

# # 散布図に楕円を重ねて描画

# np.random.seed(1)
# x0 = np.random.normal(2, 0.45, 300)
# y0 = np.random.normal(2, 0.45, 300)
# x1 = np.random.normal(6, 0.4, 200)
# y1 = np.random.normal(6, 0.4, 200)

#     # | 引数           | 意味                       | 英語                 |
#     # | ------------ | ------------------------ | ------------------ |
#     # | `loc=2`      | 平均値（mean）                | mean               |
#     # | `scale=0.45` | 標準偏差（standard deviation） | standard deviation |
#     # | `size=300`   | 生成するサンプル数                | sample size        |


# circle0 = go.layout.Shape(
#     type="circle",  # 円を描画
#     # 円の外接矩形の左下 (x0, y0) と 右上 (x1, y1) を指定
#     x0=min(x0),
#     y0=min(y0),
#     x1=max(x0),
#     y1=max(y0),
#     opacity=0.2,
#     fillcolor="blue",
#     line={"width": 0},
# )
# circle1 = go.layout.Shape(
#     type="circle",
#     x0=min(x1),
#     y0=min(y1),
#     x1=max(x1),
#     y1=max(y1),
#     opacity=0.2,
#     fillcolor="orange",
#     line={"width": 0},
# )
# circle_fig = go.Figure()
# circle_fig.add_trace(go.Scatter(x=x0, y=y0, mode="markers", name="groupA"))
# circle_fig.add_trace(go.Scatter(x=x1, y=y1, mode="markers", name="groupB"))
# circle_fig.update_layout(shapes=[circle0, circle1])
# circle_fig.show()

# ------------------------------------------------------------

# SVG（Scalable Vector Graphics）での描画
    # type="path" にすることで、円・長方形・線といった定型の図形ではなく、
    # SVG（Scalable Vector Graphics）の path コマンドを直接使って図形を定義

svg_fig = go.Figure()
svg_fig.update_layout(
    shapes=[
        go.layout.Shape(
            type="path",  # SVGパスを指定
            path=" M 1 1 L 1 3 L 4 1 Z",  # ❶ SVGパス
            fillcolor="LightPink",
        )
    ]
)
# SVGのパス命令（path command）の解説
    # | コマンド    | 意味             | 内容                       |
    # | ------- | -------------- | ------------------------ |
    # | `M 1 1` | **Move to**    | ペンを座標 (1, 1) に移動（描画はしない） |
    # | `L 1 3` | **Line to**    | (1, 3) まで直線を描く           |
    # | `L 4 1` | **Line to**    | (4, 1) まで直線を描く           |
    # | `Z`     | **Close path** | 始点 (1, 1) に戻って閉じる        |

svg_fig.show()

# ------------------------------------------------------------



# ------------------------------------------------------------



# ------------------------------------------------------------



# ------------------------------------------------------------



# ------------------------------------------------------------



# ------------------------------------------------------------



# ------------------------------------------------------------



# ------------------------------------------------------------

