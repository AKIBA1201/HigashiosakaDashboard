# data_loader.py
import os
import pandas as pd
import geopandas as gpd

# プロジェクトのルートディレクトリを取得
BASE_DIR = os.path.dirname(os.path.abspath(__file__))

# Excelデータの読み込み
population_data = pd.read_excel(os.path.join(BASE_DIR, "町目別20240930.xlsx"), skiprows=1)
population_data.columns.values[0] = '町名'
population_data.columns = population_data.columns.str.replace(r'[\n\r\s　]+', '', regex=True)

# 年齢区分ごとの合計列を作成
population_data = population_data.assign(
    age_under_10=population_data['０歳～４歳'] + population_data['５歳～９歳'],
    age_10_19=population_data['１０歳～１４歳'] + population_data['１５歳～１９歳'],
    age_20_29=population_data['２０歳～２４歳'] + population_data['２５歳～２９歳'],
    age_30_39=population_data['３０歳～３４歳'] + population_data['３５歳～３９歳'],
    age_40_49=population_data['４０歳～４４歳'] + population_data['４５歳～４９歳'],
    age_50_59=population_data['５０歳～５４歳'] + population_data['５５歳～５９歳'],
    age_60_69=population_data['６０歳～６４歳'] + population_data['６５歳～６９歳'],
    age_70_79=population_data['７０歳～７４歳'] + population_data['７５歳～７９歳'],
    age_80_89=population_data['８０歳～８４歳'] + population_data['８５歳～８９歳'],
    age_over_90=population_data['９０歳～９４歳'] + population_data['９５歳～９９歳'] + population_data['１００歳以上'],
    age_under_20=population_data['０歳～４歳'] + population_data['５歳～９歳'] + population_data['１０歳～１４歳'] + population_data['１５歳～１９歳'],
    age_20_39=population_data['２０歳～２４歳'] + population_data['２５歳～２９歳'] + population_data['３０歳～３４歳'] + population_data['３５歳～３９歳'],
    age_40_59=population_data['４０歳～４４歳'] + population_data['４５歳～４９歳'] + population_data['５０歳～５４歳'] + population_data['５５歳～５９歳'],
    age_60_79=population_data['６０歳～６４歳'] + population_data['６５歳～６９歳'] + population_data['７０歳～７４歳'] + population_data['７５歳～７９歳'],
    age_over_80=population_data['８０歳～８４歳'] + population_data['８５歳～８９歳'] + population_data['９０歳～９４歳'] + population_data['９５歳～９９歳'] + population_data['１００歳以上']
)

# GeoJSON形式の地図データを読み込み
map_data_town = gpd.read_file(os.path.join(BASE_DIR, "higashiosaka.GeoJSON"), layer="town")
map_data_town = map_data_town.merge(population_data, left_on='S_NAME', right_on='町名', how='left')
