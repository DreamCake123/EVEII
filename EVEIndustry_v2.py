#import dependencies
import os
import pandas
from NamesTranslator import get_type_name

#import data
csv_path = os.path.join(os.path.dirname(__file__), "data/industryActivityMaterials.csv")

df = pandas.read_csv(csv_path)

uids = []
data_dict = {}

def get_unique_id():
    for type_id in df["typeID"]:
        if type_id in uids:
            pass
        else:
            uids.append(type_id)

def map_dict(df_, input_id):
    dict = {}
    sliced_df = df_.loc[df["typeID"] == input_id, "materialTypeID":"quantity"]
    data = sliced_df["quantity"].tolist();
    for index, item in enumerate(sliced_df["materialTypeID"].tolist(), start=0):
        dict[item] = data[index]
    return dict



def get_inputs_name(input_id):
    materials_data = data_dict[int(input_id)]
    print("~~~~~Input Materials~~~~~")
    for k in materials_data:
        k_name = get_type_name(k)
        print(k_name + " (%s) " %k + " x" + str(materials_data[k]))
    print("~~~~~~~~~~END~~~~~~~~~~")

def get_inputs_rtn(input_id):
    materials_data = data_dict[int(input_id)]
    return materials_data

print("Getting unique IDs...")
get_unique_id()

print("Indexing type ID to materials...")

for i, x in enumerate(uids):
    activity_materials = df.loc[df["typeID"] == x]
    materials_dict = map_dict(activity_materials, x)
    data_dict[x] = materials_dict
    if i != 0 and i % 1000 == 0:
        print(str(i) + " items completed..")

if __name__ == '__main__':
    print("Ctrl + C to quit")
    while True:
        get_inputs_name(input("Enter blueprint ID: "))