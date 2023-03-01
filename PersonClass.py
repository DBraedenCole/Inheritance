class Person:
    def __init__(self, nm, addy, phon):
        self.__name = nm
        self.__address = addy
        self.__phone_num = phon

    def get_name(self):
        return self.__name

    def get_address(self):
        return self.__address

    def get_phone_number(self):
        return self.__phone_num

    def print_person(self):
        print(f"Name: {self.__name}\nAddress: {self.__address}\nPhone number: {self.__phone_num}")

class Customer(Person):
    def __init__(self, nm, addy, phon,cust_no,mail_tf):
        Person.__init__(self, nm, addy, phon)

        self.__customer_number = cust_no
        self.__mail = mail_tf

    def print_person(self):
        
        print("Method 1")
        Person.print_person(self)
        print(f"Customer number:{self.__customer_number}")
        if self.__mail:
            print(f"Mailing list preference: Yes")
        else:
            print(f"Mailing list preference: No")

        
        print("\nMethod 2")
        print(f"Name: {Person.get_name(self)}")
        print(f"Address: {Person.get_address(self)}")
        print(f"Phone: {Person.get_phone_number(self)}")
        print(f"Name: {Person.get_name(self)}")
        if self.__mail:
            print(f"Mailing list preference: Yes")
        else: 
            print(f"Mailing list preference: No")