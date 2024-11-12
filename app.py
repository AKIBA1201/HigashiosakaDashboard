# app.py

from dash import Dash

# アプリケーションの初期化
app = Dash(__name__)

# 他のファイルからレイアウトとコールバックをインポート
from layout import layout
from callbacks import register_callbacks

# アプリのレイアウトを設定
app.layout = layout

# コールバック関数の登録
register_callbacks(app)

# サーバー起動設定
if __name__ == '__main__':
    app.run_server(host='0.0.0.0', port=8000, debug=True)
