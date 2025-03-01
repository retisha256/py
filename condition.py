has_good_credit = False
has_high_income = False

if has_good_credit and has_high_income:
    print("Eligible for loan")
else:
    print("Not eligible for loan")
has_good_credit = True
has_high_income = False

if has_good_credit or has_high_income:
    print("Eligible for loan")
else:
    print("Not eligible for loan")

has_good_credit = True
has_criminal_record = False

if has_good_credit and not has_criminal_record:
    print("Eligible for loan")
else:
    print("Not eligible for loan")

temperature = 40
if temperature > 30:
    print("It's too hot!")
else:
        print("Lets chill outside!")

name =input("your name")
len == 50
if len(name)< 10:
     print("Name is too short!")
elif len(name) >50:
     print("Name is too long!")


