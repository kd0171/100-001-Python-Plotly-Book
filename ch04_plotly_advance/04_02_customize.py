import plotly.graph_objects as go
from plotly.subplots import make_subplots
import numpy as np

x = [1, 2, 3]
line_y = [5, 3, 2]
scatter_y = [-2, 4, 3]
bar_y = [1, 3, 4]

# ------------------------------------------------------------

# line_trace = go.Scatter(
#     x=x,
#     y=line_y,
#     # 折れ線グラフのスタイル
#     # colorを16進数で指定
#     line={"width": 5, "color": "#1f77b4", "dash": "dashdot"},
#     opacity=0.4,  # 不透明度
#     name="line",
# )
# # line.dashでは、線の見た目について以下の指定が可能
#     # | 設定値（英語）                     | 日本語の意味 | 説明                  |
#     # | --------------------------- | ------ | ------------------- |
#     # | `solid`                     | 実線     | 途切れのない通常の線。デフォルト設定。 |
#     # | `dot`                       | 点線     | 点のように短く区切られた線。      |
#     # | `dash` または `longdash`       | 破線     | 一定間隔の短い線分と空白を繰り返す。  |
#     # | `dashdot` または `longdashdot` | 一点鎖線   | 破線と点線を交互に組み合わせた線。   |

# scatter_trace = go.Scatter(
#     x=x,
#     y=scatter_y,
#     mode="markers",
#     # 要素のスタイル
#     marker={
#         "size": 20,
#         # colorをrgbaで指定
#         "color": "rgba(255, 127, 14, 0.5)",
#         "line": {"width": 3, "color": "rgba(214, 39, 40, 0.5)"},
#     },
#     name="scatter",
# )
# bar_trace = go.Bar(
#     x=x,
#     y=bar_y,
#     width=0.3,
#     marker={
#         # colorをrgbで指定
#         "color": ["rgb(255, 127, 14)", "rgb(44, 160, 44)", "rgb(214, 39, 40)"],
#         "line": {"width": 3, "color": "black"},
#     },
#     opacity=0.4,  # 不透明度
#     name="bar",
# )
# layout = go.Layout(
#     # グラフタイトルのスタイル
#     # colorをCSSカラーネームで指定
#     title={
#         "text": "Title",
#         "font": {"family": "arial", "size": 20, "color": "green"},
#     },
#     # X軸のスタイル
#     xaxis={
#         "title": {
#             "text": "X軸",
#             "font": {"family": "arial", "size": 10, "color": "navy"},
#         },
#         "tickfont": {"family": "arial", "size": 10, "color": "olive"},
#         "tickangle": 45,
#         # tickangle：軸目盛ラベルの回転角度（度単位）。
#             # → 45° 傾けて表示。
#     },
#     # Y軸のスタイル
#     yaxis={
#         "title": {
#             "text": "Y軸",
#             "font": {"family": "arial", "size": 10, "color": "darkviolet"},
#         },
#         # 軸線まわりの設定
#         "showline": True, # showline: Y軸の主線（軸そのもの）を表示
#         "linewidth": 2, # linewidth: 軸線の太さ（ピクセル単位）
#         "linecolor": "darkgray",
#         # グリッド線まわり
#         "gridwidth": 1,
#         "gridcolor": "indianred",
#         # ゼロ線 (zeroline)
#         "zeroline": True, # zeroline: ゼロ線を表示
#         "zerolinewidth": 2,
#         "zerolinecolor": "indigo",
#     },
# )
# go.Figure([line_trace, scatter_trace, bar_trace], layout=layout).show()

# add_trace() と layout はどちらもグラフの見た目（スタイル）や設定に関係しますが、担当する範囲（責任範囲）が異なる
    # | 設定場所                                   | 影響する対象                                    | 主な用途                                                |
    # | -----------------------------------       | ----------------------------                   | ------------------------------                          |
    # | **`.add_trace()` 内（= 各 trace の設定）** | **データ系列（1本の線・1組の棒など）ごとの見た目** | 線の色・マーカーの形・透明度・凡例名などを設定              |
    # | **`layout`**                              | **グラフ全体や軸・タイトルなどの外観**            | タイトル、軸のラベル、グリッド線、フォント、背景色などを設定 |

