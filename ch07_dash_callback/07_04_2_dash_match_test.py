import dash
from dash import html, dcc
from dash.dependencies import Input, Output, State, MATCH
import plotly.express as px

gapminder = px.data.gapminder()
app = dash.Dash(__name__)

app.layout = html.Div(
    [
        html.Button("Add", id="add_btn"),
        html.Div(id="container", children=[]),
    ]
)

# 子を “積み増し” する
@app.callback(
    Output("container", "children"),
    Input("add_btn", "n_clicks"),
    State("container", "children"),
    prevent_initial_call=True
)
def add_dropdown(n, children):
    # 追加する index を一意にする（既存数を使うと安全）
    idx = (len(children) // 1) + 1
    new = html.Div([
        dcc.Dropdown(
            id={"type": "my_dropdown", "index": idx},
            options=[{"label": c, "value": c} for c in gapminder.country.unique()],
            value="Japan"
        ),
        dcc.Graph(id={"type": "my_graph", "index": idx})
    ])
    return children + [new]   # ← 1個だけ追加して返す

# MATCH：各ペアを個別に更新
@app.callback(
    Output({"type": "my_graph", "index": MATCH}, "figure"),
    Input({"type": "my_dropdown", "index": MATCH}, "value")
)
def update_graph(selected_country):
    df = gapminder[gapminder.country == selected_country]
    return px.line(df, x="year", y="gdpPercap", title=selected_country)

if __name__ == "__main__":
    app.run_server(debug=True)
