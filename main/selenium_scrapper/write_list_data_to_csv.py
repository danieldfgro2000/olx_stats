import csv

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
