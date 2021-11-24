from flask import Flask
import json
import random as rn


app = Flask(__name__)

def payment():
	VIRTUAL_ACCOUNT_LENGTH = 10

	data = request.get_json()
	print(data)
	shopping_cart_id = data[1]

	rn.seed(shopping_cart_id)

	# virtual_account = '7771674623'
	virtual_account = ''
	for _ in range(VIRTUAL_ACCOUNT_LENGTH):
		rand = rn.randint(1, 9)
		virtual_account += str(rand)

	total_price = get_shopping_cart_total(shopping_cart_id)

	payload = json.dumps({
		'VIRTUAL_ACCOUNT': virtual_account,
		'TOTAL_PRICE': total_price
	})

	return payload
app.add_url_rule('/payment', 'payment', payment)

def get_shopping_cart_total(shopping_cart_id = 3):
	total = rn.randint(5, 2000) * 1000 - rn.randint(0, 999)
	return total

if __name__ == '__main__':
	app.run()
