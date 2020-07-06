class Employee:
    def __init__(self, name, id_number, department, job_title):
        self.__name = name
        self.__id_number = id_number
        self.__department= department
        self.__job_title = job_title
    def set_name(self):
        self.__name = name
    def set_id_number(self):
        self.__id_number = id_number
    def set_department(self):
        self.__department= department
    def set_job_title(self):
        self.__job_title = job_title
    def get_name(self):
        return self.__name
    def get_id_number(self):
        return self.__id_number
    def get_department(self):
        return self.__department
    def get_job_title(self):
        return self.__job_title

nume1 = input('Introduceti numele primului angajat: ')
id_number1 = input('Introduceti numarul id number al angajatului 1: ')
department1 = input('Introduceti departamentul angajatului 1: ')
job_title1 = input('Introduceti statutul primului angajat: ')
obj1 = Employee(nume1, id_number1, department1, job_title1)
nume2 = input('Introduceti numele celui de-al doilea angajat: ')
id_number2 = input('Introduceti numarul id number al angajatului 2: ')
department2 = input('Introduceti departamentul angajatului 2: ')
job_title2 = input('Introduceti statutul celui de-al doilea angajat: ')
obj2 = Employee(nume2, id_number2, department2, job_title2)
nume3 = input('Introduceti numele celui de-al treilea angajat: ')
id_number3 = input('Introduceti numarul id number al angajatului 3: ')
department3 = input('Introduceti departamentul angajatului 3: ')
job_title3 = input('Introduceti statutul celui de-al treilea angajat: ')
obj3 = Employee(nume3, id_number3, department3, job_title3)
print(obj1.get_name(), obj1.get_id_number(), obj1.get_department(), obj1.get_job_title())
print(obj2.get_name(), obj2.get_id_number(), obj2.get_department(), obj2.get_job_title())
print(obj3.get_name(), obj3.get_id_number(), obj3.get_department(), obj3.get_job_title())