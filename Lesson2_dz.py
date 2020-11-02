# Task 1

class Cars:

    def __init__(self, hp, torq, fuel_cons):
        self.hp = hp
        self.torq = torq
        self.fuel_cons = fuel_cons

    def acs(self, sec):
        self.sec = sec
        print(
            f'We are acselerating {self.sec}  sec with {self.torq} torque and {self.hp} hp by loosing {self.fuel_cons} per 100 km')

    def brake(self):
        print(f'We are braking now to compensate of {self.hp} horse powers ')


class Trucks(Cars):

    def __init__(self, hp, torq, fuel_cons, cargo):
        self.hp = hp
        self.torq = torq
        self.fuel_cons = fuel_cons
        self.cargo = cargo

    def acs(self, sec):
        self.sec = sec
        print(
            f'We are acselerating {self.sec} with {self.torq}  torque and {self.hp} horse powers loosing {self.fuel_cons} per 100 km , watch out you have a {self.cargo} kg on board')

    def brake(self):
        print(
            f'We are braking now to compensate of {self.hp} horse powers ,watch out you have a {self.cargo} kg on board')


class Sportcars(Cars):

    def acs(self, sec):
        self.sec = sec
        print(
            f'We are acselerating {self.sec} with {self.torq}  torque and {self.hp} horse powers loosing {self.fuel_cons} per 100 km , watch out,  your car price has 000000 in price number')

    def brake(self):
        print(
            f'We are braking now to compensate of {self.hp} horse powers ,watch out,  your car price has 000000 in price number')


truck1 = Trucks('500', '900', '50', '20 000')
truck1.brake()
truck1.acs('50')
print('-' * 35)
Sportcar1 = Sportcars('1000', '9000', '40')
Sportcar1.brake()
Sportcar1.acs('100')


# Task2 Создать класс магазина. Конструктор должен инициализировать
# значения: «Название магазина» и «Количество проданных
# товаров». Реализовать методы объекта, которые будут увеличивать
# кол-во проданных товаров, и реализовать вывод значения
# переменной класса, которая будет хранить общее количество
# товаров проданных всеми магазинами.


def tot_sales():
    print(shop.added)


class shop():
    items: int
    added = 0

    def __init__(self, name, sales):
        self.name = name
        self.sales = sales
        shop.added += sales

    def sale(self, items):
        self.items = items
        self.sales = self.items + self.sales
        shop.added += self.items
        print(self.sales)


    def tot_sales(shop):
        print(shop.added)


print('-' * 35)
shop1 = shop('First', 10)
print(shop1.sales)
shop2 = shop('Second', 4)
print(shop2.sales)
print(shop2.sale(10))
# print(shop2.sale(15))
tot_sales()