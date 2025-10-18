import pandas as pd
import plotly.express as px
import numpy as np
# ------------------------------------------------------------

# # 分割表示（列と行）
# tips = px.data.tips() # tips データセットは、レストランで支払われたチップ（tip）に関するデータ
# print(tips.head())
# px.scatter(
#     tips,
#     x="total_bill",
#     y="tip",
#     color="size",
#     facet_col="sex",
#     facet_row="time",
# ).show()

# ------------------------------------------------------------

# # アニメーション
#     # このアニメーション導入以前は全ての年のデータがグラフ内に分けずに描画されていた
# gapminder = px.data.gapminder()
# print(gapminder.head())
# gapminder_fig=px.scatter(
#     gapminder, 
#     x="gdpPercap", 
#     y="lifeExp",
#     log_x=True, # x軸を対数
#     hover_name="country",
#     size="pop",
#     size_max=40,
#     color="continent",
#     facet_col="continent", # continent列の値ごとに分割
#     width=800, # （分割時は分割後の）グラフの横幅
#     animation_frame="year", # year列の値を用いたスライダーの実装
# )
# gapminder_fig.update_xaxes(tickfont={"size":8}) # 各サブプロット（subplot）のx軸の目盛り文字（tick labels） のフォントサイズを指定
# gapminder_fig.show() 

# ------------------------------------------------------------

# Plotly の Figure オブジェクト（figure object）には
#     trace（トレース）：実際のデータ点や線の情報
#     layout（レイアウト）：全体の見た目や構成情報
# の2つの主要構成

# # スタイルの設定：図の中の点の設定
#     # figureの作成
# tips = px.data.tips()
# styled_fig = px.scatter(tips,x="total_bill",y="tip",facet_col="sex")

#     # traceの変更
#         # trace（トレース）**とは、Plotly内部での「1種類のデータ系列（data series）」のこと
#         # （例：1本の散布図、1本の折れ線、1つのヒストグラムなど）
# styled_fig.update_traces(   # update_traces() は、**すでに作成済みのtrace（系列）に対してスタイルを変更するメソッド（method）
#     marker={    # marker（マーカー）**は散布図の「点（データポイント）」のスタイルを制御
#         "size":10,
#         "color":"lightblue",
#         "line":{"width":2, "color":"slateblue"},    # 図の中の点に枠線が指定されたスタイルになる
#     }
# )
# styled_fig.show()

# ------------------------------------------------------------

# # スタイルの設定：分割後の図表毎のスタイルの設定
#     # figureの作成
# tips = px.data.tips()
# styled_fig = px.scatter(tips,x="total_bill",y="tip",facet_col="sex")

#     # traceの変更
#         # trace（トレース）**とは、Plotly内部での「1種類のデータ系列（data series）」のこと
#         # （例：1本の散布図、1本の折れ線、1つのヒストグラムなど）
# styled_fig.update_traces(   
#     marker={    # marker（マーカー）**は散布図の「点（データポイント）」のスタイルを制御
#         "size":10,
#         "color":"lightblue",
#         "line":{"width":2, "color":"slateblue"},  
#     },
#     row=1, # 分割後の位置（行ごとに分割していない場合は1を入れる）
#     col=1, 
# )
# styled_fig.update_traces( 
#     marker={   
#         "size":10,
#         "color":"lightpink",
#         "line":{"width":2, "color":"deeppink"},  
#     },
#     row=1,
#     col=2,
# )
# styled_fig.show()

# ------------------------------------------------------------

# # グラフ全体のスタイル：背景、タイトル
# tips = px.data.tips()
# styled_fig = px.scatter(tips,x="total_bill",y="tip",facet_col="sex")

#     # traceの変更
#         # trace（トレース）**とは、Plotly内部での「1種類のデータ系列（data series）」のこと
#         # （例：1本の散布図、1本の折れ線、1つのヒストグラムなど）
# styled_fig.update_traces(   
#     marker={    # marker（マーカー）**は散布図の「点（データポイント）」のスタイルを制御
#         "size":10,
#         "color":"lightblue",
#         "line":{"width":2, "color":"slateblue"},  
#     },
#     row=1,
#     col=1, 
# )
# styled_fig.update_traces( 
#     marker={   
#         "size":10,
#         "color":"lightpink",
#         "line":{"width":2, "color":"deeppink"},  
#     },
#     row=1,
#     col=2,
# )

#     # layoutの変更
# styled_fig.update_layout(
#     width=800, # グラフの大きさを指定
#     height=400,
#     title={
#         "text":"総支払額とチップの金額",
#         "font":{"family":"Courier","size":20,"color":"slategray"},
#     },
#     margin={"l":20,"r":20,"t":40,"b":20}, # 一番外側の要素と外枠の間の余白
#     paper_bgcolor="antiquewhite" # 背景色を設定（全体）

# )
# styled_fig.show()


# ------------------------------------------------------------

# グラフ全体のスタイル：x,y軸（x,y-axis）の設定変更
tips = px.data.tips()
styled_fig = px.scatter(tips,x="total_bill",y="tip",facet_col="sex")

    # traceの変更
        # trace（トレース）**とは、Plotly内部での「1種類のデータ系列（data series）」のこと
        # （例：1本の散布図、1本の折れ線、1つのヒストグラムなど）
styled_fig.update_traces(   
    marker={    # marker（マーカー）**は散布図の「点（データポイント）」のスタイルを制御
        "size":10,
        "color":"lightblue",
        "line":{"width":2, "color":"slateblue"},  
    },
    row=1,
    col=1, 
)
styled_fig.update_traces( 
    marker={   
        "size":10,
        "color":"lightpink",
        "line":{"width":2, "color":"deeppink"},  
    },
    row=1,
    col=2,
)

    # layoutの変更
styled_fig.update_layout(
    width=800, # グラフの大きさを指定
    height=400,
    title={
        "text":"総支払額とチップの金額",
        "font":{"family":"Courier","size":20,"color":"slategray"},
    },
    margin={"l":20,"r":20,"t":40,"b":20}, # 一番外側の要素と外枠の間の余白
    paper_bgcolor="antiquewhite" # 背景色を設定（全体）

)

    # 軸の設定
styled_fig.update_xaxes(
    ticks="outside",  # 軸メモリ（数値とグラフの間の小さな棒）を外側に表示
    tickwidth=2,      # 軸メモリの太さ
    tickcolor="seagreen",  # 軸メモリの色
    ticklen=10,       # 軸メモリの長さ
    # X軸タイトル、フォントサイズ
    title={"text": "総支払金額", "font": {"size": 10}},
)
styled_fig.update_yaxes(
    ticks="outside",
    tickwidth=2,
    tickcolor="dimgray",
    ticklen=10,
    col=1,
    title={"text": "チップの金額", "font": {"size": 10}},
)

styled_fig.show()

