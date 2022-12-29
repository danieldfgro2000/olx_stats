from operator import itemgetter
import tqdm
from selenium.common.exceptions import \
	NoSuchElementException, StaleElementReferenceException, ElementClickInterceptedException, \
	ElementNotInteractableException
from selenium.webdriver.common.by import By

from main.selenium_scrapper.handle_page_loading import load_next_page_is_available, click_on_next_button
from main.utils.date_time import current_time
import sys


def init_data_scrapping(selenium_web_driver):
	print("START scrapping...")
	
	total_items = selenium_web_driver.find_element(By.CSS_SELECTOR, 'div[data-testid="total-count"').text.split(' ')[2]
	print(f"total = {total_items}")
	
	scrapped_data_list = []
	
	while len(scrapped_data_list) < int(total_items):
		scrapped_data_list.extend(try_scrapping(selenium_web_driver, total_items))
		
		if load_next_page_is_available(selenium_web_driver):
			click_on_next_button(selenium_web_driver)
		else:
			break
	print(f"Finished for this type")

	return sorted(scrapped_data_list, key=itemgetter(2))


def try_scrapping(selenium_web_driver, total_of_elements):
	
	scrapped_data_list = []
	try:
		without_adds = selenium_web_driver.find_elements(By.CSS_SELECTOR, 'div[data-cy="l-card"]')
		
		if total_of_elements != '0':
			for element in tqdm.tqdm(without_adds):
				try:
					ad_link = element.find_element(By.XPATH, "./a").get_attribute("href")
					
					ad_title = element.find_element(By.TAG_NAME, "h6").get_attribute("innerText")
					
					ad_price_1 = element.find_element(By.CSS_SELECTOR, "p[data-testid='ad-price']").get_attribute(
						"innerText").strip()
					if '€' in ad_price_1.split(' ')[1]:
						ad_price = float(ad_price_1.split(' ')[0].replace(',', '.'))
					else:
						ad_price = float(ad_price_1.split(' ')[0] + ad_price_1.split(' ')[1].replace(',', '.'))
					
					# print(f"price = '{ad_price}'")
					ad_year = element.find_element(By.CLASS_NAME, "css-efx9z5").get_attribute("innerText")
					
					ad_location_date = element.find_element(By.CSS_SELECTOR,
					                                        "p[data-testid='location-date'").text.split('-')
					ad_location = ad_location_date[0]
					
					ad_relisting = ad_location_date[len(ad_location_date) - 1]
					if "Azi" in ad_relisting:
						ad_listing_date = current_time.split(' ')[0]
					elif "Reactualizat" in ad_relisting:
						ad_listing_date = "Reactualizat" + current_time.split(' ')[0]
					else:
						ad_listing_date = ad_relisting
				
				except (NoSuchElementException, StaleElementReferenceException, ElementNotInteractableException,
				        ElementClickInterceptedException):
					tb = sys.exc_info()[0]
					print(f"Scrape Data TraceBack {tb}")
					continue
				scrapped_data_list.append([ad_link, ad_title, ad_price, ad_year, ad_listing_date, ad_location])
	except (NoSuchElementException, StaleElementReferenceException, ElementNotInteractableException,
	        ElementClickInterceptedException):
		tb = sys.exc_info()[0]
		print(f"Scrape Data TraceBack {tb}")
	return scrapped_data_list

