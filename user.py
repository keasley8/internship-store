## User
## Attributes: name, email
## Methods: _init_, login, logout

class User:
    def _init_(self, name, email):
        self.name = name
        self.email = email
        self.logged_int = False

    def login(self):
        self.logged_in = True
        print(f"{self.email} has logged in.")

    def logout(self):
        self.logged_in = False
        print(f"{self.email} has logged out.")


## Subclass: Cashier
## Attributes: till_id
## Methods: make_order, process_payment
class Cashier(User):

    def __init__(self, name, email, till_id):
        super().__init__(name, email)
        self.till_id = till_id

    def make_order(self):
        print(f"{self.email} is making an order.")

    def process_payment(self):
        print(f"{self.email} is processing a payment.")

## Subclass: Customer
## Attributes: shopping_cart
## Methods: order and complain

class Customer(User):
    def _init_(self, name, email, shopping_cart):
        super()._init_(name, email)
        self.shopping_cart = shopping_cart

    def order(self):
        print(f"{self.email} is ordering.")

    def complain(self):
        print(f"{self.email} is complaining")




## Test 1
## name = Timmy email = tim@internship.com
user_1 = User("Timmy", "tim@internship.com")
print(user_1._dict_)

## Test 2: Create a customer named: Jimmy, jimmy@coolperson.com; eggs and bacon
customer_1 = Customer("Jimmy", "jimmy@coolperson.com", ["eggs", "bacon"])
print(customer_1._dict_)


## Test 3: Create a cashier named: Jasmine, jasmine@internship.com, till_id 772
cashier_1 = Cashier("Jasmine", "jasmine@internship.com", 772)
print(cashier_1._dict_)

## Hello Dee Cohort 1
