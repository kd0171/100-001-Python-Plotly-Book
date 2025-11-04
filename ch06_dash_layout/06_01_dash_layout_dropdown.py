import dash
import dash_core_components as dcc

app = dash.Dash(__name__)

# layout 属性に 表示するコンポーネント（component） を指定
    # ここでは Dropdown（ドロップダウンメニュー） コンポーネントをひとつだけ配置
app.layout =  dcc.Dropdown()

# Dashでは、レイアウトに設定できるのは「コンポーネント（component）」です。
    # その最上位に置けるのは：
    # 単一のコンポーネント（例：dcc.Dropdown()）
    # または複数をまとめたコンテナ（container）（例：html.Div([...])）

# html.Div は「複数の部品をまとめて配置するためのキャンバス（canvas）」 のようなもの

if __name__ == "__main__":
    app.run_server(debug=True)