from lec_7 import BankAccount, Vehicle, Customer, Point

my_account = BankAccount('Guy Taggar', 137137)
his_account = BankAccount('Betanir Taggar', 13511)
me = Customer('Guy Taggar', 'Sirkin 27', '1995-03-10')
him = Customer('Nir Taggar', 'Amos Oz 3', '1998-06-14')
p1 = Point(3, 3)
p2 = Point(2, 4)

def print_account_info(account):
    print(f'Customer: {account.customer}')
    print(f'Account id: {account.account_number}')
    print(f'Balance: {account.balance}')


BankAccount.f('args')
my_account.f('Hey')

# print(me.age())
# print(him.age())

# print(p1)
# p1 += p2
print(p1)
print(repr(p1))
print(eval('Point(2, 51)'))
# print(eval(repr(p1)))
