import sys
import time

from selenium import webdriver
from selenium.webdriver.chromium.service import ChromiumService
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.common.exceptions import NoSuchElementException, TimeoutException, StaleElementReferenceException, \
	ElementClickInterceptedException

from main.utils.constants import WAIT_AFTER_LOADING


def setup_selenium_web_driver(input_url):
	chromium_path = "/usr/lib/chromium-browser/chromedriver"
	service_obj = ChromiumService(executable_path=chromium_path)
	selenium_web_driver = webdriver.Chrome(service=service_obj)
	selenium_web_driver.get(input_url)
	
	accept_tnc(selenium_web_driver)
	
	return selenium_web_driver


def accept_tnc(selenium_web_driver):
	try:
		WebDriverWait(selenium_web_driver, 1)
		selenium_web_driver.find_element(By.XPATH, "//*[@id='onetrust-accept-btn-handler']").click()
		WebDriverWait(selenium_web_driver, 3)
	except (NoSuchElementException, TimeoutException, StaleElementReferenceException):
		tb = sys.exc_info()[0]
		print(f"Scrape Data TraceBack {tb}")


def load_next_page_is_available(selenium_web_driver):
	try:
		selenium_web_driver.find_element(By.CSS_SELECTOR, 'a[data-testid="pagination-forward"]')
		return True
	except NoSuchElementException:
		tb = sys.exc_info()[0]
		print(f"Load Next Page TraceBack {tb}")
		return False


def click_on_next_button(selenium_web_driver):
	try:
		selenium_web_driver.find_element(By.CSS_SELECTOR, 'a[data-testid="pagination-forward"]').click()
		# print("Next Button Clicked")
		# print(f"Waiting for content to load... {WAIT_AFTER_LOADING} sec")
		time.sleep(WAIT_AFTER_LOADING)
		# print("Page loaded OK")
	except (TimeoutException, StaleElementReferenceException, ElementClickInterceptedException):
		tb = sys.exc_info()[0]
		print(f"Scrape Data TraceBack {tb}")
