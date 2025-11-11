import dash
import dash_core_components as dcc
import plotly
import plotly.graph_objects as go

gapminder = plotly.data.gapminder()
gapminder2007 = gapminder[gapminder["year"] == 2007]

# ➊ figureの作成
fig = go.Figure()

# # plotlyによるFigureの追加
# fig.add_trace(
#     go.Scatter(
#         x=gapminder2007.loc[gapminder2007["continent"] == "Asia", "gdpPercap"],
#         y=gapminder2007.loc[gapminder2007["continent"] == "Asia", "pop"],
#         name="Asia",
#         mode="markers",
#         marker={
#             "size": gapminder2007.loc[gapminder2007["continent"] == "Asia", "lifeExp"]
#             / 2
#         },
#         text=gapminder2007.loc[gapminder2007["continent"] == "Asia", "country"],
#     )
# )

# for文を用いたグルーピング（大陸ごとに色や凡例が分かれる）
for c in gapminder2007.continent.unique(): # 各大陸名を重複なしで取り出します
    fig.add_trace(
        go.Scatter(
            x=gapminder2007.loc[gapminder2007["continent"] == c, "gdpPercap"],
            y=gapminder2007.loc[gapminder2007["continent"] == c, "pop"],
            name=c,
            mode="markers",
            marker={
                "size": gapminder2007.loc[gapminder2007["continent"] == c, "lifeExp"]
                / 2
            },
            text=gapminder2007.loc[gapminder2007["continent"] == c, "country"],
        )
    )

# for文によるグループ化のメリット
    # | 機能         | for文なし    | for文あり           |
    # | ---------- | --------- | ---------------- |
    # | 色分け        | すべて同じ色    | 大陸ごとに自動で別の色      |
    # | 凡例（legend） | 表示なしまたは1つ | 各大陸ごとに表示         |
    # | ホバー情報      | 国名のみ      | 国名＋大陸ラベル         |
    # | データ選択      | 不可        | 大陸単位でON/OFF切り替え可 |

fig.update_layout(
    xaxis={"type": "log", "title": "gdpPercap"},
    yaxis={"type": "log", "title": "pop"},
    title="Gapminder",
)


app = dash.Dash(__name__)

app.layout = dcc.Graph(
    # ➋ figureにfigを渡す
    figure=fig
)

if __name__ == "__main__":
    app.run_server(debug=True)