import csv
import os.path

from main.selenium_scrapper.input_urls import moto_models, atv_models
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
	
	for data in list_of_adds:
		type_atv_or_moto = get_type(data)
		brand = get_brand(data)
		model = get_model(data)
		
		if brand is not None and model is not None:
			scrapped_path = "main/selenium_scrapper/scrapped_data/"
			if not os.path.isdir(f"{scrapped_path}{brand}"):
				os.makedirs(f"{scrapped_path}{brand}/")
			with open(f'{scrapped_path}{brand}'
			          f'{today}-{type_atv_or_moto}-{brand}-{model}.listing.csv', 'a+', newline='',
			          encoding="utf-8") as file:
				writer = csv.writer(file)
				writer.writerow(data)


def get_model(data):
	for brand in moto_models:
		for moto_model in brand:
			if moto_model in data[1]:
				return moto_model
	
	for brand in atv_models:
		for atv_model in brand:
			if atv_model in data[1]:
				return atv_model


def get_brand(data):
	if 'kawasaki' in data[1]:
		brand = 'kawasaki'
	elif 'honda' in data[1]:
		brand = 'honda'
	elif 'yamaha' in data[1]:
		brand = 'yamaha'
	elif 'suzuki' in data[1]:
		brand = 'suzuki'
	else:
		brand = None
	return brand


def get_type(data):
	if 'atv' in data[1]:
		type_atv_or_moto = 'atv'
	elif 'moto' in data[1]:
		type_atv_or_moto = 'moto'
	else:
		type_atv_or_moto = 'moto'
	return type_atv_or_moto
