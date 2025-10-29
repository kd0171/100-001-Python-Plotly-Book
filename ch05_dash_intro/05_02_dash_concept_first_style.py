import dash
import dash_html_components as html

app = dash.Dash(__name__)

app.layout = html.H1(
    "Hello Dash",
    # スタイルの設定
    style = {"color":"red", "textAlign":"center"},
)

if __name__ == "__main__":
    app.run_server(debug=True)