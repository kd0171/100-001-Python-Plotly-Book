import plotly.graph_objects as go

# ------------------------------------------------------------

# # データの構造
# fig = go.Figure()
# print(fig.to_json()[:80]) # type: ignore
#     # {"data":[],"layout":{"template":...

# # データを更新するとJSONデータが更新される
# fig.add_trace(go.Scatter(x=[1,2],y=[3,2]))
# print(fig.to_json()[:80]) # type: ignore
#     # {"data":[{"x":[1,2],"y":[3,2],"type":"scatter"}],"layout":{"template":...

# print(fig.data)
#     # (Scatter({
#     #     'x': [1, 2], 'y': [3, 2]
#     # }),)

# fig.data[0].x=[3.4]
# print(fig.data)
#     # (Scatter({
#     #     'x': [3.4], 'y': [3, 2]
#     # }),)

# ------------------------------------------------------------

# コンストラクタの引数にデータを渡す
layout = go.Layout(title="test")
fig = go.Figure(layout=layout) # Figureクラスのコンストラクタであるlayoutにデータを渡す
fig.show()

print(fig.layout.to_json()[:80]) # type: ignore
    # {"title":{"text":"test"},"template":{"data":{"histogram2dcontour":[{"type":"

# タイトルのデータ構造
    # titleの中には複数の属性が含まれている（text,font,xなど）
    # これらにアクセスするためには本来、go.Layout(title={"text":"..."})のようにデータを渡すが
    # マジックアンダー記法では、簡易的に、title_text="..."title_font=dict()と表記可能
    # この中でタイトルのテキスト部分に当たるtitle_textは、更に省略可能で、title="..."と書いてもよい

# 値の変更
    # | 方法                                                           | 主な使い方        | 適用範囲               | 備考        |
    # | ------------------------------------------------------------ | ------------ | ------------------ | --------- |
    # | **代入（assignment）**<br>`fig.layout.title.text = "..."`        | 個別の属性を1つずつ設定 | 単一のプロパティ（property） | ピンポイント更新  |
    # | **updateメソッド**<br>`fig.layout.update(title={"text": "..."})` | 複数の属性をまとめて更新 | 一部または全体（dict構造）    | 複数項目を一括変更 |

    # 属性を指定した値の代入
fig.layout.title.text="new assigned title" # type: ignore
print(fig.layout.to_json()[:80]) # type: ignore
    # {"title":{"text":"new assigned title"},"template":{"data":{"histogram2dcontour":

    # update関数（layoutオブジェクトの関数）による値の代入
fig.layout.update(title={"text":"updated title", "font": {"size": 20, "color": "red"}})
print(fig.layout.to_json()[:80]) # type: ignore
    # {"title":{"text":"updated title","font":{"size":20,"color":"red"}},"template":{"  

    # update_layout関数（Figureオブジェクトの関数）による値の代入
fig.update_layout(title={"text":"updated title by update_layout", "font": {"size": 12, "color": "blue"}})
print(fig.layout.to_json()[:90]) # type: ignore
    # {"title":{"text":"updated title by update_layout","font":{"size":12,"color":"blue"}},"temp

# ------------------------------------------------------------

# traceの追加（add_traceメソッド）
fig2 = go.Figure()
fig2.add_trace(go.Scatter(x=[1,2,3],y=[1,5,3]))
fig2.show()

# 1つのFigureに複数のtraceを追加可能
fig2.add_trace(go.Bar(x=[1,2,3],y=[-1,-2,-3]))
fig2.show()

# 一度に複数のtraceをあるFigureに追加（add_tracesメソッド）
fig2.add_traces(
    [go.Scatter(x=[1,2,3],y=[3,2,4]),go.Bar(x=[1,2,3],y=[1,2,3])]
)
fig2.show()

# ------------------------------------------------------------




# ------------------------------------------------------------



