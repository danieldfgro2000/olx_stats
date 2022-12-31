import matplotlib.pyplot as plt
import matplotlib.ticker
import numpy as np
import seaborn as sns

from main.data_mining.a_return_data_from_all_files import return_data_from_all_files, TimeFrameAndModelEnum

sns.set_theme(style='darkgrid')
sns.set(rc={'axes.facecolor': 'cornflowerblue'})


def show_plot():
	ax = plt.gca()
	ax.xaxis.set_major_locator(matplotlib.ticker.MultipleLocator(500))
	ax.yaxis.set_major_locator(matplotlib.ticker.MultipleLocator(1))
	plt.show()


all_moto_list = return_data_from_all_files(TimeFrameAndModelEnum.ALL)


def show_most_popular():
	moto_count = all_moto_list.groupby(['Model', 'Year', 'Price']).size().reset_index(name="Location")
	model_count = moto_count.Model.value_counts().iloc[:20]
	
	print(f'model count= \n {model_count}')
	sns.countplot(
		data=moto_count,
		y='Model',
		hue='Model',
		palette='Greens_d',
		order=moto_count.Model.value_counts().iloc[:20].index
	)
	plt.show()


def show_most_popular_by_year():
	moto_count = all_moto_list.groupby(['Year', 'Price', 'Model'])

	print(moto_count.size())
	
	sns.catplot(
		data=all_moto_list
		.sort_values('Model')
		.groupby("Model").filter(lambda x: len(x) > 30),
		x='Year',
		y='Model',
		kind='box'
	)
	plt.show()


def show_most_popular_by_price():
	sns.catplot(
		data=all_moto_list
		.sort_values('Model')
		.groupby("Model")
		.filter(lambda x: len(x) > 30),
		x='Model',
		y='Price',
		kind='boxen'
	)
	plt.show()


def show_most_popular_by_price_and_year():
	sns.relplot(
		data=all_moto_list
		.sort_values('Model')
		.groupby('Model')
		.filter(lambda x: len(x) > 30),
		x='Price',
		y='Year',
		col='Model',
		col_wrap=5,
		# hue='Price',
		# style='choice',
		# kind='line',
		dashes=False,
		markers=True
	
	)
	plt.show()
	

def show_price_estimation(query_model):
	sns.lmplot(
		data=all_moto_list.query(f'Model == "{query_model}"'),
		x='Price',
		y='Year',
		ci=None,
		scatter_kws={'s': 80}
	)
	show_plot()


# show_most_popular()
# show_most_popular_by_year()
# show_most_popular_by_price()
# show_most_popular_by_price_and_year()
show_price_estimation('z750')
