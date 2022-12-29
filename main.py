from facade_list_scrapper import list_scrapping
from main.utils.date_time import current_time_millis, time_passed

if __name__ == '__main__':
    start_time = current_time_millis
    list_scrapping()
    end_time = current_time_millis
    print(f'TIME: {time_passed}')


