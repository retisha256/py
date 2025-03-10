def student_capture():
    details= {"Name": input("Please enter your name:"),
              "Age": int(input("Please enter your age: ")),
              "Gender": input("Please enter your gender: "),
              "Program": input("Please enter your program: "),
              "Year_of_study": int(input("Please enter your year of study:")),
              "Faculty": input("Please enter your faculty:"),
              "Date_of_birth":input("Please enter your date of birth(dd/mm/yyyy): "),
              "Test1_marks": int(input("Please enter test1 marks: ")),
              "Test2_marks": int(input("Please enter test2 marks: ")),
              "Final_exam_marks":int(input("Please enter final exam marks: ") )
              }
    Sum= (((details["Test1_marks"])+ (details["Final_exam_marks"]))/2)*0.4
    Final_mark = details["Final_exam_marks"]*0.6
    total = Sum + Final_mark
    print(f"Average of the two tests out of 40 is {Sum }")
    print(f"Your final exam marks are {Final_mark}")
    print(f"Your total marks are {total}")
    return details
student_capture()
#
    

