class MotoModel:
	def __init__(self, title, link, brand, model, type_atv_or_moto, year, price, added_date, location, sell_date=None):
		self.title = title
		self.link = link
		self.brand = brand
		self.model = model
		self.type_atv_or_moto = type_atv_or_moto
		self.year = year
		self.price = price
		self.added_date = added_date
		self.location = location
		self.sell_date = sell_date
