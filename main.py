# 1
class OnlineShop:

    shop_name = "Tech Market"

    def __init__(self, product_name, price, quantity):
        self.product_name = product_name
        self.price = price
        self.quantity = quantity

    def total_price(self):
        return self.price * self.quantity

    @classmethod
    def change_shop_name(cls, new_name):
        cls.shop_name = new_name

    @staticmethod
    def is_valid_price(price):
        return price < 0




# 2
class Student:

    passing_score = 60

    def __init__(self, name, score):
        self.name = name
        self.score = score

    def is_passed(self):
        return self.score >= Student.passing_score

    @classmethod
    def change_shop_name(cls, new_score):
        cls.passing_score = new_score

    @staticmethod
    def is_valid_price(score):
        return 0 <= score <= 100




# 3
class BankCard:

    bank_name = "AgroBank"

    def __init__(self, card_number, balance):
        self.card_number = card_number
        self.balance = balance

    def withdraw(self, amount):
        if self.balance >= amount:
            self.balance -= amount
            return self.balance
        else:
            return "Balans yetarli emas"

    @classmethod
    def change_shop_name(cls, new_name):
        cls.new_name = new_name

    @staticmethod
    def is_valid_number(number):
        return len(number) == 16
