def get_rule_category(rule: dict) -> str:
	''' Get rule category in string. This category is also a key for its corresponding dictionary.
		Input(dict) = rule
		Output(str) = category of the rule
 
		Example:
		Input   = {'producer': 'N', 'product': ['people']}
		Output  = 'terminal'
	'''
	rule_product = rule[PRODUCT_KEY]
	if len(rule_product) == 0:
		return EPSILON_RULE_KEY
	elif len(rule_product) == 1:
		if rule_product[0].islower:
			return TERMINAL_RULE_KEY
		else:
			return UNARY_RULE_KEY
	elif len(rule_product) == 2:
		return BINARY_RULE_KEY
	else:
		return N_ARIES_RULE_KEY