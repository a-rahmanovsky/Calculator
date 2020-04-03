import datetime as dt
import math


class Calculator:
    def __init__(self, limit):
        self.limit = limit
        self.records = []

    def add_record(self, record):
        self.records.append(record)

    def get_today_stats(self):
        amount_today = 0
        for record in self.records:
            if record.date == dt.datetime.now().date():
                amount_today += record.amount
        return amount_today

    def __get_diff_dates(self, date1, date2):
        if date1 == date2:
            return 0
        s = str(date1 - date2)
        print(date1, date2)
        days = int(s.split()[0])
        return abs(days)

    def get_week_stats(self):
        cur_date = dt.datetime.now().date()
        amount_week = 0
        for record in self.records:
            if self.__get_diff_dates(cur_date, record.date) <= 7:
                amount_week += record.amount
        return amount_week


class CashCalculator(Calculator):
    USD_RATE = 75.0
    EURO_RATE = 85.0

    def __init__(self, limit):
        super().__init__(limit)

    def __convert_cash(self, cash, currency):
        if currency == "rub":
            return f"{float(cash)} руб"
        elif currency == "usd":
            return f"{round(cash / self.USD_RATE, 2)} USD"
        else:
            return f"{round(cash / self.EURO_RATE, 2)} Euro"

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


