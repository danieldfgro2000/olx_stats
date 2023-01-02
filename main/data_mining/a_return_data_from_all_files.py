import os
import sys
from enum import Enum

import pandas as pd

from main.utils.date_time import current_time

today = current_time.split(' ')[0]

scrapped_data_path = f'/home/daniel/PycharmProjects/olx_stats/main/selenium_scrapper/scrapped_data/'
today_scrapped_data_path = f'/home/daniel/PycharmProjects/olx_stats/main/selenium_scrapper/scrapped_data/{today}/'
honda_today_scrapped_data_path = f'/home/daniel/PycharmProjects/olx_stats/main/selenium_scrapper/scrapped_data/{today}/honda/'
kawasaki_today_scrapped_data_path = f'/home/daniel/PycharmProjects/olx_stats/main/selenium_scrapper/scrapped_data/{today}/kawasaki/'


class TimeFrameAndModelEnum(Enum):
	ALL = scrapped_data_path
	TODAY = today_scrapped_data_path
	HONDA = honda_today_scrapped_data_path
	KAWASAKI = kawasaki_today_scrapped_data_path


def return_data_from_all_files(timeframe_and_model: TimeFrameAndModelEnum):
	list_of_csv = []
	try:
		for root, dirs, files in os.walk(os.path.normpath(timeframe_and_model.value)):
			for file in files:
				rf = pd.read_csv(
					filepath_or_buffer=os.path.join(root, file),
					index_col=None,
					header=0,
					delimiter=',',
					names=['Price', 'Year', 'Location', 'added_date', 'Link', 'Title', 'Brand', 'Model',
					       'Type_moto_or_atv']
				)
				list_of_csv.append(rf)
		return pd.concat(list_of_csv, ignore_index=True)
	except ValueError:
		tb = sys.exc_info()[0]
		print(f"Return CSV list TraceBack {tb}")
		return pd.DataFrame({'A': []})
