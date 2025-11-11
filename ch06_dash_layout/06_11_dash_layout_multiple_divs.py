import dash
import dash_html_components as html
import dash_core_components as dcc
import plotly
import plotly.graph_objects as go

div_style3 = {
    "width": "500px",  # 横幅: 500px
    "height": "250px",  # 高さ: 250px
    "backgroundColor": "lime",  # 背景色: ライム
    "margin": "5%",  # 要素の外側の余白領域 上下50px、autoで中央寄せ
    "display": "inline-block",
}

div_style4 = {
    "width": "29%",  # 横幅: 500px
    "height": "350px",  # 高さ: 250px
    "backgroundColor": "skyblue",  # 背景色: ライム
    "margin": "2%",  # 要素の外側の余白領域 上下50px、autoで中央寄せ
    "display": "inline-block",
}
# display: inline-block の意味：要素を横に並べるが、ブロック要素の性質（幅・高さ指定）も保持する
    # | モード            | 並び方         | 幅・高さ指定 | 代表例                  |
    # | -------------- | ----------- | ------ | -------------------- |
    # | `block`        | 縦に並ぶ（改行される） | 可能     | `<div>`, `<p>`       |
    # | `inline`       | 横に並ぶ（改行しない） | 不可     | `<span>`, `<a>`      |
    # | `inline-block` | 横に並ぶ        | 可能 ✅   | カスタム要素や `div` に使うと便利 |


app = dash.Dash(__name__)


app.layout = html.Div(
    [
        html.Div(
            [
                html.Div(style=div_style3),
                html.Div(style=div_style3),
            ],
            id="first_leader",
        ),
        html.Div(
            [
                html.Div(style=div_style4),
                html.Div(style=div_style3),
                html.Div(style=div_style4),
            ],
            id="second_leader",
        )
    ],
    id="leader"
)


if __name__ == "__main__":
    app.run_server(debug=True)