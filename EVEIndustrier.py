print("Initializing....")

from FetchPrice import *
from EVEIndustry_v2 import get_inputs_rtn
from EVEBlueprints import *
from NamesTranslator import get_type_name

def do_get_input_info_rtn(inp):
	result = {}

	materials_ids_list = get_inputs_rtn(inp)

	grand_total = 0

	for k, v in materials_ids_list.items():
		price = get_price_buy_percentile(k)
		grand_total += price * v

	quantity = int(get_blueprint_result_quantity(int(inp)))
	cost_per = grand_total/quantity
	product = get_product_from_blueprint(int(inp))
	sell_price = get_price_sell_percentile(product)

	margin = 0
	try:
		margin = round(sell_price/cost_per, 2)
	except Exception as e:
		print(e)

	result["total_cost"] = grand_total
	result["cost_per"] = cost_per
	result["sell_price"] = sell_price
	result["margin"] = margin

	return result

def do_get_input(usr_input):
	materials_ids_list = get_inputs_rtn(usr_input)

	grand_total = 0

	for k, v in materials_ids_list.items():
		price = get_price_buy_percentile(k)
		grand_total += price * v

	print("==========BP: %s==========" %get_type_name(int(usr_input)))
	print("")
	print("Input Materials: ")

	for k, v in materials_ids_list.items():
		print("%s (%d) x%d" %(get_type_name(k), k, v))

	print("Total cost: " + str(grand_total))

	quantity = int(get_blueprint_result_quantity(int(usr_input)))

	print("Resulting amount: " + str(quantity))

	cost_per = grand_total/quantity
	print("Cost / Amount: " + str(cost_per))

	product = get_product_from_blueprint(int(usr_input))
	sell_price = get_price_sell_percentile(product)

	print("Sell price: " + str(sell_price))
	print("Margin: " + str(round(sell_price/cost_per, 2)))
	print("")
	print("====================================")

if __name__ == '__main__':
	print("Ctrl + C to quit")
	while True:
		try:
			inp = input("Enter a blueprint ID: ")
			do_get_input(inp)
		except Exception as e:
			print(e)