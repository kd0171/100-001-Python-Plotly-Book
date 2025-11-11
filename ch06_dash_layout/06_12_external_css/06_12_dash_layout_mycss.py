import dash
import dash_html_components as html
import dash_core_components as dcc
import plotly
import plotly.graph_objects as go

app = dash.Dash(__name__)

# # assets フォルダへの自動読み込み」は、実質的に external_stylesheets に登録しているのと同じ動作
# external_stylesheets = ["/assets/custom_style.css"]
# app = dash.Dash(__name__, external_stylesheets=external_stylesheets)


# assetsからの読み取る場合の文法の違い
    # | 項目     | CSSファイル（`style.css`）      | Python内の `style={...}`           |
    # | ------ | ------------------------- | -------------------------------- |
    # | 書式     | 通常のCSS構文                  | Python辞書（dictionary）構文           |
    # | プロパティ名 | ハイフン区切り（kebab-case）       | キャメルケース（camelCase）               |
    # | 値      | 単位を含む文字列（`500px`, `5%`など） | 同じく文字列。ただし `"500px"` のようにクォートが必要 |
    # | コメント   | `/* ... */`               | `# ...`                          |
    # | 定義方法   | `.クラス名 { ... }`           | 変数に辞書として代入                       |
    # | 適用方法   | `className="..."`         | `style={...}`                    |
# またcssでは改行時には；を用いる

app.layout = html.Div(
    [
        html.Div(
            [
                html.Div(className="roundsqlime columns"),
                html.Div(className="roundsqlime columns"),
            ],
        ),
        html.Div(
            [
                html.Div(className="roundsqblue columns"),
                html.Div(className="roundsqblue columns"),
                html.Div(className="roundsqblue columns"),
            ],
        )
    ],
)


if __name__ == "__main__":
    app.run_server(debug=True)