import json
def add_veiw(products):
    with open('json_files/menu.json','r+') as file_handler:
        user_details_dict = json.load(file_handler)
        print(user_details_dict)
        num_of_items = len(user_details_dict.keys())
        if products not in user_details_dict.values():
            user_details_dict[num_of_items+1]=products
            file_handler.seek(0)
            json.dump(user_details_dict,file_handler)

def modify_view(idx,products):
    with open('Amazon_Replica/json_files/view.json','r+') as file_handler:
        user_details_dict = json.load(file_handler)
        print("idx = ",idx)
        print("products ",products)
        print("keys = ",user_details_dict.keys())
        if idx in [int(key) for key in list(user_details_dict.keys())]:
            user_details_dict[str(idx)]=products
            print("view ",user_details_dict)
            file_handler.seek(0)
            json.dump(user_details_dict,file_handler)

def delete_item(idx):
    with open('Amazon_Replica/json_files/view.json','r+') as file_handler:
        user_details_dict = json.load(file_handler)
        if idx in user_details_dict.keys():
            del user_details_dict[idx]
            file_handler.seek(0)
            json.dump(user_details_dict,file_handler)

def get_user_details():

    with open('json_files/user_registration_details.json') as file_handler:
            user_dict = json.load(file_handler)
            for key in user_dict.keys():
                print(key)