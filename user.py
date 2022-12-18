class Products:

    def __init__(self,add,remove):
        self._add = add
        self._remove = remove
        self.view = [["s" for _ in range(remove)] for _ in range(0,add)]
        self._order_products = {}

def show_view(self):
    print("*"*10)
    for i in range(self._add):
        for j in range(self._remove):
            print(self.view[i][j],end=" ")

        print()

        print("*"*10)

        def get_price(self):
            if self._add*self._remove <= 60:
                self._price_product1 = 500
                self._price_product2 = 700
                self._price_product3 = 900
            else:
                self._price_product1 = 600
                self._price_product2 = 800
                self._price_product3 = 1000 

        def buy_product(self,add,remove):
            if self.view[add-1][remove-1]=='B':
                print("Product completd")
            if add < int(self._add/2):
                price = self._price_product1
            elif add < int(self._add/2):
                price = self._price_product2
            else:
                price = self._price_product3

            print("your product price is ", price,"\n do you want to continue order")
            display = "1:Yes\n2:No\n"
            price(display)
            user_input = input()
            if user_input=="1":
                display = "Plese enter name"
                print(display)
                name=input.split()
                user_dict = {"name": name}
                print("Order successful")
