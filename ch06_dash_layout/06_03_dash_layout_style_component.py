import dash
import dash_html_components as html

app = dash.Dash(__name__)

app.layout = html.P(
    "こんにちは。昨日は雪が降りました。",
    style = {
        "fontSize":50,
        "color":"white",
        "backgroundColor":"#000000",
    },
)

if __name__ == "__main__":
    app.run_server(debug=True)