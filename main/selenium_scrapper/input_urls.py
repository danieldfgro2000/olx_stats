from main.model.honda.models import honda_moto_models, honda_atv_models
from main.model.kawasaki.models import kawasaki_moto_models, kawasaki_atv_models
from main.model.suzuki.models import suzuki_moto_models, suzuki_atv_models
from main.model.yamaha.models import yamaha_moto_models, yamaha_atv_models
from main.utils.MotoEnumMod import MotoAtvEnum, MotoEnum

moto_kawa_url = "https://www.olx.ro/d/auto-masini-moto-ambarcatiuni/motociclete-scutere-atv/motociclete/q-kawasaki/?currency=EUR&search%5Bprivate_business%5D=private&search%5Bfilter_float_price:from%5D=500&search%5Bfilter_float_year:from%5D=2003&search%5Bfilter_float_enginesize:from%5D=250&search%5Bfilter_enum_state%5D%5B0%5D=used"
moto_honda_url = "https://www.olx.ro/d/auto-masini-moto-ambarcatiuni/motociclete-scutere-atv/motociclete/q-honda/?currency=EUR&search%5Bprivate_business%5D=private&search%5Bfilter_float_price:from%5D=500&search%5Bfilter_float_year:from%5D=2003&search%5Bfilter_float_enginesize:from%5D=250&search%5Bfilter_enum_state%5D%5B0%5D=used"
moto_yamaha_url = "https://www.olx.ro/d/auto-masini-moto-ambarcatiuni/motociclete-scutere-atv/motociclete/q-yamaha/?currency=EUR&search%5Bprivate_business%5D=private&search%5Bfilter_float_price:from%5D=500&search%5Bfilter_float_year:from%5D=2003&search%5Bfilter_float_enginesize:from%5D=250&search%5Bfilter_enum_state%5D%5B0%5D=used"
moto_suzuki_url = "https://www.olx.ro/d/auto-masini-moto-ambarcatiuni/motociclete-scutere-atv/motociclete/q-suzuki/?currency=EUR&search%5Bprivate_business%5D=private&search%5Bfilter_float_price:from%5D=500&search%5Bfilter_float_year:from%5D=2003&search%5Bfilter_float_enginesize:from%5D=250&search%5Bfilter_enum_state%5D%5B0%5D=used"
atv_kawa_url = "https://www.olx.ro/d/auto-masini-moto-ambarcatiuni/motociclete-scutere-atv/atv/q-kawasaki/?currency=EUR&search%5Bfilter_float_price:from%5D=500&search%5Bfilter_float_year:from%5D=2000&search%5Bfilter_float_enginesize:from%5D=250"
atv_honda_url = "https://www.olx.ro/d/auto-masini-moto-ambarcatiuni/motociclete-scutere-atv/atv/q-honda/?currency=EUR&search%5Bfilter_float_price:from%5D=500&search%5Bfilter_float_year:from%5D=2000&search%5Bfilter_float_enginesize:from%5D=250"
atv_yamaha_url = "https://www.olx.ro/d/auto-masini-moto-ambarcatiuni/motociclete-scutere-atv/atv/q-yamaha/?currency=EUR&search%5Bfilter_float_price:from%5D=500&search%5Bfilter_float_year:from%5D=2000&search%5Bfilter_float_enginesize:from%5D=250"
atv_suzuki_url = "https://www.olx.ro/d/auto-masini-moto-ambarcatiuni/motociclete-scutere-atv/atv/q-suzuki/?currency=EUR&search%5Bfilter_float_price:from%5D=500&search%5Bfilter_float_year:from%5D=2000&search%5Bfilter_float_enginesize:from%5D=250"

atv_kawa_cluj_url = "https://www.olx.ro/d/auto-masini-moto-ambarcatiuni/motociclete-scutere-atv/atv/cluj-judet/q-kawasaki/?currency=EUR&search%5Bfilter_float_price:from%5D=500&search%5Bfilter_float_year:from%5D=2000&search%5Bfilter_float_enginesize:from%5D=250"

moto_url_list = [moto_kawa_url, moto_honda_url, moto_yamaha_url, moto_suzuki_url]
atv_url_list = [atv_kawa_url, atv_honda_url, atv_yamaha_url, atv_suzuki_url]

moto_models = [kawasaki_moto_models, honda_moto_models, yamaha_moto_models, suzuki_moto_models]
atv_models = [kawasaki_atv_models, honda_atv_models, yamaha_atv_models, suzuki_atv_models]


def return_url_list():
	moto_urls = []
	year = '1998'
	engine_size = '250'
	for moto_or_atv in MotoAtvEnum:
		for brand in MotoEnum:
			moto_urls.append(
				f'https://www.olx.ro/d/auto-masini-moto-ambarcatiuni/motociclete-scutere-atv/{moto_or_atv.name}/q-{brand.name}/?currency=EUR&search%5Bprivate_business%5D=private&search%5Bfilter_float_price:from%5D=500&search%5Bfilter_float_year:from%5D={year}&search%5Bfilter_float_enginesize:from%5D={engine_size}&search%5Bfilter_enum_state%5D%5B0%5D=used')
	
	return moto_urls


return_url_list()
