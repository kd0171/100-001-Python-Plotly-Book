import dash
import dash_html_components as html

app = dash.Dash(__name__)

# app.layout = html.Div(className="circle")   技術的には一重で問題ありません。
# 構造を整理して拡張しやすくするために二重にします
app.layout = html.Div([html.Div(className="circle")])  # className属性を設定

    # assets/ フォルダ内にある .css や .js ファイルは 自動で読み込まれます（auto-loaded）
    # 開発者が app.css.append_css() のような指定をする必要はありません
    # ファイル名は何でもOKですが、一般的には style.css を使います

if __name__ == "__main__":
    app.run_server(debug=True)