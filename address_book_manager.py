from collections import UserDict

class Field:
    def __init__(self, value):
        self.value = value

    def __str__(self):
        return str(self.value)

class Name(Field):
    pass

class Phone(Field):
    def __init__(self, value):
        super().__init__(value)
    
    def validation(self):

        if len(self.value()) == 10:

            pass
        
        else: 
            
            raise Exception("Phone number shall be 10 digits long")



class Record:
    def __init__(self, name):
        self.name = Name(name)
        self.phones = []

    def add_phone(self, phone):

        return self.phones.append(phone)
    
    def remove_phone(self, phone):
        return self.phones.remove(phone)
    
    def update_phone(self, phone, new_phone):
        self.phones[self.phones.index(phone)] = new_phone
        
    
    #def update_phone(self, phone, new_phone):
    #    return self.phones.insert(self.phones.index(phone), new_phone)
    
    def show_phone(self):
        
        return f"{'; '.join(p.value for p in self.phones)}"
    
    def __str__(self):
        return f"Contact name: {self.name.value}, phones: {'; '.join(p.value for p in self.phones)}"

class AddressBook(UserDict):

    def add_record(self, record):

        self.data.update({record.name : record.phones})



        


    # реалізація класу




record_1 = Record('Roma')

  #  print(record_1)

phone = Phone('1234567890')

phone_1 = Phone('123')

record_1.add_phone(phone)

print(record_1)

record_1.add_phone(phone_1)

print(record_1)

  #  record_1.remove_phone(phone_1)

print(record_1.show_phone())

  #  print(record_1)

phone_2 = Phone('567')

record_1.update_phone(phone_1, phone_2)

print(record_1)
    

book = AddressBook()

book.add_record(record_1)

print(book)

print(record_1.name)

for name, record in book.data.items():
    print(str(name) + ' - ' + '; '.join(p.value for p in record))






'''
     # Створення нової адресної книги
    book = AddressBook()

    # Створення запису для John
    john_record = Record("John")
    john_record.add_phone("1234567890")
    john_record.add_phone("5555555555")

    # Додавання запису John до адресної книги
    book.add_record(john_record)

    # Створення та додавання нового запису для Jane
    jane_record = Record("Jane")
    jane_record.add_phone("9876543210")
    book.add_record(jane_record)

    # Виведення всіх записів у книзі
    for name, record in book.data.items():
        print(record)

    # Знаходження та редагування телефону для John
    john = book.find("John")
    john.edit_phone("1234567890", "1112223333")

    print(john)  # Виведення: Contact name: John, phones: 1112223333; 5555555555

    # Пошук конкретного телефону у записі John
    found_phone = john.find_phone("5555555555")
    print(f"{john.name}: {found_phone}")  # Виведення: 5555555555

    # Видалення запису Jane
    book.delete("Jane") '''