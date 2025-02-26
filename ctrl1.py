#code to interpret 
num =int(input("input your first number"))
num2 =int(input("input your second number"))
operator = input("choose the operator")
print(num, operator, num2)
if num > num2:
    print("Error:First number must be less than the second number.")
if num %num2 == 0:
    print(f"{num} is divisible by{num2}")
    #
if num != 0 :
        num2 +=num 
        print(num2) 