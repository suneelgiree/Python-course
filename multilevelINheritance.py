class Employee:
    company = "ICT"
    def show(self, name, language, department):
        self.name = name
        self.language = language
        self.department = department
        print(f"Employee name is {self.name}")

class Programmer(Employee):
    company = "ICT INFO TECH"
    def showLanguages(self):
        print(f"Programming languages known: {self.language}")

class Manager(Programmer):
    def showDepartment(self):
        print(f"Department is: {self.department}")
        super().showLanguages()

a = Manager()

a.show("Suneel","Python", "Software Development")

a.showLanguages()

a.showDepartment()
