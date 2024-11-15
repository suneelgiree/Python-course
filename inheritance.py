class Employee:
    company = "ICT"
    def show(self, name, language):
        self.name = name
        self.language = "Python"
        print(f"Employee name is {self.name}")

# class Programmer:
#      company = "ICT INFO TECH"
#      def show(self):
#         print(f"Employee name is {self.name}")

#      def showLanguages(self):
#         print(f"Programming languages known: {self.languages}")

class Programmer(Employee):
    company = "ICT INFO TECH"
    def showLanguages(self):
        print(f"Programming languages known: {self.language}")

a = Employee()
b = Programmer()

print(a.company)
print(b.company)
b.show("Suneel", "PYTHON")
b.showLanguages()