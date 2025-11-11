import dash
import dash_html_components as html

app = dash.Dash(__name__)

app.layout = html.Div(
    [
        html.P(
            "こんにちは。昨日は雪が降りました。",
            style={
                "fontSize": 50,  # フォントサイズ
                "color": "white",  # 文字色
                "backgroundColor": "#000000",  # 背景色
                "width": "40%",
                "display": "inline-block", # 横並びにするため
                # 通常、<p> タグは ブロック要素（block element） なので縦に並びます
                # しかし display: "inline-block" にすると、横に並べられるようになります。
            },
        ),
        html.P(
            "こんにちは。今日は晴れました。",
            style={
                "fontSize": 50,  # フォントサイズ
                "color": "white",  # 文字色
                "backgroundColor": "red",  # 背景色
                "width": "40%",
                "display": "inline-block",  # ➊
                "verticalAlign": "top",
                # デフォルトでは、inline-block 要素は 
                # ベースライン（baseline） に揃うため、テキスト量の違いで位置がずれます。
                # "top" を指定すると、上下の高さが違っても 上端（top）で揃う
            },
        ),
    ]
)

if __name__ == "__main__":
    app.run_server(debug=True)