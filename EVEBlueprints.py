import os
import pandas

#if __name__ == '__main__':
#	exit()

csv_path = os.path.join(os.path.dirname(__file__), "data/industryActivityProducts.csv")

df = pandas.read_csv(csv_path)

def get_blueprint_from_product(id):
	return df.loc[df["productTypeID"] == id].values[0][0]

def get_product_from_blueprint(id):
	return df.loc[df["typeID"] == id].values[0][2]

def get_blueprint_result_quantity(id):
	return df.loc[df["typeID"] == id].values[0][3]

def get_all_blueprints():
	return df.iloc[:, 0]