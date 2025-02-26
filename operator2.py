#comparison operators compare two values of a boolean data structure
var = 100
var2 = 10

#greater than operator (var > var2) checks if var is greater than var2  (var2 < var)  checks if var2 is less than var  (var2 <= var)  checks if var2 is less than or equal to var  (var2 >= var)  checks if var2 is greater than or equal to var
print (var>var2)

#less than operator  (var2 > var)  checks if var2 is greater than var
print(var<var2)
#greater than or equal operator
print(var>=var2)
# less or equal operators
print(var<=var2)
#not equal we use != symbols
print (var !=var2) 

# equality operator == checks if two values are equal
print(var==var2)
#Logical Operators 
#and (for and is &,1,||) , or, not(!)
log =5
log2=6
print((log > log2) & (log2 < log))

print(not (log2 < log))
print((log > log2) or (log2 < log))
numbers ={20,30} 
print(20 in numbers)
print(30 in numbers)
print(20 not in numbers) 
name ="Tisha"
print("T"not in name)
print(20 is not numbers)
print(20 is 20)