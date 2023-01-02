import os
import pandas as pd

scrapped_data_path = f'/home/daniel/PycharmProjects/olx_stats/main/selenium_scrapper/scrapped_data/'


def return_list_with_all_csvs():
	list_of_csv = []
	
	for root, dirs, files in os.walk(os.path.normpath(scrapped_data_path)):
		for file in files:
			new_file = os.path.join(root, file)
			
			list_of_csv.append(new_file)
	
	print(f'csv size = {len(list_of_csv)}')
	return list_of_csv


# return_list_with_all_csvs()

def compare_files():
	
	for index in range(len(return_list_with_all_csvs())):
		rf_1 = pd.read_csv(return_list_with_all_csvs()[index])
		rf_2 = pd.read_csv(return_list_with_all_csvs()[index + 1])
		# result = pd.merge(rf_1, rf_2)
	# print(result)
	
# compare_files()
	