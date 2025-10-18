import pandas as pd
import plotly.express as px
import numpy as np

# グラフ描画関数（scatter()：散布図, line()：折れ線グラフ）

# # Pandas（パンダス） の DataFrame（データフレーム）
#     # データフレームは、**表形式データ（tabular data）**を扱うための構造で、列名と行データを持ち
# df = pd.DataFrame([[1,1],[2,5],[3,3]],columns=["x","y"]) # columns=["x", "y"] は列名（column names）を指定
# px.line(
#     df,
#     x="x",
#     y="y"
# ).show()

# ------------------------------------------------------------

# # サンプルデータの読み込みと表示
# tips = px.data.tips() # tips データセットは、レストランで支払われたチップ（tip）に関するデータ
# # print(tips.head())
# px.scatter(tips,x="total_bill",y="tip").show() # x（横軸）とy（縦軸）にはデータ内のatributeを指定

# ------------------------------------------------------------

# # リストなどのデータの可視化
# px.line(x=[1,2,3],y=[2,5,3]).show()

# ------------------------------------------------------------

# numpy.ndarrayをpandas.DataFrameの代わりに渡す
np.random.seed(1)
arr = np.random.rand(100,4)
# 0以上1未満（[0, 1)）の一様分布（uniform distribution） に従う乱数（random numbers） を生成します。
    # 100：行（rows）の数
    # 4：列（columns）の数
print(arr) # 「e-01」の部分は 指数表記（exponential notation）
px.scatter(arr, x=0,y=1,color=2,size=3).show()

# メモ： numpy.ndarrayとpandas.DataFrameの違い
# numpy.ndarray：
    # 列名（column name） はありません。
    # 列番号（column index） だけが使えます。(x=0,y=1,color=2,size=3の部分)
# pandas.DataFrame：
    # 列名（column names）付きの表形式データ（tabular data）
