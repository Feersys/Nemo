k = 0


class Restaurant:
    def __init__(self):
        self.seats_num = {}#кол-во мест - список номеров столов
        self.tables_num = {}#айди стола - объект стола
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
        for i in range(len(self.seats_num)):
            if self.seats_num == seats:

    def add_payment(self):
        pass

    def payment(self):
        pass

    def add_table(self, seats):
        a = Table(seats)
        idx = a.id
        if seats not in self.seats_num:
            self.seats_num[seats] = {}
        self.seats_num.update(a)


    def delete_table(self):
        pass


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
            print("Нечего оплачивать. Для обнуления столика введите 'Yes' ")
            if input() == "Yes":
                self.persons = 0
                self.bill = 0
                self.is_reserved = False

            else:
                return
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


table_1 = Table(4)
table_1.reserve(3)
table_2 = Table(3)
table_1.payment()
