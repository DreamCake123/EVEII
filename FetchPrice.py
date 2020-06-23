import requests
import xmltodict

base_url = "https://api.evemarketer.com/ec/marketstat?typeid="

def main():
	while True:
		type_id = input("Type ID: ")
		data = get_data(base_url + type_id)
		print(data["exec_api"]["marketstat"]["type"]["sell"]["percentile"])

def get_data(url):
	response = requests.get(url)
	return xmltodict.parse(response.content)

def get_price_buy_percentile(type_id):
	type_id = str(type_id)
	data = get_data(base_url + type_id)
	return float(data["exec_api"]["marketstat"]["type"]["buy"]["percentile"])

def get_price_sell_percentile(type_id):
	type_id = str(type_id)
	data = get_data(base_url + type_id)
	return float(data["exec_api"]["marketstat"]["type"]["sell"]["percentile"])

if __name__ == '__main__':
	main()