# ------------------------------------------------------------

# # グラフサイズ、色、余白の設定
# fig = go.Figure(
#     go.Scatter(x=["2020-01-01","2020-01-02","2020-01-03"],y=[3,5,2])
# )
# fig.update_layout(
#     autosize=False, 
#     # 自動サイズ調整（autosize）をオフにします。
#     # これを False にすることで、次の width / height の指定が有効
#     width=300,
#     height=300,
#     margin={"l":50,"r":50,"b":50,"t":80,"pad":15}, # **グラフ領域外側の余白（margin）**を設定
#         # "pad": 全方向に追加する内側余白（グラフとグラフ描画領域の端までの距離）、l,r,b,tの値に加算される
#     paper_bgcolor="lightcoral", # 図全体（paper）の背景色を指定
#     xaxis={"title":{"text":"x"}},
#     yaxis={"title":{"text":"y"}}
# )
# fig.show()

# ------------------------------------------------------------

# # 軸の設定
# fig = make_subplots(rows=1,cols=2)
# fig.add_trace(
#     go.Scatter(x=["2010","2011","2012"],y=[1,10,10001],name="line"),row=1,col=1
# )
# fig.update_xaxes(type="date",row=1,col=1)
# fig.update_yaxes(type="log",row=1,col=1)
# # type の代表的な設定と用途
#     # | 値                 | 軸の種類     | データ例                        | 主な用途       |
#     # | -----------------  | ------      | ---------------------------    | ---------- |
#     # | `"linear"`         | 線形（数値） | 1, 2, 3, 4                     | 通常の数値データ   |
#     # | `"log"`            | 対数        | 1, 10, 100                     | 値の範囲が広いデータ |
#     # | `"date"`           | 日時        | `"2020-01-01"`, datetime       | 時系列データ     |
#     # | `"category"`       | カテゴリ     | `"A"`, `"B"`, `"C"`            | 区分データ      |
#     # | `"multicategory"`  | 階層カテゴリ | `[["1年","1年"],["A組","B組"]]` | 階層的カテゴリ    |


# # fig.add_trace(go.Bar(x=[["1年", "1年"], ["A組", "B組"]], y=[70, 60]), row=1, col=2)
# # fig.add_trace(go.Bar(x=[["2年", "2年"], ["A組", "B組"]], y=[70, 60]), row=1, col=2)
# # fig.update_xaxes(type="multicategory", row=1, col=2)  # 階層カテゴリ

# # Plotly は「上位階層」と「下位階層」の関係を、同じ値が複数回現れる構造から自動的に推定します
# # 以下のコードでも階層性は認識されるが、トレース毎に色を設定することができない
# # fig.add_trace(go.Bar(x=[["1年", "1年","2年", "2年"], ["A組", "B組","A組", "B組"]], y=[70, 60, 70, 60]), row=1, col=2)
# # トレース毎に分けることで以下のような設定が可能
# fig.add_trace(
#     go.Bar(
#         x=[["1年", "1年"], ["A組", "B組"]],
#         y=[70, 60],
#         name="1年",  # ← 凡例ラベル
#         marker_color="steelblue",  # ← 色指定
#     ), row=1, col=2
# )

# # 「2年」グループ
# fig.add_trace(
#     go.Bar(
#         x=[["2年", "2年"], ["A組", "B組"]],
#         y=[80, 65],
#         name="2年",
#         marker_color="orange",
#     ), row=1, col=2
# )

# fig.update_xaxes(type="multicategory", row=1, col=2)  # 階層カテゴリ
# fig.show()

# ------------------------------------------------------------

# # 2つのグラフを1つの図に描画して、両側に軸を書く
# two_yaxis_fig = make_subplots(specs=[[{"secondary_y":True}]])
#     # make_subplots(specs=[[{"secondary_y": True}]]) は、1つのサブプロットに右Y軸を追加するためのヘルパー
# two_yaxis_fig.add_trace(
#     go.Scatter(x=[1,2,3],y=[3,2,4],name="1st"),
# )
# two_yaxis_fig.add_trace(
#     go.Scatter(x=[1,2,3],y=[1,20,15],name="2nd"),
#     secondary_y=True,
# )
# two_yaxis_fig.update_yaxes(title={"text":"1st"},showgrid=False)
# two_yaxis_fig.update_yaxes(
#     secondary_y=True,
#     title={"text":"2nd"},
#     showgrid=False
# )
# two_yaxis_fig.show()

