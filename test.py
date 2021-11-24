<<<<<<< HEAD
bobi = []
a = bobi['caci']
=======
from flask import Flask
import json
import random as rn


app = Flask(__name__)


def payment():
	VIRTUAL_ACCOUNT_LENGTH = 10

	data = request.get_json()
	print(data)
	shopping_cart_id = data[3]

	rn.seed(shopping_cart_id)

	# virtual_account = '7771674623'
	virtual_account = ''
>>>>>>> 02a2cf99c9c0590b1685c35192e0f88604eebe47
