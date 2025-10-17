import plotly.express as px

# px.data は、Plotly Express が提供するデータモジュール
# データ名はdfまたはgapminder
df = px.data.gapminder()

# データ.head()は、最初の５行を取得できるDataFrameメソッド
# print(df.head())

# ------------------------------------------------------------

# scatter plot（散布図）を描画
# 最低限px.scatter(data_frame, x, y)、これらのarguments（引数）は必須
# px.scatter(
#     df, x="gdpPercap", y="lifeExp"   
# ).show()

# ------------------------------------------------------------

# # グラフの描画
# px.scatter(
#     df, 
#     x="gdpPercap", 
#     y="lifeExp",
#     log_x=True, 
#     hover_name="country", # マウスオーバー時に表示されるメインのラベル（hover label）
#     size="pop", # pop列の値（人口）に基づいて、散布図上の点の大きさを変更
#     size_max=40, # 点の最大値
#     color="continent", # continent列の値ごとに色が区別 
# ).show() # hover_name 以外にも、グラフに使われている属性（arguments） は自動的にマウスオーバー（hover）時に表示

# ------------------------------------------------------------

# # グラフの分割
# px.scatter(
#     df, 
#     x="gdpPercap", 
#     y="lifeExp",
#     log_x=True, 
#     hover_name="country",
#     size="pop",
#     size_max=40,
#     color="continent",
#     facet_col="continent", # continent列の値ごとに分割
#     width=800, # （分割時は分割後の）グラフの横幅
# ).show() 

# ------------------------------------------------------------

# # Figureオブジェクトの代入
#     # Figure オブジェクトには、いくつもの「更新メソッド（update methods）」が定義
# facet_fig=px.scatter(
#     df, 
#     x="gdpPercap", 
#     y="lifeExp",
#     log_x=True, 
#     hover_name="country",
#     size="pop",
#     size_max=40,
#     color="continent",
#     facet_col="continent", # continent列の値ごとに分割
#     width=800, # （分割時は分割後の）グラフの横幅
# )
# facet_fig.update_xaxes(tickfont={"size":8}) # 各サブプロット（subplot）のx軸の目盛り文字（tick labels） のフォントサイズを指定
# facet_fig.show() 

# ------------------------------------------------------------

# アニメーションの追加
animation_fig=px.scatter(
    df, 
    x="gdpPercap", 
    y="lifeExp",
    log_x=True, 
    hover_name="country",
    size="pop",
    size_max=40,
    color="continent",
    facet_col="continent", # continent列の値ごとに分割
    width=800, # （分割時は分割後の）グラフの横幅
    animation_frame="year", # year列の値を用いたスライダーの実装
)
animation_fig.update_xaxes(tickfont={"size":8}) # 各サブプロット（subplot）のx軸の目盛り文字（tick labels） のフォントサイズを指定
animation_fig.show() 

# ------------------------------------------------------------

















