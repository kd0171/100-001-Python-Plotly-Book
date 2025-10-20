import plotly.express as px
import numpy as np
import pandas as pd

gapminder = px.data.gapminder()
tips = px.data.tips()

# ------------------------------------------------------------

# # 散布図
# # print(gapminder.head())
# # DataFrame.loc[行の条件, 列の指定]は、Pandas の DataFrame（データフレーム） からラベル（label）や条件式（condition）でデータを取り出すためのアクセサ（accessor）
# gapminder_2007 = gapminder.loc[gapminder["year"] == 2007] # 条件に該当する行のみを抽出
# px.scatter(
#     gapminder_2007,
#     x="gdpPercap",
#     y="lifeExp",
#     size="pop",
#     color="continent",
#     hover_name="country",
#     log_x=True,
#     size_max=60,
# ).show()

# # 一部の列のみを抽出することも可能
# gapminder_min = gapminder.loc[gapminder["year"] == 2007, ["country", "lifeExp", "gdpPercap"]] # 条件に該当する行のみを抽出
# print(gapminder_min.head())

# ------------------------------------------------------------

# # scatter matrix（散布図行列）
# print(tips.head())
# scatter_matrix_fig = px.scatter_matrix(
#     tips,
#     dimensions=["total_bill","tip","size"],
#     color="time", # シンボルの色
#     symbol="smoker", # シンボル（点の形：〇、□、◇など）
# ).show()

# ------------------------------------------------------------

# # Line Chart(折れ線グラフ)
# print(gapminder.head())
# gapminder_Oceania = gapminder.loc[gapminder["continent"] == "Oceania"] # .loc[]の後の括弧は四角い括弧
# px.line(
#     gapminder_Oceania,
#     x="year",
#     y="lifeExp",
#     color="country",
# ).show()

# ------------------------------------------------------------

# # Bar Chart(棒グラフ)
# gapminder_Canada = gapminder.loc[gapminder["country"]=="Canada"]
# px.bar(
#     gapminder_Canada,
#     x="year",
#     y="pop",
#     color="lifeExp",
#     hover_data=["lifeExp","gdpPercap"],
# ).show()

# メモ：色付けの規則
    # Plotly Express（px）は、color= に指定された列（column）の**データ型（data type）**を見て、色付け方法（color mapping method）**を自動的に決めます。
    # データ型（dtype）	色の扱い	表示の仕方
    # 数値（numeric, int/float）	連続カラースケール（continuous color scale）	グラデーション（例：青→黄→赤）
    # 文字列／カテゴリ（string, category）	離散カラーマップ（discrete color map）	各カテゴリごとに固有の色

# ホバーの情報
    # パラメータ	説明
    # hover_name	ホバー時のタイトル行（主ラベル）に表示する列     hover_name="country",      # ← ホバータイトル
    # hover_data	追加で表示する列（複数指定OK）                  hover_data=["pop", "continent"],  # ← 追加データ

# ------------------------------------------------------------

# # 様々なBar Chart
#     # 積み上げ棒グラフ
# px.bar(
#     tips,
#     x="sex",
#     y="total_bill",
#     color="time",
# ).show()
#     # 横に並べる棒グラフ
# px.bar(
#     tips,
#     x="sex",
#     y="total_bill",
#     color="smoker",
#     barmode="group",
# ).show()

# barmode にはいくつかのオプションがあります👇
    # barmode	表示スタイル	説明
    # "relative"	積み上げ（stacked）	デフォルト。色で分けた棒を積み上げる
    # "group"	グループ表示	色で分けた棒を横に並べる
    # "overlay"	重ね描き（透明）	棒を重ねて比較（透明度を使うと便利）
    # "stack"	"relative" とほぼ同義	積み上げ表示（非推奨表記）

# ------------------------------------------------------------

# # Area Chart（面グラフ）
# px.area(
#     gapminder,
#     x="year",
#     y="pop",
#     color="continent",
#     line_group="country", # データ内でグループ化した行毎に実行するの、国毎にまず線を引く
# ).show()


# ------------------------------------------------------------

# # エラーバー付きの散布図
# np.random.seed(1)
# df = pd.DataFrame(np.random.randn(100,2),columns=["x","y"])
# px.scatter(
#     df,
#     x="x",
#     y="y",
#     error_x=np.random.rand(100) * 0.1, # 各点のX方向の誤差（±の長さ）を指定、現在の値はエラーバーを生成するための仮の値で特に意味はない（通常は標準偏差など）
#     error_y=np.random.rand(100) * 0.1,
# ).show()


# ------------------------------------------------------------

# # 箱ひげ図
# px.box(tips, x="time", y="total_bill").show()
    # デフォルト：
        # 中央の線（中央値 median）
        # 上下の箱（第1四分位 Q1・第3四分位 Q3）
        # 「ひげ」（データの範囲）
            # ひげ（下）	Q1 − 1.5 × IQR	lower whisker
            # ひげ（上）	Q3 + 1.5 × IQR	upper whisker
        # 外れ値（outlier）を点で表示（デフォルトは "outliers"）

# # ノッチ付き箱ひげ図（ノッチ（notch）＝中央値（median）の95%信頼区間（confidence interval）を切り込みで表す）：中央値に統計的な信頼区間を追加している
# px.box(
#     tips,
#     x="time",
#     y="total_bill",
#     color="smoker",        # smoker 列で色分け
#     notched=True,          # ノッチを入れる
#     points="all",          # すべての値を点で描画（箱ひげ図の横に全ての点がプロットされて表示される）
#     title="Box plot of total bill",
#     hover_data=["day"],    # ホバーソールに day 列の値を表示
# ).show()

