#import dependencies
import os
import pandas

#import data
csv_path = os.path.join(os.path.dirname(__file__), "data/industryActivityMaterials.csv")

df = pandas.read_csv(csv_path)

print("Initializing....")

uids = []
def get_unique_id():
    print("Getting unique IDs...")
    for type_id in df["typeID"]:
        if type_id in uids:
            pass
        else:
            uids.append(type_id)
get_unique_id()

def map_dict(df_, input_id):
    dict = {}
    sliced_df = df_.loc[df["typeID"] == input_id, "materialTypeID":"quantity"]
    data = sliced_df["quantity"].tolist();
    for index, item in enumerate(sliced_df["materialTypeID"].tolist(), start=0):
        dict[item] = data[index]
    return dict

print("Indexing type ID to materials...")
data_dict = {}
for i, x in enumerate(uids):
    activity_materials = df.loc[df["typeID"] == x]
    materials_dict = map_dict(activity_materials, x)
    data_dict[x] = materials_dict
    if i != 0 and i % 100 == 0:
        print(str(i) + " items completed..")

print("Ctrl + C to quit")
while True:
	input_id = input("Enter blueprint ID: ")
	try:
		print(data_dict[int(input_id)])
	except KeyError as e:
		print("Type ID not found! Make sure you are entering the blueprint ID")
	except Exception as e:
		print(e)