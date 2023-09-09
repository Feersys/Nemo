class Menu:
    def __init__(self, ppt, nump, pay):
        self.ppt = ppt
        self.nump = nump
        self.pay = pay

    def payment(self):
        pass

    def add_payment(self):
        add = int(input("Добавить в счёт: "))
        self.pay += add
        print("К счёту добавленна сумма: ", add)

    def seat(self):
        table = int(input("Введите номер столика: "))
        if tables[table] == False:
            print("Этот столик уже занят. ")
            pass
        person = int(input("Введите количество персон"))
        if person > 4:
            print("Слишком много персон. Максимум - 4 на стол. ")
            pass
        tables[table] = False

