import csv
import os
import sys

import tqdm
from selenium.common.exceptions import \
	NoSuchElementException, StaleElementReferenceException, ElementClickInterceptedException, \
	ElementNotInteractableException
from selenium.webdriver.common.by import By

from main.model.all_moto_atv_models import moto_atv_brand_model_dict, reduced_moto_atv_brand_model_dict
from main.selenium_scrapper.handle_page_loading import load_next_page_is_available, click_on_next_button
from main.utils.date_time import current_time


def init_data_scrapping(selenium_web_driver):
	print("START scrapping...")
	
	total_items = selenium_web_driver.find_element(By.CSS_SELECTOR, 'div[data-testid="total-count"').text.split(' ')[2]
	total_pages = 0
	page = 0
	if total_items != 0:
		total_pages = int(total_items) // 40
		if total_pages == 0:
			total_pages = 1
		print(f'total_pages = {total_pages}')
	print(f"total = {total_items}")
	
	scrapped_data_list = []
	
	while page <= total_pages:
		scrapped_data_list.extend(try_scrapping(selenium_web_driver, total_items))
		if load_next_page_is_available(selenium_web_driver):
			page += 1
			print(f'page = {page} [ {len(scrapped_data_list)} ]', end=' ')
			click_on_next_button(selenium_web_driver)
		else:
			break
	print(f"Finished for this type")
	return sorted(remove_duplicates(scrapped_data_list), key=lambda x: float(x[0]))


def try_scrapping(selenium_web_driver, total_of_elements):
	scrapped_data_list = []
	try:
		without_adds = selenium_web_driver.find_elements(By.CSS_SELECTOR, 'div[data-cy="l-card"]')
		
		if total_of_elements != '0':
			for element in tqdm.tqdm(without_adds):
				try:
					ad_link = element.find_element(By.XPATH, "./a").get_attribute("href")
					if 'extended_search_extended_category' in ad_link:
						continue
					ad_title = element.find_element(By.TAG_NAME, "h6").get_attribute("innerText")
					ad_price_1 = element.find_element(By.CSS_SELECTOR, "p[data-testid='ad-price']").get_attribute(
						"innerText").strip()
					if '€' in ad_price_1.split(' ')[1]:
						ad_price = float(ad_price_1.split(' ')[0].replace(',', '.'))
					else:
						ad_price = float(ad_price_1.split(' ')[0] + ad_price_1.split(' ')[1].replace(',', '.'))
					ad_year = element.find_element(By.CLASS_NAME, "css-efx9z5").get_attribute("innerText")
					ad_location_date = element.find_element(By.CSS_SELECTOR,
					                                        "p[data-testid='location-date'").text.split('-')
					ad_location = ad_location_date[0]
					ad_relisting = ad_location_date[len(ad_location_date) - 1]
					if "Azi" in ad_relisting:
						ad_listing_date = current_time.split(' ')[0]
					elif "Reactualizat" in ad_relisting:
						ad_listing_date = current_time.split(' ')[0] + " Reactualizat"
					else:
						ad_listing_date = ad_relisting
				except (NoSuchElementException, StaleElementReferenceException, ElementNotInteractableException,
				        ElementClickInterceptedException):
					tb = sys.exc_info()[0]
					print(f"Scrape Data TraceBack {tb}")
					continue
				
				for brand in moto_atv_brand_model_dict:
					if brand in ad_link or brand in ad_title:
						add_brand = brand
						for model in moto_atv_brand_model_dict.get(brand):
							if model in ad_link:
								add_model = model
								add_type = moto_atv_brand_model_dict.get(brand).get(model)
								
								scrapped_data_list.append([
									total_of_elements,
									ad_price,
									ad_year,
									ad_location,
									ad_listing_date,
									ad_link,
									ad_title,
									add_brand,
									add_model,
									add_type
								])
	except (NoSuchElementException, StaleElementReferenceException, ElementNotInteractableException,
	        ElementClickInterceptedException):
		tb = sys.exc_info()[0]
		print(f"Scrape Data TraceBack {tb}")
	
	return scrapped_data_list


def remove_duplicates(scrapped_data_list):
	without_duplicates = []
	for add in scrapped_data_list:
		if add not in without_duplicates:
			without_duplicates.append(add)
	return without_duplicates
