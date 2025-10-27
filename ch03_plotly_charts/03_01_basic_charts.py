import plotly
import plotly.graph_objects as go
import numpy as np
from plotly.subplots import make_subplots
import pandas as pd
# ------------------------------------------------------------

# # 折れ線グラフ
# go.Figure(
#     go.Scatter(
#         x=[1,2,3],
#         y=[3,1,5],
#     )
# ).show()


# ------------------------------------------------------------

# Range Selectorを用いた折れ線グラフ
# stocks = plotly.data.stocks()
# # print(stocks.head())

# # go.Figure(
# #     go.Scatter(
# #         x=stocks["date"],
# #         y=stocks["GOOG"]
# #     )
# # ).show()

# ts_layout = go.Layout(
#     # X軸のRange SliderとRange Selectorを表示
#     xaxis = {
#         "rangeslider": {"visible":True}, # X軸の下にスライダーを描画する、これだけでスライダーは実装される
#         "rangeselector": { # X軸の上にボタンを表示して、範囲を切り替える設定
#             "buttons": [
#                 {"label":"1m", "step":"month", "count":1},
#                 {"label":"7d", "step":"day", "count":7},
#                 {"step":"all"}
#             ]
#         },
#     }
# )

#     # | 属性                                | 意味                                 |
#     # | :----------------------------      | :--------------------------          |
#     # | `label`                            | ボタン上の文字（例："1m"）             |
#     # | `step`                             | 単位（"day"・"month"・"year" など）    |
#     # | `count`                            | 単位の数（例：1 → 1か月, 7 → 7日）     |
#     # | `stepmode`（省略時は `"backward"`） | 現在位置から過去方向に遡るかどうか      |

# # step（単位）と count（その数）がどう解釈されるかは、元のデータ（特に x 軸の型 / 型推論） に強く関係
# # step "day" / "month" / "year" / "hour" … などの時間単位 Plotly.js (JavaScript) 側で定義
#     # "week" は？ Python版 Plotly では未サポート（→エラーになる）
#     # 自分で定義："step": "day", "count": 7

# go.Figure(
#     go.Scatter(
#         x=stocks["date"],
#         y=stocks["GOOG"]
#     ),
#     layout = ts_layout,
# ).show()

# ------------------------------------------------------------

# # 欠損値を補完
# line_x_not_null = np.arange(5)  
#     # np.arange([start,] stop[, step]): NumPy の **等差数列（arithmetic sequence）**を生成する関数
# line_y_with_null = np.array([1, 2, np.nan, 4, 5])  # 欠損値を含んだデータ
#     # np.array() は Python のリスト [1, 2, np.nan, 4, 5] をNumPy配列（ndarray） に変換する関数
# with_null_fig = go.Figure()

# # 後から変更しやすいのでadd_traceメソッドでそれぞれのtraceを追加している
# with_null_fig.add_trace(
#     go.Scatter(x=line_x_not_null, y=line_y_with_null, name="default")
# )
# with_null_fig.add_trace(
#     go.Scatter(
#         x=line_x_not_null,
#         y=line_y_with_null + 1,
#         name="connectgaps",  
#         connectgaps=True,   # 欠損値を無視して線を接続
#     )
# )
# with_null_fig.show()


# interp_x, interp_y = np.array([1, 2, 3]), np.array([1, 3, 2])
# line_shapes = ("linear", "spline", "hv", "vh", "vhv", "hvh")

# # 6 行 1 列の Figure を作成（各サブプロットのタイトルは line_shapes を流用）
# interp_fig = make_subplots(rows=6, cols=1, subplot_titles=line_shapes)

# for i, shape_name in enumerate(line_shapes, 1):  # 添字は 1 から開始（row 番号に合わせる）
#     interp_fig.add_trace(
#         go.Scatter(
#             x=interp_x,
#             y=interp_y,
#             name=shape_name,
#             line={"shape": shape_name},  # 補間方法（interpolation/segmentation）を指定
#             hovertext=shape_name,
#             # connectgaps=True  # 欠損値を無視して線をつなぎたい場合はここを有効化
#         ),
#         row=i,
#         col=1,
#     )

# interp_fig.show()

# 折れ線の**形状（line shape）**を指定。主な意味は次のとおり：
    # "linear"：隣接点を直線で結ぶ（piecewise linear）。
    # "spline"：スプライン曲線（spline interpolation）。滑らかに補間。
    # "hv"：**水平→垂直（horizontal→vertical）**の順で折れる“階段（step）”線。
    # "vh"：**垂直→水平（vertical→horizontal）**で折れる。
    # "vhv"：垂直→水平→垂直。
    # "hvh"：水平→垂直→水平。
# いわゆるステップチャート（step chart）/**階段線（step line）**のバリエーションです。

# ------------------------------------------------------------