# ------------------------------------------------------------

# # 目盛りの位置の設定
# config_tick_fig = make_subplots(
#     rows=2,cols=2,
#     horizontal_spacing=0.15,
#     vertical_spacing=0.2
# )
# config_tick_fig.add_trace(go.Scatter(x=[1,2,3],y=[5,3,4]))
# config_tick_fig.update_xaxes(
#     tick0=2,
#     dtick=0.3,
#     title="2を基準に刻み幅は0.3",
#     row=1,
#     col=1
# )
# config_tick_fig.update_yaxes(
#     autorange="reversed",
#     title="y軸の順序を逆に設定",
#     row=1,
#     col=1
# )
# config_tick_fig.add_trace(
#     go.Scatter(x=[1,2,3],y=[5,3,4]),row=1,col=2
# )
# config_tick_fig.update_xaxes(
#     tickvals=[1.6,2,2.2],title="表示する目盛を指定",row=1,col=2
# )
# config_tick_fig.update_yaxes(
#     range=[2,4],title="描画範囲を指定（2-4）",row=1,col=2
# )
# config_tick_fig.add_trace(go.Scatter(x=[-1,0,1],y=[4,5,3]),row=2,col=1)
# config_tick_fig.update_xaxes(
#     rangemode="nonnegative",title="正の値の範囲のみを描画",row=2,col=1
# )
# config_tick_fig.update_yaxes(
#     rangemode="tozero", # データの最小値が0より大きくても、必ず0を含むように軸範囲を取る
#     title="0からの範囲を描画",row=2,col=1
# )
# config_tick_fig.show()


# | 値                 | 意味                  | 挙動                        |
# | ----------------- | ------------------- | ------------------------- |
# | `"normal"`（デフォルト） | データ範囲にぴったり合わせる      | 最小値～最大値                   |
# | `"tozero"`        | 範囲に0を含める            | min>0なら0～max、max<0ならmin～0 |
# | `"nonnegative"`   | 常に0以上の範囲を確保（負の値を無視） | min<0でも0から表示開始            |
    # rangemode="nonnegative" を指定すると、データに負の値が含まれていても Y軸は0以上から始まる 場合

# ------------------------------------------------------------

# # 凡例の非表示
# x = [1, 2, 3]
# various_legend_fig = go.Figure()
# various_legend_fig.add_trace(go.Scatter(x=x, y=[5, 3, 2])) 
# various_legend_fig.add_trace(go.Scatter(x=x, y=[4, 2, 3], name="line2")) 
# various_legend_fig.add_trace(
#     go.Scatter(x=x, y=[3, 5, 4], name="line3", 
#                showlegend=False, # 凡例を表示しない
#     ) 
# )
# various_legend_fig.show()


# ------------------------------------------------------------

# # 横並びの凡例と凡例の位置
# horizontal_legend_fig = go.Figure()
# horizontal_legend_fig.add_trace(go.Scatter(x=x, y=[5, 3, 2], name="line1"))
# horizontal_legend_fig.add_trace(go.Scatter(x=x, y=[4, 2, 3], name="line2"))
# horizontal_legend_fig.update_layout(legend_orientation="h")  # 横並びの凡例
# # 凡例の位置
# # horizontal_legend_fig.update_layout(legend={"x":0.5,"y":-0.15})  
# # 描画領域の左下が(x,y)=(0,0)で凡例の左下の位置を指定する。(1,1)が描画領域の右上
# # 基準点を左下から凡例の中央に置きたい場合は"xanchor":"center"
# horizontal_legend_fig.update_layout(legend={"xanchor":"center","x":0.5,"y":-0.15})  # 凡例の位置
# horizontal_legend_fig.show()


# ------------------------------------------------------------

