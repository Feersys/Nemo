class Table:
    def __init__(self, seats, persons, bill):
        self.seats = seats
        self.persons = persons
        self.bill = bill
        self.is_reserved = False

    def payment(self):
        pass

    def add_payment(self):
        add = int(input("Добавить в счёт: "))
        self.pay += add
        print("К счёту добавленна сумма: ", add)

    def reserve(self, persons):
        table = int(input("Введите номер столика: "))
        if self.is_reserved:
            print("Этот столик уже занят. ")
            return
        if persons > self.seats:
            print("Слишком много персон. ")
            return
        tables[table] = False

