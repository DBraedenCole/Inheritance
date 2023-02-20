class Person:
    def __init__(self, nm, addy, phon):
        self.__name = nm
        self.__address = addy
        self.__phone_num = phon
    
    def print_person(self):
        print(f"Name: {self.__name}\nAddress: {self.__address}\nPhone number: {self.__phone_num}")

class Customer(Person):
    def __init__(self, nm, addy, phon,cust_no,mail_tf):
        Person.__init__(nm, addy, phon)

        self.__customer_number = cust_no
        self.__mail = mail_tf

    def print_person(self):
        print(f"Name: {self.__name}\nAddress: {self.__address}\nPhone number: {self.__phone_num}\nCustomer number:{self.__customer_number}\nMailing list preference: {self.__mail}")
        
