import dash
import dash_html_components as html

app = dash.Dash(__name__)   # Dashインスタンスの生成
# dash.Dash クラス は アプリケーション（application instance） を作るためのコンストラクタ（constructor） です。
    # __name__ はPythonの**特殊変数（special variable）**で、現在のファイルのモジュール名を指します。
    # Dashは内部的にFlaskサーバを使うため、アプリの識別子として__name__を渡します。


# dash_html_components は HTMLタグをPythonの関数として使うためのモジュール 
app.layout = html.H1("Hello Dash")  # コンポーネントをlayout属性に渡す

if __name__ == "__main__":
    app.run_server(debug=True)  # アプリケーションの起動
