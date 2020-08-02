class Employee():
    no_of_leaves=8

    def __init__(self,name,salary,role):
        self.name=name
        self.salary=salary
        self.role=role

    def print_details(self):
        return f"The name is {self.name} and salary is {self.salary} and role is {self.role}"


    #Class method is the method which is specially used to modify the class variable
    #it takes class as a default argument i.e cls it will automatically modify the class variable for all of the objects of the class also in actual class blueprint
    @classmethod
    def change_leaves(cls,leaves):
        cls.no_of_leaves=leaves


    @classmethod
    def from_dash(cls,string):
        params=string.split("-")

        #returns object of class employee
        return cls(params[0],params[1],params[2])


emp1=Employee("sush",100000,"SDE1")
emp2=Employee("sushant",150000,"SDE2")
print(emp1.print_details())

Employee.change_leaves(10)
#emp1.change_leaves(10) this will also produce the same results

print(f"no of leaves in first employee object={emp1.no_of_leaves}")
print(f"no of leaves in second employee object={emp2.no_of_leaves}")
print(f"no of leaves in Employee class template={Employee.no_of_leaves}")






#Class method as a alternative constructor
emp3=Employee.from_dash("ankit-220-SDE1")
print(emp3.print_details())





