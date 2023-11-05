from b.rest import Restaurant

R1 = Restaurant()
R1.add_table(4)
R1.reserve(4)
print(R1.tables_num)
R1.info()
R1.add_payment(0, "lemon water")
R1.payment(0)
R1.delete_table(0)
