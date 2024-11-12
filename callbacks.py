# callbacks.py
import pandas as pd
from dash.dependencies import Output, Input
import plotly.express as px
import plotly.graph_objects as go
from layout import variable_options
from data_loader import map_data_town, population_data

def register_callbacks(app):
    # 地図を更新するコールバック関数
    @app.callback(
        Output('mapPlot', 'figure'),
        Input('variable', 'value')
    )
    def update_map(selected_var):
        display_label = [k for k, v in variable_options.items() if v == selected_var][0]
        
        fig = px.choropleth_mapbox(
            map_data_town,
            geojson=map_data_town.__geo_interface__,
            locations='S_NAME',
            color=selected_var,
            featureidkey='properties.S_NAME',
            mapbox_style="carto-positron",
            zoom=12.2,
            center={"lat": map_data_town.geometry.centroid.y.mean() + 0.005, "lon": map_data_town.geometry.centroid.x.mean() + 0.01},
            opacity=0.5,
            labels={selected_var: display_label}
        )
        
        fig.update_traces(
            hovertemplate="<b>%{location}</b><br>" + display_label + ": %{z}<extra></extra>"
        )
        
        fig.update_layout(margin={"r": 0, "t": 0, "l": 0, "b": 0})
        return fig

    # バープロットを更新するコールバック関数
    @app.callback(
        Output('barPlot', 'figure'),
        Input('mapPlot', 'clickData')
    )
    def update_bar(clickData):
         if clickData is None:
             return go.Figure()
         else:
                town_name = clickData['points'][0]['location']
                town_data = population_data[population_data['町名'] == town_name]
                if town_data.empty:
                    return go.Figure()
                
                # 年齢区分の列名とラベル
                age_groups = ['age_under_10', 'age_10_19', 'age_20_29', 'age_30_39', 'age_40_49',
                            'age_50_59', 'age_60_69', 'age_70_79', 'age_80_89', 'age_over_90']
                age_labels = ['10歳未満', '10代', '20代', '30代', '40代',
                            '50代', '60代', '70代', '80代', '90歳以上']
                
                # データ取得と欠損値補完
                try:
                    population_values = town_data[age_groups].iloc[0].fillna(0).values
                except KeyError as e:
                    print(f"Error: {e}")
                    return go.Figure()

                # グラフ作成
                df = pd.DataFrame({'AgeGroup': age_labels, 'Population': population_values})
                fig = px.bar(df, x='AgeGroup', y='Population', title=f'{town_name}の年齢層分布')
                fig.update_layout(xaxis_title='', yaxis_title='', xaxis_tickangle=45)
                return fig
