from main.selenium_scrapper.handle_page_loading import setup_selenium_web_driver
from main.selenium_scrapper.scrape_list import init_data_scrapping

from main.selenium_scrapper import input_urls
from main.selenium_scrapper.write_list_data_to_csv import write_scrapped_data_to_csv

from main.utils.MotoEnumMod import MotoEnum
from main.utils.date_time import current_time, current_time_millis, time_passed


def list_scrapping():
	start_moto_scrapping()
	start_atv_scrapping()
	

def execute_scrapping(url, brand_add, type_moto_or_atv):
	print(f"Loading specific URL: {url}")
	print(f"Brand = {brand_add}")
	selenium_web_driver = setup_selenium_web_driver(url)
	scrapped_data_list = init_data_scrapping(selenium_web_driver)
	write_scrapped_data_to_csv(scrapped_data_list, brand_add, type_moto_or_atv)


def start_moto_scrapping():
	for brand in MotoEnum:
		execute_scrapping(url=input_urls.moto_url_list[brand.value - 1], type_moto_or_atv="MOTO", brand_add=brand.name)


def start_atv_scrapping():
	for brand in MotoEnum:
		execute_scrapping(url=input_urls.atv_url_list[brand.value - 1], type_moto_or_atv="ATV", brand_add=brand.name)
		


