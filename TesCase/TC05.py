import sys

class Car:
	def __init__(self):
		self.engine = None
		self.price = 0
		self.brand = ''
		self.gas = 0
	
	def set_engine(self, engine):
		self.engine = engine
	
	def set_price(self, price):
		self.price = price
		
	def set_brand(self, brand):
		self.brand = brand
		
	def fill_gas(self, value):
		self.gas += value
		
	def start(self):
		if gas <= 0:
			raise
		else:
			print('The car is starting...')
	
	def get_sell_price(self):
		if self.brand == 'karimun':
			return 50000000
		elif self.brand == 'calya':
			return 120000000
		elif self.brand == 'ferrari':
			return 2000000000
		else:
			return 0
			
	def save_car_model(self):
		with open('car.model', 'r') as f_out:
			f_out.writelines(self.engine)
			f_out.writelines(self.price)
			f_out.writelines(self.brand)
			f_out.writelines(self.gas)
			
	def do_nothing(self):
		pass
		
	def go(self):
		km = 0
		tired = False
		while not tired and self.gas > 0:
			print(km, 'km.. vroom vroom..')
			km += 2
			self.gas -= 1
			if km >= 15:
				tired = True
				
	def repeat(self):
		for i in range(10):
			print('TBFO matkul favoritku')
			continue
				
if __name__ == '__main__':
	car = Car()
	car.do_nothing()
	for i in range(10):
		car.fill_gas(4)
		car.go()
		if i == 5:
			break
	print(car is Car)