# 散布図
    # modeを"markers"に指定すると散布図になる

# np.random.seed(1)
# scatter_x, scatter_y = np.random.randn(2,100) 
# # np.random.randn(2, 100) が shape = (2, 100) の2次元配列を返す
#     # 「最初の次元（行）」を2つに**分解（アンパック）**している
# go.Figure(
#     go.Scatter(
#         x=scatter_x,
#         y=scatter_y,
#         mode="markers",
#         name="standard normal distribution"
#     )
# ).show()

# # 散布図で色やサイズを指定し、高次元を描画
# np.random.seed(1)
# scatter_color = np.random.rand(100)
# scatter_size = np.random.rand(100)*30
# go.Figure(
#     go.Scatter(
#         x=scatter_x,
#         y=scatter_y,
#         mode="markers",
#         name="4d",
#         marker={
#             "color":scatter_color,
#             "size":scatter_size,
#             "sizemode": "diameter", # 大きさを直径で表現
#             "opacity":0.7, # 要素の不透明度
#             "showscale": True, # カラースケールで表示
#         }
#     )
# ).show()

# color：意味：マーカー（点）の色を指定。
    # 指定できる値：
        # 単一値（例："red", "rgb(0,128,255)"）→ 全部同じ色。
        # 配列（例：scatter_color = np.random.randn(100)）→ 値に応じて色分け。

# size:意味：各マーカーのサイズを指定。
    # 指定できる値：
        # 単一値：全ての点が同じ大きさ。
        # 配列：各点ごとにサイズを変えられる。

# sizemode:意味：サイズ指定の解釈方法。
    # 指定できる値：
        # "diameter"（直径）👉 デフォルト。数値 = 点の直径（pixel単位）。
        # "area" 👉 数値 = 点の面積（pixel²）。

# showscale:意味：色を数値と対応させる**カラーバー（color scale legend）**を右側に表示するかどうか。
    # 有効になる条件：color が配列（数値系列）である場合のみ。

# ------------------------------------------------------------

# # 大規模データの散布図の高速描画（Scattergl）
# np.random.seed(1)
# large_x, large_y = np.random.randn(2,100000)
# go.Figure(
#     go.Scattergl(
#         x=large_x,
#         y=large_y,
#         mode="markers"
#     )
# ).show()

# # 複数のtraceを渡す可能性がある場合は、go.Figure([])と中に[]を入れる
# np.random.seed(1)
# large_x, large_y = np.random.randn(2,100000)
# go.Figure([
#     go.Scattergl(
#         x=large_x,
#         y=large_y,
#         mode="markers"
#     )
# ]).show()

# ------------------------------------------------------------

# 棒グラフ（bar chart）
# bar_fig = make_subplots(
#     rows=2,
#     cols=2,
#     subplot_titles=["ラベル","座標","横"] # 順番にグラフのタイトル
# )
# bar_fig.add_trace( # X値が文字列型
#     go.Bar(x=["a","b","c"],y=[3,5,2]),
#     row=1,
#     col=1,
# )
# bar_fig.add_trace( # 複数のグラフを表示したい場合には同じ行と列を指定
#     go.Bar(x=["a","b","c"],y=[1,2,3]),
#     row=1,
#     col=1,
# )
# bar_fig.add_trace( # X値が数値型
#     go.Bar(x=[0,1,4],y=[1,4,3]),
#     row=1,
#     col=2,
# )
# bar_fig.add_trace( # グラフが横向き
#     go.Bar(x=[3,2,4],y=[1,2,3],orientation="h"), # orientationで向きを調整可能
#     row=2,
#     col=1,
# )
# bar_fig.show()

# ------------------------------------------------------------

# # グループ化した棒グラフ
# bar_trace1 = go.Bar(x=["a","b","c"], y=[3,5,2], name="group1")
# bar_trace2 = go.Bar(x=["a","b","c"], y=[4,3,1], name="group2")
# grouped_fig = go.Figure([bar_trace1,bar_trace2])
# grouped_fig.show()

# # 積み上げ棒グラフ
# stacked_fig = go.Figure(
#     [bar_trace1,bar_trace2],
#     layout=go.Layout(barmode="stack")
# )
# stacked_fig.show()

# # 負の領域を含むグラフ
# bar_trace3 = go.Bar(x=["a","b","c"], y=[-2,-3,1], name="group3")
# relative_fig = go.Figure(
#     [bar_trace1,bar_trace2,bar_trace3],
#     layout=go.Layout(barmode="relative")
# )
# relative_fig.show()

# ------------------------------------------------------------

