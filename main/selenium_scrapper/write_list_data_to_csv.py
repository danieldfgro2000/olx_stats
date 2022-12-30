import csv
import os.path

from main.utils.date_time import current_time


def write_scrapped_data_to_csv(list_of_adds, type_atv_or_moto, brand):
	today = current_time.split(' ')[0]
	with open(f'/home/daniel/PycharmProjects/olx_stats/main/selenium_scrapper/scrapped_data/'
	          f'{today}-{type_atv_or_moto}-{brand}.listing.csv', 'w+', newline='', encoding="utf-8") as file:
		writer = csv.writer(file)
		headers = ['Link', 'Title', 'Price', 'Year', 'Second', 'Listing date', 'Location']
		writer.writerow(headers)
		print("Writing to CSV")
		for data in list_of_adds:
			writer.writerow(data)


def write_scrapped_model_data_to_csv(list_of_adds):
	today = current_time.split(' ')[0]
	scrapped_path = "main/selenium_scrapper/scrapped_data/"
	if not os.path.isdir(f'{scrapped_path}{today}'):
		os.makedirs(f'{scrapped_path}{today}/')
	for data in list_of_adds:
		brand = data[6]
		model = data[7]
		if brand is not None and model is not None:
			if not os.path.isdir(f"{scrapped_path}{today}/{brand}"):
				os.makedirs(f"{scrapped_path}{today}/{brand}")
			with open(f'{scrapped_path}{today}/{brand}/'
			          f'{today}-{brand}-{model}.listing.csv', 'a+', newline='',
			          encoding="utf-8") as file:
				writer = csv.writer(file)
				writer.writerow(data)


