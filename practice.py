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