import dash
import dash_html_components as html
import dash_core_components as dcc
import plotly
import plotly.graph_objects as go

app = dash.Dash(__name__)

app.layout = html.Div(
    style={
        "width": "500px",  # 横幅: 500px
        "height": "250px",  # 高さ: 250px
        "backgroundColor": "lime",  # 背景色: ライム
        "margin": "50px auto 50px",  # 要素の外側の余白領域 上下50px、autoで中央寄せ
    }
)

# 「margin」プロパティの4方向指定
    # | 値の数 | 意味（順番）     | 例                                                        |
    # | --- | ---------- | -------------------------------------------------------- |
    # | 1つ  | 上下左右すべて同じ  | `margin: 20px;` → 上右下左すべて20px                            |
    # | 2つ  | 上下, 左右     | `margin: 10px 20px;` → 上下10px、左右20px                     |
    # | 3つ  | 上, 左右, 下   | `margin: 10px 20px 30px;` → 上10px、左右20px、下30px           |
    # | 4つ  | 上, 右, 下, 左 | `margin: 10px 20px 30px 40px;` → 上10px、右20px、下30px、左40px |


if __name__ == "__main__":
    app.run_server(debug=True)