import PersonClass as p

name = 'Braeden'
address = '66 Daughtrey Ave'
phone = '520-909-4855'
cust_num = '1111'
on_list = True

p1 = p.Person(name,address,phone)

c1 = p.Customer(name, address, phone, cust_num, on_list)

p1.print_person()

print("\n\n")

c1.print_person()