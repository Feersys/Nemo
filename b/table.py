k = 0


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
            return
        if self.bill == 0:
            print("Нечего оплачивать")
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