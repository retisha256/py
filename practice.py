x = lambda a: a+10
print(x(5))
#a lambda function can take any number of arguments, but can only have one expression
y= lambda a: a/20
print(y(600))
#lambda function  with multiple arguments
x = lambda a, b : a * b
print(x(5, 6))
x = lambda a, b,c : a * b/c
print(x(5, 6,2))
#power of a lambda
def myfunc(n):
  return lambda a : a * n
mytripler = myfunc(3)

print(mytripler(11))


#a list of carnames with a for loop
cars =["Volvo", "BMW","Jeep"]
for x in cars:
  print(x)
x =cars[0] 
#an  array is not in built but we can use arrays from numpy
#modifying the first item in a list
cars =["Volvo", "BMW","Jeep"] 
cars[0]="Toyota"
#getting the length of an array
x= len(cars)
print(x)
print(cars)
#adding items in array
cars.append("Honda")
print(cars)
#removing items in array
cars.pop(1)
print(cars)
#clearing items from a list
#cars.clear()
print(cars)
cars.copy()
print(cars)
#count returns the number of times that item appears in that list
cars =["Jeep","Honda","Honda","BMW"]
x=cars.count("Honda")
print(x)
#adding a list to another we use extend
fruits = ['apple', 'banana', 'cherry']

cars = ['Ford', 'BMW', 'Volvo']

fruits.extend(cars)
print(fruits)
#finding position of items in a list we use index
fruits = ['apple', 'banana', 'cherry']

x = fruits.index("cherry")
print(x)
#inserting items in a list
fruits = ['apple', 'banana', 'cherry']

fruits.insert(1, "orange")
print(fruits)
#reverse- reverses the items in a list
fruits = ['apple', 'banana', 'cherry']

fruits.reverse()
print(fruits)
#sort arranges items in a list
cars = ['Ford', 'BMW', 'Volvo']

cars.sort()
print(cars)
#arranging items in descending order 
cars = ['Ford', 'BMW', 'Volvo']

cars.sort(reverse=True)
print(cars)
#sorting a list by its length
def myFunc(y):
  return len(y)

cars = ['Ford', 'Mitsubishi', 'BMW', 'VW']

cars.sort(key=myFunc)

print(cars)
# A function that returns the 'year' value:
def myFunc(e):
  return e['year']

cars = [
  {'car': 'Ford', 'year': 2005},
  {'car': 'Mitsubishi', 'year': 2000},
  {'car': 'BMW', 'year': 2019},
  {'car': 'VW', 'year': 2011}
]

cars.sort(key=myFunc)
print(cars)
# A function that returns the length of the value:
def myFunc(e):
  return len(e)

cars = ['Ford', 'Mitsubishi', 'BMW', 'VW']

cars.sort(reverse=True, key=myFunc)
print(cars)
# A function that returns the length of the value:
def myFunc(e):
  return len(e)

cars = ['Ford', 'Mitsubishi', 'BMW', 'VW']

cars.sort(key=myFunc)
print(cars)
#creating a class
class myClass:
 var = 2
#creating an object
var2 =myClass
print(var2.var) 
#creating class person with method name and age
class Person:
  def __init__(self, name, age):
    self.name = name
    self.age = age

person1 = Person("John", 36)

print(person1.name)
print(person1.age)
class Person:
  def __init__(self, name, age):
    self.name = name
    self.age = age
#The self parameter is a reference to the current instance of the class, and is used to access variables that belong to the class.
  def myfunc(self):
    print("Hello my name is " + self.name)

person1 = Person("John", 36)
person1.age = 40
person1.myfunc()
print(person1.age)
#in instances where u have an empty class with no content u can use pass
class myown:
  pass
