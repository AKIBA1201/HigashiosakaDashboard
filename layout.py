# layout.py

from dash import dcc, html

# `variable_options` は選択肢リストなのでここに定義
variable_options = {
    "人口総数": "人口総数",
    "世帯数": "世帯数",
    "男性": "男",
    "女性": "女",
    "10代未満": "age_under_10",
    "10代": "age_10_19",
    "20代": "age_20_29",
    "20代と30代": "age_20_39",
    "30代": "age_30_39",
    "40代": "age_40_49",
    "40代と50代": "age_40_59",
    "50代": "age_50_59",
    "60代": "age_60_69",
    "60代と70代": "age_60_79",
    "70代": "age_70_79",
    "80代": "age_80_89",
    "80代以上": "age_over_80",
    "90代以上": "age_over_90"
}

# レイアウト構成
layout = html.Div([
    html.Div([
        html.Div(style={'height': '50px'}),
        dcc.Dropdown(
            id='variable',
            options=[{'label': k, 'value': v} for k, v in variable_options.items()],
            value='人口総数',
            style={'width': '100%'}
        ),
        dcc.Graph(id='barPlot', style={'height': '600px'})
    ], style={'width': '25%', 'display': 'inline-block', 'verticalAlign': 'top'}),
    html.Div([
        dcc.Graph(id='mapPlot', style={'height': '750px', 'width': '100%'})
    ], style={'width': '75%', 'display': 'inline-block', 'verticalAlign': 'top'})
])