# # 面グラフ
#     # fillに"tozeroy"を渡すと塗りつぶす
# np.random.seed(7)
# area_x = np.arange(10)
# area_y1, area_y2 = np.random.rand(2,10)
# # np.random.randn() は 標準正規分布：範囲は固定されていません（理論的には −∞ ～ +∞）
# # np.random.rand() は 一様分布 (uniform distribution)：すべての値が 0以上1未満 の範囲に均等に出現
# area_trace= go.Scatter(
#     x=area_x,
#     y=area_y1,
#     name="area 1",
#     fill="tozeroy", # 0-Yまでの間を塗りつぶし(to zero y)
#     mode="none", # 線とマーカーを描画しない
#     fillcolor="mediumslateblue"
# )
# area_fig = go.Figure([area_trace])
# area_fig.show()

# # 積み上げ面グラフ（足し算）
# next_area_trace= go.Scatter(
#     x=area_x,
#     y=area_y1+area_y2,
#     name="area 2",
#     fill="tonexty", # 既存のグラフから-Yまでの間を塗りつぶし
#     mode="none", # 線とマーカーを描画しない
#     fillcolor="lightpink"
# )
# stacked_area_fig = go.Figure([area_trace,next_area_trace])
# stacked_area_fig.show()
# # 積み上げ面グラフ（stacked area chart）では、go.Figure([...]) に渡すトレースの順番が非常に重要
#     # 原則：下から積みたい順に並べる（下層→上層の順で追加）。

# # 積み上げ面グラフ（グループ化）
# area_trace_a1= go.Scatter(
#     x=area_x,
#     y=area_y1,
#     name="area 1",
#     stackgroup="groupA", # グループ名を命名
#     mode="none", 
#     fillcolor="mediumslateblue"
# )
# area_trace_a2= go.Scatter(
#     x=area_x,
#     y=area_y2,
#     name="area 2",
#     stackgroup="groupA", # グループ名を命名
#     mode="none", 
#     fillcolor="lightpink"
# )
# stackgroup_area_fig = go.Figure([area_trace_a1,area_trace_a2])
# stackgroup_area_fig.show()

# # 積み上げ面グラフ（100分率）
# normed_area_fig=go.Figure()
# normed_area_fig.add_trace(
#     go.Scatter(
#         x=area_x,
#         y=area_y1,
#         name="area 1",
#         stackgroup="groupA", # グループ名を命名
#         mode="none", 
#         groupnorm="fraction", # 合計を1として正規化
#         fillcolor="mediumslateblue"
#     )
# )
# normed_area_fig.add_trace(
#     go.Scatter(
#         x=area_x,
#         y=area_y2,
#         name="area 2",
#         stackgroup="groupA", # グループ名を命名
#         mode="none", 
#         groupnorm="fraction", # 合計を1として正規化
#         fillcolor="lightpink"
#     )
# )
# normed_area_fig.show()

# ------------------------------------------------------------

# # 円グラフ
# companies = ["A社", "B社", "C社", "D社"]
# sales_2019 = [1000, 700, 300, 100]
# sales_2020 = [1500, 1100, 450, 380]

# # go.Figure(
# #     go.Pie(labels=companies, values=sales_2019), # x,yの代わりにvaluesを用いる
# #     layout=go.Layout(title="売上"),
# # ).show()

# # 円グラフを横に並べる
# sales_pie_fig = make_subplots(
#     rows=1,
#     cols=2,
#     specs=[[{"type":"domain"},{"type":"domain"}]],
#     subplot_titles=["2019年の売上","2020年の売上"],
# )
# # Plotlyの「トレース（trace）」には、2つの座標系タイプ
#     # | タイプ              | 説明                              | 代表的なグラフ                                              |
#     # | :------------       | :-----------------               | :--------------------------------------------------- |
#     # | `"xy"`（デフォルト） | 通常の2軸グラフ（x軸・y軸を持つ）   | 散布図（scatter）、折れ線（line）、棒グラフ（bar）など                   |
#     # | `"domain"`          | 軸を持たない“領域ベース”のプロット  | 円グラフ（pie）、サンバースト（sunburst）、ツリーマップ（treemap）、ドーナツグラフなど |

# sales_pie_fig.add_trace(
#     go.Pie(
#         labels=companies,
#         values=sales_2019,
#         scalegroup="sales",
#     ),
#     row=1,
#     col=1,
# )
# sales_pie_fig.add_trace(
#     go.Pie(
#         labels=companies,
#         values=sales_2020,
#         scalegroup="sales",
#     ),
#     row=1,
#     col=2,
# )
# # scalegroup="sales" は、「同じグループ名を持つ複数の円グラフのスケールをそろえる」ための指定。
# # "sales" はただのグループ名文字列で、変数ではなく明示的に定義する必要もない
# # これが変数である必要はなく、文字列が一致していれば同じグループと見なされます。
# sales_pie_fig.show()

# ------------------------------------------------------------

