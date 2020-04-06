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
        self.currency_info = {
            'rub': (1, "руб"),
            'usd': (self.USD_RATE, "USD"),
            'eur': (self.EURO_RATE, "Euro")
        }

    def __convert_cash(self, cash, currency):
        rate, name = self.currency_info[currency]
        actual_cash = round(cash / rate, 2)
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
        return "Хватит есть!"

class Record:
    def __init__(self, amount, comment='', date=dt.datetime.now().date()):
        self.amount = amount
        self.comment = comment
        self.date = date if date == dt.datetime.now().date() else dt.datetime.strptime(date, '%d.%m.%Y').date()
