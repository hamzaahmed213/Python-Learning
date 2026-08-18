# Create a parent class Employee with name and salary attributes. Add display() to print the employee's
#  details and work() as a general work method. Then create a child class Developer with an additional 
#  programming_language attribute. Override work() to print "Developer is writing code".

# Create another child class Manager that inherits from Employee and has an additional team_size
#  attribute. Override work() to print "Manager is managing the team". Create d1 = Developer(...)
#  and m1 = Manager(...), then call d1.display(), d1.work(), m1.display(), and m1.work().

class employee:
    name = "Hamza"
    salary = 1200000
    programming_language = "Python"
    team_size = 10

    def display(self):
        print(f"Employee name is:{self.name} and Salary is:{self.salary}")

    def work(self):
        print(f"{self.name} is Working")

class developer(employee):
        def work(self):
            
            print(f"{self.name} is writing code")
            
            print(f"{self.name} is wiring codes in {self.programming_language} language")

class manager(employee):
     def work(self):
          print(f"{self.name} is  a Manager and he is managing team")
          
          print(f"{self.name} is managing team size of {self.team_size}")


d1 = developer()
d1.display()
d1.work()
m1 = manager()
m1.display()
m1.work()
