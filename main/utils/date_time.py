import time
from datetime import datetime

now = datetime.now()
current_time = now.strftime("%Y-%m-%d %H:%M:%S")
today = now.strftime('%Y-%m-%d')
yesterday = today.split('-')[0] + '-' + today.split('-')[1] + '-' + str(int(today.split('-')[2]) - 1)

current_time_millis = now.microsecond


class RetrievePreviousDays:

    def __init__(self, day=today, no_of_days=0):
        self.today = day
        self.prev_day = today
        self.no_of_days = no_of_days
        self.day_int = int(self.today.split('-')[2])
        self.month_int = int(self.today.split('-')[1])
        self.year_int = int(self.today.split('-')[0][2:4])

    def _is_month_with_31_day(self):
        n = self.month_int - 1
        return n == 1 or n == 3 or n == 5 or n == 7 or n == 8 or n == 10 or n == 12

    def is_month_with_28_day(self):
        return self.month_int - 1 == 2

    def is_first_month(self):
        return self.month_int == 1

    def is_previous_month(self):
        return self.day_int - self.no_of_days <= 0

    @staticmethod
    def return_month_starting_with_zero(month_int):
        if month_int < 10:
            month_str = f'0{month_int}'
        else:
            month_str = str(month_int)
        return month_str

    def return_n_prev_day(s):
        if s.no_of_days == 0:
            s.prev_day = s.today
        else:
            if s.is_previous_month():
                s.set_prev_day_based_on_month()
            else:
                month_str = s.return_month_starting_with_zero(s.month_int)
                s.prev_day = str(s.year_int) + '-' + month_str + '-' + str(s.day_int - s.no_of_days)
        return s.prev_day

    def set_prev_day_based_on_month(s):
        if s.is_first_month():
            s.prev_day = str(s.year_int - 1) + '-' + '12' + '-' + str(
                31 + s.day_int - s.no_of_days)
        elif s._is_month_with_31_day():
            s.prev_day = str(s.year_int) + '-' + s.return_month_starting_with_zero(
                s.month_int - 1) + '-' + str(
                31 + s.day_int - s.no_of_days)
        elif s.is_month_with_28_day():
            s.prev_day = str(s.year_int) + '-' + s.return_month_starting_with_zero(
                s.month_int - 1) + '-' + str(
                28 + s.day_int - s.no_of_days)
        else:
            s.prev_day = str(s.year_int) + '-' + s.return_month_starting_with_zero(
                s.month_int - 1) + '-' + str(
                30 + s.day_int - s.no_of_days)

    def return_dict_for_no_of_prev_days(self):
        dict_prev_days: dict = {}
        for i in range(1, self.no_of_days + 1):
            self.no_of_days = i
            self.return_n_prev_day()
            day_key = f'day-{i}'
            day_value = self.prev_day
            dict_prev_days.update({day_key: day_value})
        return dict_prev_days


def time_it(func):
    def measure_time(*args, **kw):
        start_time = time.time()
        result = func(*args, **kw)
        print("Processing time of %s(): %.3f seconds." % (func.__qualname__, time.time() - start_time))
        return result

    return measure_time


if __name__ == "__main__":
    # print(f'now = {now}')
    # print(f"current time = {current_time}")
    # print(f"current time millis = {current_time_millis}")
    # print(f'today = {today}')
    # print(f'yesterday = {yesterday}')
    RetrievePreviousDays(no_of_days=10).return_dict_for_no_of_prev_days()
