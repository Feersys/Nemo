k = 0


class Restaurant:
    def __init__(self):
        self.seats_num = dict()  # кол-во мест - список номеров столов
        self.tables_num = dict()  # айди стола - объект стола
        self.total_bill = 0
        self.menu = [
            {
                "name": "cheesecake",
                "price": 100
            },
            {
                "name": "coffee",
                "price": 50
            }
        ]

    def reserve(self, seats):

        for i in range(self.seats_num[seats]):
            if self.tables_num[i].is_reserved is False:
                self.tables_num[i].is_reserved = True
                print("Теперь этот столик зарезервирован.")
                continue
            else:
                print("Нет свободных столиков на ", seats, "человек.")

    def add_payment(self, idx, food):
        for i in self.menu:
            if self.menu.get["name"] == food:
                price = self.menu["price"]
        self.tables_num[idx].add_payment(price)
        print("Позиция добавлена в чек")

    def payment(self, idx):
        self.total_bill += self.tables_num[idx].bill
        self.tables_num[idx].payment()
        print("Столик оплачен. Счёт обнулён")

    def add_table(self, seats):
        a = Table(seats)
        other = {}
        idx = a.id
        if seats not in self.seats_num:
            self.seats_num[seats] = {idx}
        else:
            other[seats] = idx
            self.seats_num[seats].append(idx)

        self.tables_num[idx] = a

    def delete_table(self, idx):
        a = int(self.tables_num[idx].seats)
        self.seats_num[a].delete(idx)
        del self.tables_num[idx]


class Table:

    def __init__(self, seats):
        global k
        self.seats = seats
        self.persons = 0
        self.bill = 0
        self.is_reserved = False
        self.id = k
        k += 1

    def payment(self):
        if self.is_reserved is False:
            print("За столиком никого нет. ")
        if self.bill == 0:
            print("Нечего оплачивать")

        print("Столик оплачен и обнулён. ")
        self.persons = 0
        self.bill = 0
        self.is_reserved = False

    def add_payment(self, add):
        if self.is_reserved is False:
            print("За столиком никого нет. ")
            return
        self.bill += add
        print("К счёту добавлена сумма: ", add)

    def reserve(self, persons):
        if self.is_reserved is True:
            print("Этот столик уже занят. ")
            return
        if persons > self.seats:
            print("Слишком много персон. ")
            return
        self.persons = persons
        self.is_reserved = True
        print("Столик забронирован на ", persons, " человек.")


R1 = Restaurant()
R1.add_table(4)
print(R1.tables_num)
R1.delete_table(0)
