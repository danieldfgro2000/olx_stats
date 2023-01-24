import os

import pandas as pd

from main.data_mining.a_return_csv_data import return_a_list_with_all_csv
from main.model.all_moto_atv_models import moto_atv_brand_model_dict
from main.utils.date_time import time_it, today, yesterday


def pandas_read_csv(path):
    return pd.read_csv(
        filepath_or_buffer=os.path.realpath(path),
        index_col=None,
        header=0,
        delimiter=',',
        names=[
            'Price',
            'Year',
            'Location',
            'added_date',
            'Link',
            'Title',
            'Brand',
            'Model',
            'Type_moto_or_atv'
        ]
    )


def merge_csvs(csv_list):
    if len(csv_list) > 0:
        model_pd = pd.concat(map(pandas_read_csv, csv_list), ignore_index=True)
        model_pd.drop_duplicates(subset='Link', keep='first', inplace=True, ignore_index=True)
        return model_pd


def make_dir_if_does_not_exist(path):
    if not os.path.exists(path):
        os.makedirs(path)


@time_it
def iterate_trough_csvs_by_model():
    list_of_csv = return_a_list_with_all_csv()

    for brand in moto_atv_brand_model_dict:

        list_of_csv_by_brand = []

        for model in moto_atv_brand_model_dict.get(brand):

            list_of_csv_by_model = []

            for csv in list_of_csv:
                if model in csv:
                    list_of_csv_by_model.append(csv)
            if len(list_of_csv_by_model) > 0:
                # save_by_brand_or_model_to_csv_from_all_csvs(csv_list=list_of_csv_by_model, model=model)
                list_of_csv_by_brand.extend(list_of_csv_by_model)

                compare_last_two_files_for_model(list_of_csv_by_model)


        # if len(list_of_csv_by_brand) > 0:
        # save_by_brand_or_model_to_csv_from_all_csvs(csv_list=list_of_csv_by_brand, brand=brand)


def compare_last_two_files_for_model(list_of_csv):
    today_csv_list = []
    yesterday_csv_list = []

    number_of_days_to_check = 10

    for csv in list_of_csv:

        day_in_csv = csv[len(csv) - 20: len(csv) - 12]

        if day_in_csv == today:
            today_csv_list.append(csv)

        if day_in_csv == yesterday:
            # print(f'f append csv = {csv}')
            # print(f'f yesterday size = {csv}')
            yesterday_csv_list.append(csv)

    df1 = merge_csvs(today_csv_list)

    df2 = merge_csvs(yesterday_csv_list)
    print(f'df2 = {df2}')
    if df1 is not None and df2 is not None:
        merged = pd.merge(df1, df2)
        print(f" merged = {merged}")
        # print(pd)
    # rf_1 = pd.read_csv(dict_csv.get(model)[len(dict_csv.get(model)) - 1])
    #
    # rf_2 = pd.read_csv(dict_csv.get(model)[len(dict_csv.get(model)) - 2])
    #
    # result = pd.merge(rf_1, rf_2, how='right')


def save_by_brand_or_model_to_csv_from_all_csvs(csv_list, brand=None, model=None):
    csv_model_path = '/home/daniel/PycharmProjects/olx_stats/main/data_mining/csv/model'
    csv_brand_path = '/home/daniel/PycharmProjects/olx_stats/main/data_mining/csv/brand'

    model_pd = None

    merge_csvs(csv_list)
    if model and model_pd is not None:
        csv_path = csv_model_path
        make_dir_if_does_not_exist(csv_path)
        model_pd.to_csv(path_or_buf=f'{csv_path}/{model}.csv')

    if brand and model_pd is not None:
        csv_path = csv_brand_path
        make_dir_if_does_not_exist(csv_path)
        model_pd.to_csv(path_or_buf=f'{csv_path}/{brand}.csv')


if __name__ == '__main__':
    # save_by_brand_or_model_to_csv_from_all_csvs()
    iterate_trough_csvs_by_model()
