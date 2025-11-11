import dash
import dash_html_components as html

app = dash.Dash(__name__)

app.layout = html.P(
    "こんにちは。昨日は雪が降りました。",
    style = {
        "fontSize":50,
        "color":"white",
        "backgroundColor":"#000000",
        "width":400,
        # "margin":"auto",
        "margin": "5% auto",   # 上下の余白を 5%、左右の余白を自動調整（auto）＝中央配置
    },
)

# 余白の指定
    # | 指定の個数 | 対応する辺（方向）                                | 例                       |
    # | ----- | ---------------------------------------- | ----------------------- |
    # | 4つ    | 上 (Top), 右 (Right), 下 (Bottom), 左 (Left) | `"10px 20px 30px 40px"` |
    # | 3つ    | 上, 左右, 下                                 | `"10px 20px 30px"`      |
    # | 2つ    | 上下, 左右                                   | `"10px 20px"`           |
    # | 1つ    | 全方向共通                                    | `"10px"`                |

if __name__ == "__main__":
    app.run_server(debug=True)