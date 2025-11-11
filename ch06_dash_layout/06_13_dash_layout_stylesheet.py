import dash
import dash_html_components as html

# className と style の役割分担
    # | 属性                | 役割                                                            | 書く場所     | 典型的な用途            |
    # | ----------------- | ------------------------------------------------------------- | -------- | ----------------- |
    # | `className="..."` | 外部CSS（`assets/style.css` や `external_stylesheets`）に書かれたルールを適用 | CSSファイル内 | **大きさ・配置・共通デザイン** |
    # | `style={...}`     | Pythonコード内で直接スタイル指定（インラインスタイル）                                | Dashコード内 | **色・高さなど個別の上書き**  |

# CSSのspecificity（詳細度）と宣言順 のルール：style={...} は常に className より強い
    # | 優先順位（強い→弱い）           | 適用元             | 説明                      |
    # | --------------------- | --------------- | ----------------------- |
    # | 🥇 **Inline style**   | `style={...}`   | 最強。常にclassや外部CSSより優先される |
    # | 🥈 **CSS内でのIDセレクタ指定** | `#id名 {}`       | 特定の要素IDに対しての指定          |
    # | 🥉 **CSSクラス指定**       | `.className {}` | 通常のクラス指定                |
    # | 🥈 **タグセレクタなど**       | `div {}`        | もっと弱い                   |

# ➊ 1段目用CSS辞書
div_style3 = {"height": "250px", "margin": "5%", "backgroundColor": "lime"}

# ➋ 2段目用CSS辞書
div_style4 = {"height": "250px", "backgroundColor": "skyblue"}

# ➌ スタイルシートの読み込み
external_sheet = ["https://codepen.io/chriddyp/pen/bWLwgP.css"]
app = dash.Dash(__name__, external_stylesheets=external_sheet)

app.layout = html.Div(
    [
        html.H1("5つの長方形を並べたアプリケーション"),
        # ➍ 1段目　2つの長方形
        html.Div(
            [
                # .columns は グリッド（12分割）で幅を割り当てるクラス
                    # 5/12 幅（約 41.7%）
                html.Div(style=div_style3, className="five columns"),
                html.Div(style=div_style3, className="five columns"),
            ],
            id="first_leader",
        ),
        # ➎ 2段目　3つの長方形
        html.Div(
            [
                html.Div(style=div_style4, className="four columns"),
                html.Div(style=div_style4, className="four columns"),
                html.Div(style=div_style4, className="four columns"),
            ]
        ),
    ]
)

if __name__ == "__main__":
    app.run_server(debug=True)