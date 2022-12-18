from login_register import register,login
from admin import add_view,delete_item,modify_view


def get_prompt():
    user_or_admin = """1. Users\n2. Admin\n"""
    print(user_or_admin)
    choice = int(input())
    if choice==1:
        # User part
        display = """1.Register\n2.Login\n"""
        print(display)
        choice = int(input())
        if choice==1:
            output = register(True) 
            if output:
                print("registered successfully")
        elif choice==2:
            output = login(True)
            if output:
                display = """1.Show view\n2.Order list\n3.Order History"""
                print(display)
                user_input = int(input())
                print(user_input)
            else:
                print("login failure")




    elif choice==2:
        display = """1.Register\n2.Login\n"""
        print(display)

        choice = int(input())
        if choice==1:
            output = register(False)
            if output:
                print("registered successully")
            else:
                print("registration failure")
        elif choice==2:
            output = login(False)
            if output:
                display = """1.Add view Items\n2.Edit view items\n3.Delect view items\n4.User Details"""
                print(display)
                admin_input= int(input())  
                if admin_input==1:
                    products = input("Please enter product")
                    add_view(products)
                elif admin_input==2:
                    idx,products=input("please enter id and products").split()
                    modify_view(int(idx, products))
                elif admin_input==3:
                    idx=input("please enter enter item number")
                    delete_item(int(idx))
                elif admin_input==4:
                    get_user_detail()  
            else:
                print("Login failure")
    else:
        print("Invalid choice")

    


if __name__=="__main__":
    get_prompt()