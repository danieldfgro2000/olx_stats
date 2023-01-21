from main.data_mining.a_return_csv_data import return_a_list_with_all_csv


def test_list_of_csv_is_not_empty():
	list_of_csv = return_a_list_with_all_csv()
	assert len(list_of_csv) > 0