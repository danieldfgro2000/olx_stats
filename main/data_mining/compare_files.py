import os

import pandas as pd

from main.data_mining.a_return_csv_data import return_a_list_with_all_csv
from main.model.all_moto_atv_models import moto_atv_brand_model_dict, reduced_moto_atv_brand_model_dict
from main.utils.date_time import time_it, today, RetrievePreviousDays

pd.set_option('display.width', 1000)
pd.set_option(
    'display.max_rows', None,
    'display.max_columns', None,
    'display.max_colwidth', 200
)


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
    counter = 0
    for brand in reduced_moto_atv_brand_model_dict:

        list_of_csv_by_brand = []

        for model in reduced_moto_atv_brand_model_dict.get(brand):

            list_of_csv_by_model = []

            for csv in list_of_csv:
                if model in csv:
                    list_of_csv_by_model.append(csv)
            if len(list_of_csv_by_model) > 0:
                # save_by_brand_or_model_to_csv_from_all_csvs(csv_list=list_of_csv_by_model, model=model)
                list_of_csv_by_brand.extend(list_of_csv_by_model)
                counter += 1
        compare_last_two_files_for_model(list_of_csv_by_brand, brand)

        # if len(list_of_csv_by_brand) > 0:
        # save_by_brand_or_model_to_csv_from_all_csvs(csv_list=list_of_csv_by_brand, brand=brand)


def compare_last_two_files_for_model(list_of_csv, model):
    today_csv_list = []
    previous_csv_list = []
    number_of_days_to_check = 10
    prev_days_dict = RetrievePreviousDays(no_of_days=number_of_days_to_check).return_dict_for_no_of_prev_days()
    for prev_day in prev_days_dict:
        for csv in list_of_csv:
            day_in_csv = csv[len(csv) - 20: len(csv) - 12]
            if day_in_csv == today:
                today_csv_list.append(csv)
            if day_in_csv == prev_days_dict[prev_day]:
                previous_csv_list.append(csv)
        if len(today_csv_list) == 0:
            if len(previous_csv_list) > 0:
                today_csv_list = previous_csv_list
                previous_csv_list = []
        if len(previous_csv_list) > 0:
            break
    df1 = merge_csvs(today_csv_list)
    df2 = merge_csvs(previous_csv_list)

    if df1 is not None and df2 is not None:
        csv_join_path = '/home/daniel/PycharmProjects/olx_stats/main/data_mining/csv/join/'
        csv_sold_path = '/home/daniel/PycharmProjects/olx_stats/main/data_mining/csv/sold/'
        csv_new_path = '/home/daniel/PycharmProjects/olx_stats/main/data_mining/csv/new/'
        csv_df1_path = '/home/daniel/PycharmProjects/olx_stats/main/data_mining/csv/df1/'
        csv_df2_path = '/home/daniel/PycharmProjects/olx_stats/main/data_mining/csv/df2/'

        make_dir_if_does_not_exist(csv_df1_path)
        df1.to_csv(path_or_buf=f'{csv_df1_path}df1_{model}.csv')
        make_dir_if_does_not_exist(csv_df2_path)
        df2.to_csv(path_or_buf=f'{csv_df2_path}df2_{model}.csv')

        compare = pd.concat([df1, df2])
        compare.drop_duplicates(keep='first', subset='Link', inplace=True, ignore_index=True)

        # compare_sorted = compare.sort_values(by=['Model', 'Price', 'Year'], ignore_index=True)
        compare_grouped = compare.groupby(['Model', 'Price', 'Year', 'Location', 'added_date', 'Link'])
        if compare.size > 0:
            print("=" * 50)
            print(f'df1 size = {df1.size}, df2 size = {df2.size} compare = \n {compare_grouped.describe()}')
            print("=" * 50)

        join = pd.merge(df1, df2, how='outer', indicator=True)
        sold = join[join['_merge'] == 'right_only']
        new = join[join['_merge'] == 'left_only']

        make_dir_if_does_not_exist(csv_sold_path)
        make_dir_if_does_not_exist(csv_new_path)
        if sold.size > 0:
            sold.to_csv(path_or_buf=f'{csv_sold_path}sold_{model}.csv')
        if new.size > 0:
            new.to_csv(path_or_buf=f'{csv_new_path}new_{model}.csv')
            # print("=" * 50)
            # print(f" NEW = \n{new}")
            # print("=" * 50)
        # if sold.size > 0:

        # print("=" * 50)
        # print(f" SOLD = \n{sold}")
        # print("=" * 50)


def save_by_brand_or_model_to_csv_from_all_csvs(csv_list, brand=None, model=None):
    csv_model_path = '/home/daniel/PycharmProjects/olx_stats/main/data_mining/csv/model'
    csv_brand_path = '/home/daniel/PycharmProjects/olx_stats/main/data_mining/csv/brand'

    model_pd = merge_csvs(csv_list)
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
