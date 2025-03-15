class Domestic_animals:
    def __init__(self,name,color,size,sound):
        self.name = name
        self.color = color
        self.size = size
        self.sound =sound
animal1=Domestic_animals("dog","white","big","barks")        
print(animal1.color)

#a new class
class Person:
  def __init__(self, fname, lname):
    self.firstname = fname
    self.lastname = lname

  def printname(self):
    print(self.firstname, self.lastname)

#Use the Person class to create an object, and then execute the printname method:

Person1 = Person("Tisha", "Walukagga")
Person1.printname()