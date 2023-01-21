import os

import pandas as pd

from main.data_mining.a_return_csv_data import return_a_list_with_all_csv


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


def merge_csvs_with_same_date_and_model(list_of_csv):
	if len(list_of_csv) > 1:
		# print(f'{[csv[len(csv) - 40:len(csv) - 23] for csv in list_of_csv]}')
		new_list = []
		for csv in list_of_csv:
			day = csv[len(csv) - 14: len(csv) - 12]
			month = csv[len(csv) - 17: len(csv) - 15]
			year = csv[len(csv) - 20: len(csv) - 18]
			new_list.append(pandas_read_csv(csv))
			print(f'{day}-{month}-{year}')
		
		merged = pd.concat(new_list, ignore_index=True)
		merged.drop_duplicates()
		print(merged.size)


def group_csvs_by_model():
	list_of_csv = return_a_list_with_all_csv()
	dict_csv = {}
	for x in list_of_csv:
		model = x[len(x) - 40:len(x) - 23]
		group = dict_csv.get(model, [])
		group.append(x)
		# print(f'model = {model}')
		dict_csv[model] = group
	
	for model in dict_csv:
		listing = dict_csv.get(model)
		merge_csvs_with_same_date_and_model(listing)
		print(f'model = {model}')
	# print(f'listing= {listing}')
	return dict_csv


group_csvs_by_model()


def compare_last_two_files():
	# pd.set_option('display.max_rows', None)
	# pd.set_option('display.max_columns', None)
	dict_csv = group_csvs_by_model()
	for model in dict_csv:
		rf_1 = pd.read_csv(dict_csv.get(model)[len(dict_csv.get(model)) - 1])
		# print(dict_csv.get(model)[len(dict_csv.get(model)) - 1])
		rf_2 = pd.read_csv(dict_csv.get(model)[len(dict_csv.get(model)) - 2])
		# print(dict_csv.get(model)[len(dict_csv.get(model)) - 2])
		result = pd.merge(rf_1, rf_2, how='right')
# print(result)

# compare_last_two_files()
