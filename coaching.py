num =100
num2 =3
print(num//num2)
price =10
price =20
print(price)
patient_detail ={"name":"John Smith", "age":"20","status":"New"}
# declare the new patient as a boolean variable
is_new=True
name = input("What is your name? ")
print(name)
print("Hi"+ name)
name = input("What is your name? ")
favorite_color = input("What is your favorite color? ")
print(name + " likes " + favorite_color)
birth_year = input('birth_year:')
age = 2025-int(birth_year)
print(type(birth_year))
print(type(age))

print(age)
weight_lbs = input('weight (lbs):')
weight_kg =int(weight_lbs) *0.45
print(weight_kg)
course ="python's course for beginners"
print(course)
course ='''
Hi Tish,
Hope you  are good.
Just wanted to remind you to smile always.
Take care of yourself
'''
pay= "Please come home"
print(course)

#prints the last character of the value in pay
print(pay[-1])
#eliminates the first character of the value in pay
print(pay[1:])
print(pay[0:5])#removes the last character
print(pay[:])
lend = pay[:]
print(pay)
name ="Jennifer"
#prints the characters btn e and e at the end
print(name[1:-1])
first_name = "Jojo"
last_name ="Smith"
message = first_name + '[' + last_name +']is a coder'
msg =f"{first_name} [{last_name}] is a coder"
print(message)
print(msg)
#number of characters in a variable
print(len(first_name))
#upper for turning a string to capital letters
print(first_name.upper())
#lower for turning a string to lower letters

print(first_name.lower())
#find helps allocate the index of the string
print(first_name.find("J"))
care =" Try looking for help"
aim = care.title()
#replaces a string
print(care.replace("help","aim"))
#in as a boolean value

print("Help" in care)
print(aim)
x =10+3*2

print(x)
x =(2+3)*10-3

print(x)
x = 2.9
# round ..makes yr value an integer by rounding off
print(round(x))
x = -4.5
#gives you the exact value
print(abs(x))
import math
print(math.ceil(2.9))

print(math.floor(2.9))
is_hot =False
is_cold =True

if is_hot:
    print("It's a hot day")
    print("Stay warm")
elif is_cold:
    print("It's a cold day")
    print("Stay cool")    
else:
    print("its a lovely day")    


price = 1000000
has_goodcredit = False
if has_goodcredit:
    down_payment = 0.1 * price
else:
    down_payment = 0.2 * price     
print(f"Down payment:{down_payment}")       

