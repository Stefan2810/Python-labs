import cart
from product import Product 


class Store:

    def __init__(self, stock):
        self.stock = stock
        self.customer_carts = dict() 

    def login(self, customer_id):
        self.customer_carts[customer_id] = cart.Cart()

    def add_to_cart(self, customer_id, product_name):
        """
        TODO 1:
            * adauga un produs in cart-ul unui cumparator cu id-ul dat
                - daca cumparatorul nu este logat (id-ul lui nu se gaseste
                  in lista), operatia nu se va realiza (cart-ul ramane neschimbat)
            * odata ce un produs a fost adaugat in cart, este sters din stoc
        
        Args:
            * customer_id (int):    id-ul customer-ului (fiecare
                                    customer are cate un cart)

            * product_name (str):    numele produsului ce va fi
                                     adaugat in cart    
                                        
        """ 
        for aux in self.customer_carts.keys():
            if aux == customer_id :
                for var in self.stock.view():
                    if var.name == product_name:
                        self.customer_carts[customer_id].add(var)
                        self.stock.remove(var)

    def remove_from_cart(self, customer_id, product_name):
        """
        TODO 2:
            * sterge un produs din cart-ul cumparatorului
                - daca cumparatorul nu este logat (id-ul lui nu se gaseste
                  in lista), operatia nu se va realiza (cart-ul ramane neschimbat)
            * produsul va fi adaugat iar in stocul magazinului
        
        Args:
            * customer_id (int):    id-ul customer-ului (fiecare
                                    customer are cate un cart)

            * product_name (str):    numele produslui ce va fi
                                     scos din cart
                                
        """
        for aux in self.customer_carts.keys():
            if aux == customer_id :
                for var in self.stock.view():
                    if var.name == product_name:
                        self.customer_carts[customer_id].remove(var.name)
                        self.stock.add(var)

    def view_cart(self, customer_id):
        """
        TODO 3:
            * returneaza lista produselor(nume si pret) din cart
        
        Args:
            * customer_id (int):    id-ul customer-ului (fiecare
                                    customer are cate un cart)

        Return:
            * [(str, int)]:    lista de tupluri (nume_produs, pret_produs)
                               a produselor din cart

        """
        if customer_id in self.customer_carts:
            for product in self.customer_carts[customer_id].view() :
                return ((product.name,product.price))
        return []

    def checkout(self, customer_id):
        """
        TODO 4:
            * realizeaza plata produselor
        
        Args:
            * customer_id (int):    id-ul customer-ului (fiecare
                                    customer are cate un cart)

        Returns:
            * int:pretul total al produselor din cart
        
        TIP: 
            * folositi-va de metoda cart_checkout din clasa Cart

        """
        if customer_id in self.customer_carts:
            return self.customer_carts[customer_id].cart_checkout()
        else:
            return 0 