# # 凡例のグループ化：
#     # 凡例をグループ単位でon/offにできる
#     # Dash アプリで インタラクティブ更新（filtering, animation） を行うとき、
#     # legendgroup を設定しておくと、グループ単位で色や凡例が安定
# grouped_legend_fig = go.Figure()
# grouped_legend_fig.add_trace(
#     go.Scatter(x=x, y=[5, 3, 2], name="A-1", legendgroup="groupA")
# )
# grouped_legend_fig.add_trace(
#     go.Scatter(x=x, y=[3, 5, 4], name="B-1", legendgroup="groupB")
# )
# grouped_legend_fig.add_trace(
#     go.Scatter(x=x, y=[4, 2, 3], name="A-2", legendgroup="groupA")
# )
# grouped_legend_fig.add_trace(
#     go.Scatter(x=x, y=[2, 3, 4], name="B-2", legendgroup="groupB")
# )
# grouped_legend_fig.show()


# ------------------------------------------------------------

# # カラースケール
# np.random.seed(1)
# go.Figure(
#     go.Heatmap(
#         z=np.random.randn(10, 10), # ランダムな値（平均0、標準偏差1の正規分布に従う乱数）を含む10×10の行列
#         # x と y を省略すると、Plotly は自動的に インデックス番号（0, 1, 2, …） を使って軸を作る
#         colorscale="PuBu",  # カラースケール："PuBu" = Purple–Blue（紫→青）明るい紫から濃い青への連続的なグラデーション
#         zmin=-1,  # カラースケールでカバーする値の最小値
#         zmax=3,  # 値の最大値
#     )
# ).show()

# 主な組み込みカラースケール例
    # | 系統                 | 名前                                                | 説明                 |
    # | ------------------ | ------------------------------------------------- | ------------------ |
    # | Sequential（連続）     | `"Viridis"`, `"Plasma"`, `"Inferno"`, `"Cividis"` | 数値データに適した視認性の高い連続色 |
    # | Diverging（双方向）     | `"RdBu"`, `"BrBG"`, `"PiYG"`, `"RdYlGn"`          | 中心（0など）を境に正負の値を表現  |
    # | Qualitative（カテゴリ）  | `"Pastel1"`, `"Dark2"`, `"Set1"`                  | カテゴリ分類用（離散的）       |
    # | Sequential (Blue系) | `"Blues"`, `"PuBu"`, `"BuGn"`                     | 明度変化で値を表現（例：温度、強度） |

# ------------------------------------------------------------

# markerを用いるトレース（Scatter, Bar trace）

# np.random.seed(1)
# x, y, z = np.random.randn(3, 100)
# go.Figure(
#     go.Scatter(
#         x=x,
#         y=y,
#         mode="markers",
#         marker={
#             "color": z,
#             "colorscale": "Greens",
#             "cmin": -1,
#             "cmax": 1,
#             # ❶ カラーバー、0を基準に0.2刻みの目盛を表示
#             "colorbar": {"title": "z", "tick0": 0, "dtick": 0.2},
#         },
#     )
# ).show()


# ------------------------------------------------------------

# # 散布図でカラースケールを用いる

# np.random.seed(1)
# x = np.random.rand(10)
# y = np.random.rand(10)
# go.Figure(
#     go.Scatter(
#         x=x,
#         y=y,
#         mode="markers",
#         marker={
#             "color": z,
#             "colorscale": "Greens",
#             "cmin": -1,
#             "cmax": 1,
#             # ❶ カラーバー、0を基準に0.2刻みの目盛を表示
#             "colorbar": {"title": "z", "tick0": 0, "dtick": 0.2},
#         },
#     )
# ).show()


# ------------------------------------------------------------

# 自作のカラースケールを用いる

go.Figure(
    go.Heatmap(
        z=np.random.randn(10, 10),  # 値（10×10の2次元配列）
        colorscale=[
            [0, "rgb(0,255,255)"], # カラースケールの幅の中の最小の値に対応する色
            [0.5, "rgb(0,80,80)"],
            [1, "rgb(0,20,20)"], # カラースケールの幅の中の最大の値に対応する色
        ],
        # 位置（0〜1）：カラースケール上での相対位置
            # 0 → 最小値（zminの値での色）
            # 1 → 最大値（zmaxの値での色）
        zmax=3,
        zmin=-3
    )
).show()



# ------------------------------------------------------------




# ------------------------------------------------------------




# ------------------------------------------------------------




# ------------------------------------------------------------



