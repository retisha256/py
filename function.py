
#number =int(input("the number of entries"))
#dict ={input("enter key: "): input("enter value") for _ in range(number)}
#print(dict)
#
num1 = int(input("the number of entries: "))
def enter_number():
    num2 =num1    
    capture = {input("enter key: "): input("enter value") for _ in range(num2)}
    print(capture)
enter_number()    

#    
#enter_number()  
#a value with in a function can never be accessed outside of a function
#local variables have a limit of execution (are within a specific block)
#a function is a named block
#print(capture)
  
