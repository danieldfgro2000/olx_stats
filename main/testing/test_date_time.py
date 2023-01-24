from main.utils.date_time import RetrievePreviousDays


def test__is_month_with_31_day():
    list_of_months_with_31_days = [1, 3, 5, 7, 8, 10, 12]
    for i in list_of_months_with_31_days:
        month_to_test = i + 1  # 1 to subtract for prev month
        day = f'2023-{month_to_test}-24'
        assert RetrievePreviousDays(day=day).is_month_with_31_day() is True


def test__is_not_month_with_31_day():
    list_of_months_with_31_days = [1, 3, 5, 7, 8, 10, 12]
    for i in list_of_months_with_31_days:
        month_to_test = i + 2  # 1 to subtract for prev month, 1 for not month
        if i == 7:
            month_to_test = i + 3
        day = f'2023-{month_to_test}-24'
        assert RetrievePreviousDays(day=day).is_month_with_31_day() is False


def test__is_month_with_28_day():
    month_to_test = 3 # 2 (Feb) + 1 to subtract for prev month
    day = f'2023-{month_to_test}-24'
    assert RetrievePreviousDays(day=day).is_month_with_28_day() is True


def test__calc_prev_day_is_today():
    day_to_return = '2023-01-24'
    today = '2023-01-24'
    no_of_days = 0
    day_returned = RetrievePreviousDays(day=today, no_of_days=no_of_days).return_n_prev_day()
    assert day_returned == day_to_return


def test__calc_prev_day_returns_correct_day_for_days():
    today = '2023-01-24'
    day_int = int(today.split('-')[2])
    for i in range(1, day_int):
        day_to_return = f'2023-01-{day_int - i}'
        no_of_days = i
        day_returned = RetrievePreviousDays(day=today, no_of_days=no_of_days).return_n_prev_day()
        assert day_returned == day_to_return


def test_1_calc_prev_day_returns_correct_day_for_years():
    today = '2023-01-4'
    no_of_days = 4
    day_to_return = '2022-12-31'
    day_returned = RetrievePreviousDays(day=today, no_of_days=no_of_days).return_n_prev_day()
    assert day_returned == day_to_return


def test_2_calc_prev_day_returns_correct_day_for_years():
    today = '2023-01-4'
    no_of_days = 5
    day_to_return = '2022-12-30'
    day_returned = RetrievePreviousDays(day=today, no_of_days=no_of_days).return_n_prev_day()
    assert day_returned == day_to_return


def test_3_calc_prev_day_returns_correct_day_for_years():
    today = '2023-01-4'
    no_of_days = 15
    day_to_return = '2022-12-20'
    day_returned = RetrievePreviousDays(day=today, no_of_days=no_of_days).return_n_prev_day()
    assert day_returned == day_to_return


def test_1_calc_prev_day_returns_correct_day_for_months():
    today = '2023-02-4'
    no_of_days = 4
    day_to_return = '2023-01-31'
    day_returned = RetrievePreviousDays(day=today, no_of_days=no_of_days).return_n_prev_day()
    assert day_returned == day_to_return


def test_2_calc_prev_day_returns_correct_day_for_months():
    today = '2023-02-4'
    no_of_days = 5
    day_to_return = '2023-01-30'
    day_returned = RetrievePreviousDays(day=today, no_of_days=no_of_days).return_n_prev_day()
    assert day_returned == day_to_return


def test_3_calc_prev_day_returns_correct_day_for_months():
    today = '2023-02-4'
    no_of_days = 15
    day_to_return = '2023-01-20'
    day_returned = RetrievePreviousDays(day=today, no_of_days=no_of_days).return_n_prev_day()
    assert day_returned == day_to_return


def test_4_calc_prev_day_returns_correct_day_for_months():
    today = '2023-02-4'
    no_of_days = 30
    day_to_return = '2023-01-5'
    day_returned = RetrievePreviousDays(day=today, no_of_days=no_of_days).return_n_prev_day()
    assert day_returned == day_to_return


def test_1_calc_prev_day_returns_correct_day_for_31_day_months():
    today = '2023-04-4'
    no_of_days = 4
    day_to_return = '2023-03-31'
    day_returned = RetrievePreviousDays(day=today, no_of_days=no_of_days).return_n_prev_day()
    assert day_returned == day_to_return


def test_2_calc_prev_day_returns_correct_day_for_31_day_months():
    today = '2023-04-4'
    no_of_days = 5
    day_to_return = '2023-03-30'
    day_returned = RetrievePreviousDays(day=today, no_of_days=no_of_days).return_n_prev_day()
    assert day_returned == day_to_return


def test_3_calc_prev_day_returns_correct_day_for_31_day_months():
    today = '2023-04-4'
    no_of_days = 15
    day_to_return = '2023-03-20'
    day_returned = RetrievePreviousDays(day=today, no_of_days=no_of_days).return_n_prev_day()
    assert day_returned == day_to_return


def test__calc_prev_day_returns_correct_day_for_30_day_months():
    today = '2023-07-4'
    no_of_days = 4
    day_to_return = '2023-06-30'
    day_returned = RetrievePreviousDays(day=today, no_of_days=no_of_days).return_n_prev_day()
    assert day_returned == day_to_return


def test__calc_prev_day_returns_correct_day_for_28_day_months():
    today = '2023-03-4'
    no_of_days = 4
    day_to_return = '2023-02-28'
    day_returned = RetrievePreviousDays(day=today, no_of_days=no_of_days).return_n_prev_day()
    assert day_returned == day_to_return


def test_1_retrieve_no_of_previous_days():
    no_of_days = 3
    today = '2023-03-4'
    expected_result = {'day-1': '2023-03-3', 'day-2': '2023-03-2', 'day-3': '2023-03-1'}
    actual_result = RetrievePreviousDays(day=today, no_of_days=no_of_days).return_dict_for_no_of_prev_days()
    assert actual_result == expected_result


def test_2_retrieve_no_of_previous_days():
    no_of_days = 0
    today = '2023-03-4'
    expected_result = {}
    actual_result = RetrievePreviousDays(day=today, no_of_days=no_of_days).return_dict_for_no_of_prev_days()
    assert actual_result == expected_result