# ------------------------------------------------------------

# バイオリン図

# px.violin(
#     tips,
#     x="smoker",
#     y="tip",
#     color="sex",
#     box=True, # 箱ひげ図を重ねて表示
#     points="all", # 全てのデータを描画
#     hover_data=tips.columns, # データ点をホバーした際には全ての列の情報を表示
# ).show()

# points は Violin / Box / Strip / Histogram などに共通で使える引数で、
# データ点をどの程度見せるかを決めます。
    # 値	表示される点	説明
    # "all"	すべてのデータ点	分布の形をより明確に見たいときに使う
    # "outliers"	外れ値のみ	箱ひげ図と同じルールで外れ値を点で表示
    # "suspectedoutliers"	“疑わしい外れ値”だけ	箱ひげ図の1.5〜3×IQR範囲にある点
    # False or None	点を表示しない	分布だけ見たいとき（軽量表示）

# hover_data は、マウスオーバーした際にツールチップ（hover tooltip）に表示される列や値を制御
    # 列名リスト（あなたの例）
        # hover_data=["day", "time"]
        #     → 指定した列の値がホバー時に表示されます。
    # DataFrame の全列を表示（あなたの例と同じ）
        # hover_data=tips.columns

# ------------------------------------------------------------

# # ヒストグラム
# px.histogram(tips, x="total_bill").show()


# # ヒストグラムの分割（色を指定することで分割して表示される）
# px.histogram(
#     tips, 
#     x="total_bill",
#     color="sex",
#     hover_data=tips.columns,
# ).show()

# # ヒストグラムの上にラグプロットを表示
#     # データをバーコードの線として描画して、データの密度を表示
# px.histogram(
#     tips, 
#     x="total_bill",
#     color="sex",
#     marginal="rug",
#     hover_data=tips.columns,
# ).show()

# ------------------------------------------------------------



# ------------------------------------------------------------

# 平行プロット

# ------------------------------------------------------------

# 三角図

# ------------------------------------------------------------

# ボーラチャート

# ------------------------------------------------------------

gapminder_2007=gapminder.loc[gapminder["year"]==2007]
# print(gapminder_2007.head())

# # choropleth map（階級区分図）
# px.choropleth(
#     gapminder_2007,
#     locations="iso_alpha", # geominder内の国コード列を使用
#     color="lifeExp",
#     hover_name="country",
# ).show()

# 国の読み込みの仕組み：
    # gapminder_2007 の中にある "iso_alpha" 列が「国を識別するキー」として渡されている
# px.choropleth() が必要とする主な引数
    # | 引数名          | 意味             | Gapminder内の対応列                          |
    # | ------------ | -------------- | --------------------------------------- |
    # | `locations`  | 各地点（国や州）を識別する値 | `"iso_alpha"`（3文字の国コード）                 |
    # | `color`      | 塗り分けに使う数値列     | `"lifeExp"`（平均寿命）                       |
    # | `hover_name` | ホバー時に表示する名前    | `"country"`（国名）                         |
    # | `hover_data` | （任意）追加で表示する列   | 例: `"gdpPercap"`, `"pop"`               |
    # | `projection` | 地図投影法          | `"natural earth"`, `"mercator"` など（省略可） |
    # | `scope`      | 地図範囲           | `"world"`, `"asia"`, `"europe"` など（省略可） |

# # 地域を区切った階級区分図
# px.choropleth(
#     gapminder,
#     locations="iso_alpha",
#     color="lifeExp",
#     hover_name="country",
#     scope="asia",
#     animation_frame="year",
# ).show()

# ------------------------------------------------------------

# # 地図上の散布図
# px.scatter_geo(
#     gapminder, # 教科書では2007を用いているのでアニメーションが動作しない
#     locations="iso_alpha",
#     size="gdpPercap",
#     color="lifeExp",
#     hover_name="country",
#     animation_frame="year",
# ).show()

# ------------------------------------------------------------

# # 3D scatter plot
# scatter_3d_fig = px.scatter_3d(
#     gapminder,
#     x="year",
#     y="continent",
#     z="pop",
#     size="gdpPercap",
#     color="lifeExp",
#     hover_data=["country"],
# )
# scatter_3d_fig.layout.update(scene={"zaxis":{"type":"log"}})
# scatter_3d_fig.show()

# Plotlyの「2Dグラフ」と「3Dグラフ」の違い
    # | 種類                                            | 軸の管理構造                        | 軸設定の場所                                             |
    # | --------------------------------------------- | ----------------------------- | -------------------------------------------------- |
    # | **2D グラフ** (`px.scatter`, `px.line`, …)       | xaxis, yaxis                  | `fig.update_xaxes()`, `fig.update_yaxes()`         |
    # | **3D グラフ** (`px.scatter_3d`, `px.line_3d`, …) | scene → (xaxis, yaxis, zaxis) | `fig.update_layout(scene=...)` または `.layout.scene` |

    # 2D → 各軸が独立して存在
    # 3D → 軸はすべて「scene（シーン）」という立体空間の中にまとめて存在

# ------------------------------------------------------------



# ------------------------------------------------------------


