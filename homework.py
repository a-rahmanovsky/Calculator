import datetime as dt
import math


class Calculator:
    def __init__(self, limit):
        self.limit = limit
        self.records = []

    def add_record(self, record):
        self.records.append(record)

    def get_today_stats(self):
        return sum([record.amount for record in self.records if record.date == dt.datetime.now().date()])

    def get_week_stats(self):
        cur_date = dt.datetime.now().date()
        return sum([record.amount for record in self.records if (cur_date - record.date).days <= 7])


class CashCalculator(Calculator):
    USD_RATE = 60.0
    EURO_RATE = 70.0

    def __init__(self, limit):
        super().__init__(limit)
        self.code2data = {
            'rub': (1, "руб"),
            'usd': (self.USD_RATE, "USD"),
            'eur': (self.EURO_RATE, "Euro")
        }

    def __convert_cash(self, cash, currency):
        actual_cash = round(cash / self.code2data[currency][0], 2)
        name = self.code2data[currency][1]
        return f"{actual_cash} {name}"

    def get_today_cash_remained(self, currency):
        amount_today = self.get_today_stats()
        balance = self.__convert_cash(abs(self.limit - amount_today), currency)

        if amount_today < self.limit:
            return f"На сегодня осталось {balance}"
        elif amount_today == self.limit:
            return "Денег нет, держись"
        else:
            return f"Денег нет, держись: твой долг - {balance}"

class CaloriesCalculator(Calculator):
    def __init__(self, limit):
        super().__init__(limit)

    def get_calories_remained(self):
        balance = self.limit - self.get_today_stats()
        if balance > 0:
            return f"Сегодня можно съесть что-нибудь ещё, но с общей калорийностью не более {balance} кКал"
        else:
            return "Хватит есть!"

class Record:
    def __init__(self, amount, comment='', date=dt.datetime.now().date()):
        self.amount = amount
        self.comment = comment
        self.date = date if date == dt.datetime.now().date() else dt.datetime.strptime(date, '%d.%m.%Y').date()


calc = CashCalculator(1000)
calc.add_record(Record(amount=145, comment="кофе"))
# и к этой записи тоже дата должна добавиться автоматически
calc.add_record(Record(amount=300, comment="Серёге за обед", date="03.04.2020"))
print(calc.get_week_stats())