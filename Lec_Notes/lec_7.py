import datetime
import math


class BankAccount:
    currency = '$'

    def __init__(self, customer, account_number, balance=0):
        self.customer = customer
        self.account_number = account_number
        self.balance = balance

    def deposit(self, amount):
        assert amount > 0, 'Can\'t deposit negative amount'
        self.balance += amount

    def withdraw(self, amount):
        assert amount <= self.balance or amount >= 0, 'Insufficient funds'
        self.balance -= amount
        return True

    def check_balance(self):
        print(f'The current balance for account number {self.account_number} is {self.balance:.2f}{self.currency}')

    @staticmethod
    def transfer_money(acc1, acc2, amount):
        if acc1.withdraw(amount):
            acc2.deposit(amount)

    @classmethod
    def f(cls, args):
        pass


class Vehicle:
    def __init__(self, number, make, model, price):
        self.number = number
        self.make = make
        self.model = model
        self.price = price

    def get_vehicle_name(self):
        return f'{self.make} {self.model}'

    def display(self):
        print(f'Licence number: {self.number}',
              f'Vehicle name: {self.get_vehicle_name()}',
              f'Price: {self.price}$',
              sep='\n')


class Point:
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y

    def get_x(self):
        return self.x

    def set_x(self, new_x):
        self.x = new_x

    def get_y(self):
        return self.y

    def set_y(self, new_y):
        self.y = new_y

    def dist_from_origin(self):
        return math.sqrt(self.x ** 2 + self.y ** 2)

    def __add__(self, other):
        return Point(self.x + other.x, self.y + other.y)

    def __sub__(self, other):
        return Point(self.x - other.x, self.y - other.y)

    def __eq__(self, other):
        return self.x == other.x and self.y == other.y

    def __gt__(self, other):
        return self.dist_from_origin() > other.dist_from_origin()

    def __ge__(self, other):
        return self.dist_from_origin() > other.dist_from_origin()

    def __lt__(self, other):
        return self.dist_from_origin() < other.dist_from_origin()

    def __le__(self, other):
        return self.dist_from_origin() <= other.dist_from_origin()

    def __iadd__(self, other):
        self.x += other.x
        self.y += other.y
        return self

    def __str__(self):
        return f'{self.x}, {self.y}'

    def __repr__(self):
        return f'Point({self.x}, {self.y})'


class Rectangle:
    def __init__(self, p1, p2):
        self.p1 = Point(p1.x, p1.y)
        self.p2 = Point(p2.x, p2.y)

    def get_width(self):
        return self.p2.x - self.p1.x

    def get_height(self):
        return self.p1.y - self.p2.y

    def get_area(self):
        return self.get_height() * self.get_width()


class Customer:
    def __init__(self, name, address, birthday):
        self.name = name
        self.address = address
        self.birthday = birthday

    def age(self):
        return round((datetime.date.today() - datetime.date.fromisoformat(self.birthday)).days / 365, ndigits=2)


class MyData:
    def __init__(self, data):
        self.data = data

    @classmethod
    def from_file(cls, filename):  # Initialize MyData from a file
        data = open(filename).readlines()
        return cls(data)

    @classmethod
    def from_dict(cls, data_dict):  # Initialize MyData from a dict item
        return cls(list(dict.items()))


class Queue:
    def __init__(self, size):
        self.queue = []
        self.size = size

    def enqueue(self, elem):
        if len(self.queue) < self.size:
            self.queue.insert(0, elem)
        return 'Size limit reached'

    def dequeue(self):
        return self.queue.pop()

    def is_empty(self):
        return len(self.queue) == 0


class Employee:
    def __init__(self, employee_id, name, salary):
        self.id = employee_id
        self.name = name
        self.salary = salary

    def print_details(self):
        print(f'Employee id: {self.id}')
        print(f'Name: {self.name}')
        print(f'Salary: {self.salary}')


class IT(Employee):
    workers = []

    def __init__(self, employee_id, name, salary, phone):
        super().__init__(employee_id, name, salary)
        self.phone = phone
        self.workers.append(self)

    def remove(self):
        self.workers.pop(self)


if __name__ == '__main__':
    b1 = BankAccount('Guy', '25140', 36241)
    b1.withdraw(50000)
    print(b1.balance)
    datetime.datetime.strptime('10/3/95', '%d/%m/%Y')
