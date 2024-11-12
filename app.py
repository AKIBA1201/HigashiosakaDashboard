# app.py

from dash import Dash
import webbrowser
from threading import Timer

# アプリケーションの初期化
app = Dash(__name__)

# 他のファイルからレイアウトとコールバックをインポート
from layout import layout
from callbacks import register_callbacks

# アプリのレイアウトを設定
app.layout = layout
print(app.layout)

# コールバック関数の登録
register_callbacks(app)

# サーバー起動設定
if __name__ == '__main__':
    port = 8051
    Timer(1, lambda: webbrowser.open(f'http://127.0.0.1:{port}')).start()
    app.run_server(debug=True, port=port, use_reloader=False)