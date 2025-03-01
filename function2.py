#these are called static functions which have hard coded values
def add():
    var1= 23
    var2 = 45
#return exposes the value to be accessed out of the function
    return var1 + var2

print(add())
my_num = add()
print(my_num)
print(add())

def sub():
    var1= 23
    var2 = 45
    return var2 - var1

print(sub())

def both():
    return sub() + add()

print(both())
 
def add1():
    var3= int(input("please enter your number"))
    var4= int(input("please enter another number"))
    return var3 + var4
    
def sub1():
    var3= int(input("please enter your number"))
    var4= int(input("please enter another number"))
    return var3 - var4

def both1():
    return sub1() + add1()

print(both1())


