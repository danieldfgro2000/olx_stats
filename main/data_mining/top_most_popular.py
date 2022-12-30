import os

import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns

from main.utils.date_time import current_time

today = current_time.split(' ')[0]

scrapped_data_path = f'/home/daniel/PycharmProjects/olx_stats/main/selenium_scrapper/scrapped_data/{today}/kawasaki/'


def return_data_from_all_files():
	list_of_csv = []
	for root, dirs, files in os.walk(os.path.normpath(scrapped_data_path)):
		for file in files:
			rf = pd.read_csv(
				filepath_or_buffer=os.path.join(root, file),
				index_col=None,
				header=0,
				delimiter=',',
				names=['Price', 'Year', 'Location', 'added_date', 'Link', 'Title', 'Brand', 'Model', 'Type_moto_or_atv']
			)
			list_of_csv.append(rf)
	return pd.concat(list_of_csv, ignore_index=True)


all_moto_list = return_data_from_all_files()
moto_count = all_moto_list.groupby(['Model', 'Year', 'Price']).size().reset_index(name='Location')

model_count = moto_count.Model.value_counts().index
g = sns.catplot(
	data=moto_count,
	row='Model',
	row_order=model_count,
	height=1.7,
	aspect=4
)
g.map(sns.kdeplot, 'Model count')

plt.show()
