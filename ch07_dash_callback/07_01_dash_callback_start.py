import dash
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output, State

external_stylesheets = ["https://codepen.io/chriddyp/pen/bWLwgP.css"]

app = dash.Dash(__name__, external_stylesheets=external_stylesheets)

# ➊ レイアウト 各コンポーネントにIDを付ける
app.layout = html.Div(
    [
        # コールバックの返り値を表示する
        html.H1(id="head-title", children="初期タイトル"),
        # 文字を入力するテキストエリア
        dcc.Textarea(
            id="my-text-state",
            value="初期値", # 初期値の設定
            style={"width": "80%", "fontSize": 30},
        ),
        # クリックするとコールバックを呼び出すボタン
        html.Button(id="my-button", n_clicks=0, children="submit"),
    ],
    style={"margin": 50},
)

# ➋ コールバックの作成。
@app.callback(
    Output("head-title", "children"),  # ➌ 出力項目
    Input("my-button", "n_clicks"),  # ➍ 入力項目
    State("my-text-state", "value"),  # ➎ 状態項目
    prevent_initial_call=True  # 起動時に読み込まれてほしくない場合
)
# 2つめの引数（"children"や"n_clicks"）はproperty名と呼ばれ、使えるものはフレームワークで既に定義されたもののみ
# 各コンポーネント（例：html.H1, dcc.Textarea, html.Button など）には、「設定できる・読み取れるプロパティ」があらかじめ定義    # | コンポーネント                | 主なプロパティ                        | 説明                    |
    # | ---------------------- | ------------------------------ | --------------------- |
    # | `html.Div`             | `children`, `style`, `id`      | 子要素・見た目・ID            |
    # | `html.H1`, `html.P` など | `children`, `style`, `id`      | テキスト内容・スタイル           |
    # | `dcc.Input`            | `value`, `type`, `placeholder` | 入力値・入力種別・プレースホルダ      |
    # | `dcc.Textarea`         | `value`, `style`               | 入力文字列                 |
    # | `dcc.Slider`           | `value`, `min`, `max`, `marks` | スライダー値・範囲設定           |
    # | `dcc.Dropdown`         | `options`, `value`, `multi`    | 選択肢・選択値・複数選択設定        |
    # | `html.Button`          | `n_clicks`, `children`         | クリック回数・表示文字           |
    # | `dcc.Graph`            | `figure`                       | グラフデータ（Plotly figure） |



# ➏ コールバック関数
def update_title(n_clicks, text_value):
    return text_value

# 古いバージョンで初回起動で自動発火させたくない場合
# def update_title(n_clicks, text_value):
#     if n_clicks == 0:
#         # 起動直後（ボタン未クリック）の場合は変更しない
#         raise dash.exceptions.PreventUpdate
#     return text_value


if __name__ == "__main__":
    app.run_server(debug=True)