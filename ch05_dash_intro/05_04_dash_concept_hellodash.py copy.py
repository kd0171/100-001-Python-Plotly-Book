import dash
import dash_core_components as dcc
import dash_html_components as html
import plotly.express as px

# コンポーネントのスタイル設定. 横幅80％,中央寄せにし,上下に5％の余白を作る.
core_style = {"width": "80%", "margin": "5% auto"}

app = dash.Dash(__name__)

# ➋ レイアウトにdivの子要素として3つのコンポーネントを渡す
app.layout = html.Div(
    [  # ➌ 見出しを作成する
        html.H1("Hello Dash", style={"textAlign": "center"}),
        # ➍ ドロップダウンを作成する
        dcc.Dropdown(
            options=[
                {"label": "white", "value": "white"},
                {"label": "yellow", "value": "yellow"},
            ],
            value="white",
            style=core_style,
        ),
                # | 引数        | 意味                                                         |
                # | --------- | ---------------------------------------------------------- |
                # | `options` | 選択肢（list of dicts）— 各要素に `"label"`（表示名）と `"value"`（内部値）を指定 |
                # | `value`   | 初期選択値（default selected value）                              |
                # | `style`   | CSSスタイル指定                                                  |
                # valueを受け取るにはコールバックの設定が必要

        # ➎ グラフを作成する
        dcc.Graph(
            figure=px.bar(x=[1, 2, 3, 4, 5], y=[1, 2, 3, 4, 5]), style=core_style,
        ),
    ]
)

if __name__ == "__main__":
    app.run_server(debug=True)