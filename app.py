# app.py
from dash import Dash
import os

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
    port = int(os.environ.get("PORT", 8000))  # 環境変数PORTがあればそれを使い、なければ8000を使う
    app.run_server(host='0.0.0.0', port=port, debug=True)
