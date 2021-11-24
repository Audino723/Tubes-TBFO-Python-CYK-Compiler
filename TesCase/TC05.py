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
	
	def asd(self, amin):
		if self.gas <= 0:
			print("Asdfad")
		else:
			print('The car is starting...')
	
	