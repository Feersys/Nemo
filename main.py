k = 0


class Restaurant:
    def __init__(self):
        self.seats_num = {}  # кол-во мест - список номеров столов
        self.tables_num = {}  # айди стола - объект стола
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

    def add_payment(self, idx, name):
        if self.tables_num[idx].is_reserved is False:
            print("За этим столиком никого нет")
        if name in self.menu:

        price = 0
        # здесь не получилось достать название и цену
        self.tables_num[idx].bill += price
        print("Позиция добавлена в чек")

    def payment(self, idx):
        Table.payment()
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
        self.seats_num[self.tables_num].pop(idx)
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
R1.payment(1)
