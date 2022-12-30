from main.utils.MotoEnumMod import MotoAtvEnum, MotoEnum


def return_url_list(start_price, year, engine_size):
	moto_urls = []
	for moto_or_atv in MotoAtvEnum:
		for brand in MotoEnum:
			moto_urls.append(
				f'https://www.olx.ro/d/auto-masini-moto-ambarcatiuni/motociclete-scutere-atv/'
				f'{moto_or_atv.name}/q-{brand.name}'
				f'/?currency=EUR&search%5Bprivate_business%5D=private&search%5B'
				f'filter_float_price:from%5D={start_price}&search%5Bfilter_float_year:from%5D={year}&search%5B'
				f'filter_float_enginesize:from%5D={engine_size}&search%5Bfilter_enum_state%5D%5B0%5D=used')
	
	return moto_urls

