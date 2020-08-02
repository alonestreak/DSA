#The process of wrapping property and function within a single unit is known as encapsulation.
#Sometimes encapsulation refers to hiding of data or data Abstraction which means representing essential features hiding the background detail

class Rectangle():
    #By declaring varialbe name as __name we declare the variable as private member so we can not get access them outside of the class
    def __init__(self,length,height):
        self.__length=length
        self.__height=height
    def getArea(self):
        return self.__length*self.__height
    def set_length(self,length):
        self.__length=length
    def set_height(self,height):
        self.__height=height

    def get_length(self):
        return self.__length

    def get_height(self):
        return self.__height

    def de(self):
        print(self)

rec=Rectangle(10,10)
print(rec.getArea())
#Here we get error if try to acceess the length attribute outside of the class
#print(rec.__length)
