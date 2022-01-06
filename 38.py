# Write a program having classes as Product, Order, Customer
# Do appropriate inheritance of the above classes
# Write appropriate methods / constructors in each classes
# Following output is expected
# Order No : SO001
# Customer : Sanjay Patel
# Customer Email : sanjay@dummy.com
# Name of the product is 'Pencil'
# Product Qty is : 15
# Unit Price is 20
# Order total is : 300

class Product:
    def __init__(self, name, price):
        self.name = name
        self.price = price


class Order(Product):
    def __init__(self, o_id, name, price, qty):
        self.o_id = o_id
        self.qty = qty
        self.total = qty * price
        super(Order, self).__init__(name, price)

class Customer(Order):
    def __init__(self, o_id, c_name, email, name, qty, price):
        super(Customer, self).__init__(o_id, name, price, qty)
        self.c_name = c_name
        self.email = email

    def print_order_details(self):
        print("Order No : ", self.o_id)
        print("Customer : ", self.c_name)
        print("Customer Email : ", self.email)
        print("Product name is '", self.name, "'")
        print("Product Qty is : ", self.qty)
        print("Unit Price is ", self.price)
        print("Order Total is : ", self.total)


customer = Customer(1, 'Sanjay Patel', 'sunjay@dumy.com', 'Pencil', 15, 20)
customer.print_order_details()
