from b.table import Table
import json


class Restaurant:
    def __init__(self):
        self.seats_num = dict()  # кол-во мест - список номеров столов
        self.tables_num = dict()  # айди стола - объект стола
        self.total_bill = 0
        with open("menu.json") as json_file:
            menu = json.load(json_file)
        self.menu = menu

    def reserve(self, seats):
        if type(seats) != int:
            print("Некорректное значение на вход")
            return
        for i in self.seats_num[seats]:
            if self.tables_num[i].is_reserved is False:
                self.tables_num[i].is_reserved = True
                print("Теперь этот столик зарезервирован.")
                return
        print("Нет свободных столиков на ", seats, "человек.")

    def add_payment(self, idx, food):
        price = 0
        if type(idx) != int:
            print("Некорректное значение на вход")
            return
        if type(food) != str:
            print("Некорректное значение на вход")
            return
        if self.tables_num[idx].is_reserved is False:
            return
        for category in self.menu:
            for j in category["payload"]:
                if food == j["name"]:
                    price = j["price"]

        self.tables_num[idx].add_payment(price)
        print("Позиция добавлена в чек.")

    def payment(self, idx):
        if type(idx) != int:
            print("Некорректное значение на вход")
            return
        if self.tables_num[idx].is_reserved is False:
            return
        self.total_bill += self.tables_num[idx].bill
        self.tables_num[idx].payment()
        print("Столик оплачен. Счёт обнулён")

    def add_table(self, seats):
        if type(seats) != int:
            print("Некорректное значение на вход")
            return
        a = Table(seats)
        idx = a.id
        if seats not in self.seats_num:
            self.seats_num[seats] = [idx]
        else:
            self.seats_num[seats].append(idx)

        self.tables_num[idx] = a

    def delete_table(self, idx):
        if type(idx) != int:
            print("Некорректное значение на вход")
            return
        a = int(self.tables_num[idx].seats)
        self.seats_num[a].pop(self.seats_num[a].index(idx))
        del self.tables_num[idx]

    def info(self):
        s1 = "      Информация о деятельности ресторана "
        s2 = "Общая выручка составляет: {}".format(self.total_bill)
        print(s1)
        print(s2)
        for i in self.tables_num:
            s = "Информация по столику №{}".format(i)
            s21 = "  Столик рассчитан на {} персон".format(self.tables_num[i].seats)
            s3 = "  Занятость столика на текущий момент: {}".format(self.tables_num[i].is_reserved)
            print(s)
            print(s21)
            print(s3)
            if self.tables_num[i].is_reserved is True:
                s31 = "   В текущий момент за столиком обслуживаются {} персон".format(self.tables_num[i].persons)
                s32 = "   Текущий чек стола составляет: {} рублей".format(self.tables_num[i].bill)
                print(s31)
                print(s32)