# # サンバーストグラフ
# asset_labels = ["資産", "債権", "A社", "B社", "株式", "C社", "D社", "預金"]
# asset_parents = ["", "資産", "債権", "債権", "資産", "株式", "株式", "資産"] # 各ラベル（ノード）がどの親（parent）に属しているかを示す
# asset_values = [1000, 400, 300, 100, 200, 160, 40, 400] 
# sunburst_fig = make_subplots(
#     1, 2, specs=[[{"type": "domain"}, {"type": "domain"}]]
# )
# # make_subplots() の最初の2つの位置引数は rows と cols なので、
# # 順番どおりに値を渡している場合は名前を省略してもOK です。
# sunburst_fig.add_trace(
#     go.Sunburst(
#         labels=asset_labels,  # セクタごとのラベル
#         parents=asset_parents,  # 親セクタのラベル
#         values=asset_values,  # セクタごとの値
#         branchvalues="total",  # ❶ 親が子の階層すべての合計値
#     ),
#     row=1,
#     col=1,
# )
# sunburst_fig.add_trace(
#     go.Sunburst(
#         labels=asset_labels,
#         parents=asset_parents,
#         values=asset_values,
#         branchvalues="remainder",  # ❷ 子が親とは別の値
#     ),
#     row=1,
#     col=2,
# )
# sunburst_fig.show()


# ------------------------------------------------------------

# テーブルの作成

table_values = [[1,2,3],[3,5,2]]
table_labels = ["A","B"]
table_fig = make_subplots(
    rows=2,
    cols=2,
    specs=[[{"type":"domain"},{"type":"domain"}],[{"colspan":2},None]],
    # specs の外側のリスト [...] は 全体、内側の各リスト [...] は 1行分（row） を表します。
)
# {"type": "domain"} → ドメイン型（軸を持たないタイプ）。
# "colspan": 2 → 1つのセルが横に2列分の幅を取る（列結合）。
    # +-----------+-----------+
    # |  domain1  |  domain2  |
    # +-----------------------+
    # |       colspan=2       |
    # +-----------------------+
# (1,1): {"type":"domain"}   → 左上
# (1,2): {"type":"domain"}   → 右上
# (2,1): {"colspan":2}       → 下段全体（横2つ分）
# (2,2): None                → （結合済みのため空）

table_fig.add_trace(
    go.Table(
        header={
            "values":table_labels,
            "height":18, 
        },
        cells={"values":table_values}
    ),
    row=1,
    col=1,
)
    # go.Table(
    #     header={...},   # ヘッダー（表の上部）
    #     cells={...}     # セル（表の中のデータ）
    # )

# table_fig.add_trace(
#     go.Table(
#         cells={ 
#             "values":pd.DataFrame(table_values), # Plotly の Table は 行単位ではなく列単位 でデータを渡す
#             "line":{"width":2,"color":"black"}, # 罫線のスタイル
#             "fill":{"color":"white"}, # 塗りつぶし
#             "align":"right" # 配置 "left", "center", "right"
#         },
#         header={
#             "values":table_labels,
#             "height":18, # セルの高さ
#             "line":{"width":2,"color":"black"}, # 罫線のスタイル
#             "fill":{"color":"white"}, # 塗りつぶし
#             "font":{"size":10},
#         },
#     ),
#     row=1,
#     col=2,
# )
# Plotly は DataFrame を自動で変換できるが、常に安全ではありません。
    # 列と行が反転する可能性
# →自分で明示的に列ごとのリストを渡すのが最も安全

df = pd.DataFrame(table_values)
SafePandas_trace = go.Table(
    cells={"values":[df[col] for col in df.columns], 
            "line":{"width":2,"color":"black"}, 
            "fill":{"color":"red"},
            "align":"right"
    },
    header={"values":list(df.columns),
            "height":18, 
            "line":{"width":2,"color":"black"}, 
            "fill":{"color":"orange"}, 
            "font":{"size":10},
    },
)
table_fig.add_trace(
    SafePandas_trace, # ただしはこれは
    # table_fig.add_trace(...) は トレース（go.Table, go.Scatter など） を受け取ります。
    # でも SafePandas は go.Figure（図全体）。Figure は add_trace に渡せません。
    row=1,
    col=2,
)

# そのままDataFrameを渡した場合と安全に渡した場合で高さが異なるのは、そのまま渡した場合には自動補正が加わるから
# DataFrameをそのまま go.Table に渡すのは「便利そうに見えて不安定」
# → 見た目（書式）を正確に制御したいなら、DataFrameを明示的にリスト化して渡すのが鉄則 です。
# Plotly が pandas.DataFrame を受け取れるのは「おまけ的な互換機能」

table_fig.add_trace(
    go.Scatter(x=table_values[0],y=table_values[1]),
    row=2,
    col=1,
)
table_fig.show()

# ------------------------------------------------------------




# ------------------------------------------------------------




# ------------------------------------------------------------




# ------------------------------------------------------------



