#sequence of variables
num1,num2,num3 =100,300,500
numbers =[100,300,500]
numbers1 =[num1,num2,num3]
numbers2 =[]
things =[100,200.0,"hello world",True,[1,2,3]]
print(type(numbers2))
print(type(num1))
print(things[0])

print(things[4][2])
trouble =[20,[30,[100,20,[500]]]]
print(trouble[1][1][2][0])
trouble.append(40)
print(trouble)
trouble.pop()
print(trouble)
#tuples are read only sequencies
mytuple =(100,200,300)