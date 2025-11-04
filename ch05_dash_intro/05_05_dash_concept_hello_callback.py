import dash
import dash_core_components as dcc
import dash_html_components as html
import plotly.express as px
# コールバックに必要な依存関係
from dash.dependencies import Input, Output

core_style = {"width": "80%", "margin": "5% auto"}

app = dash.Dash(__name__)

app.layout = html.Div(
    [ 
        html.H1("Hello Dash", style={"textAlign": "center"}),
        dcc.Dropdown(
            # コールバックのためのidを設定
            id="my-dropdown",
            options=[
                {"label": "white", "value": "white"},
                {"label": "yellow", "value": "yellow"},
            ],
            value="white",
            style=core_style,
        ),

        dcc.Graph(
            figure=px.bar(x=[1, 2, 3, 4, 5], y=[1, 2, 3, 4, 5]), style=core_style,
        ),
    ],
    id="all-components",
)

@app.callback(
    # 戻り値の出力先を指定：
    # id="all-components" の html.Div コンポーネントの style プロパティを動的に変更する
    Output("all-components","style"),
    # コールバックの呼び出し要素：
    # Input で指定した値は、Dashが自動的に関数の引数に渡す
    Input("my-dropdown","value"),
)
def update_backdround(selected_value):
    # 関数の戻り値を指定
    return {"backgroundColor":selected_value, "padding":"3%"}

# 関数定義とInputの対応
    # @app.callback に複数の Input を渡した場合、関数の引数にも同じ順番で自動的に値が入ります。
    # 例：
            # @app.callback(
            #     Output("output-div", "children"),
            #     Input("dropdown1", "value"),
            #     Input("dropdown2", "value")
            # )
            # def update_text(val1, val2):
            #     return f"選択: {val1}, {val2}"

if __name__ == "__main__":
    app.run_server(debug=True)