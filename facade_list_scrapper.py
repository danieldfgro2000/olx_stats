from main.selenium_scrapper.handle_page_loading import setup_selenium_web_driver
from main.selenium_scrapper.input_urls import return_url_list
from main.selenium_scrapper.scrape_list import init_data_scrapping

from main.selenium_scrapper import input_urls
from main.selenium_scrapper.write_list_data_to_csv import write_scrapped_data_to_csv, write_scrapped_model_data_to_csv

from main.utils.MotoEnumMod import MotoEnum
from main.utils.date_time import current_time, current_time_millis, time_passed


def execute_scrapping(url, brand_add, type_moto_or_atv):
	print(f"Loading specific URL: {url}")
	print(f"Brand = {brand_add}")
	selenium_web_driver = setup_selenium_web_driver(url)
	scrapped_data_list = init_data_scrapping(selenium_web_driver)
	write_scrapped_data_to_csv(scrapped_data_list, brand_add, type_moto_or_atv)
	
	
def execute_model_scrapping():
	for url in return_url_list(year='1990', engine_size='250'):
		print(f"Loading specific URL: {url}")
		selenium_web_driver = setup_selenium_web_driver(url)
		scrapped_data_list = init_data_scrapping(selenium_web_driver)
		write_scrapped_model_data_to_csv(scrapped_data_list)


