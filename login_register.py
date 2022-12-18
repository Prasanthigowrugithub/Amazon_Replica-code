import json

def register(is_user):
    print("please enter username")
    username = input()
    print("please enter password")
    password = input()

    if is_user:
        file_name = 'json_files/user_registration_details.json'
    else:
        file_name = 'json_files/admin_registration_details.json'
    print("registration filename:", file_name)    

    with open(file_name,'r+') as file_handler:
        user_details_dict = json.load(file_handler)
        if user_details_dict.get(username):
            print("choose different username")
            return False
        user_details_dict[username]=password
        file_handler.seek(0)
        json.dump(user_details_dict,file_handler)
        return True


def login(is_user):
    print("please enter username")
    username = input()
    print("please enter password")
    password = input()

    if is_user:
        file_name = 'json_files/user_registration_details.json'
    else:
        file_name = 'json_files/admin_registration_details.json'

    print("login part",file_name)
    with open(file_name,'r') as file_handler:
        details_dict = json.load(file_handler)
        print(details_dict)
        file_password = details_dict.get(username)

        if file_password==password:
            return True
        else:
            return False