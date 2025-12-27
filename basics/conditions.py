#conditional statements:
#if condition :
a = 10
if a > 20:
    print(" a greater than 20")
    print(f"{a} is grater than 20")
else:
    print("a is less than 20")
    
# if else in one line
# output_1 = True if a>40 else False
# print(output_1)
    
    
# gender = input("enter your gender:")
# age = int(input("enter your age:"))
# if gender == "male" and age >= 18:
#     print("you are eligible")
# else:
#     print("you are not eligible")
    
# if gender == "male" or age >= 18:
#     print("you are eligible")
# else:
#     print("you are not eligible")


# age = int(input("enter your age:"))

# if age >= 18:
#     print("you are eligible to proceed to fill the application")
#     gender = input("enter you gender")
#     city = input("enter your city:")
#     if gender == "male" and city == "hyd":
#         print("you can join the hyd club")
#     else:
#         print("sorry you can't join the club")
# else:
#     print("you are not eligible to apply the application")

# requirments: marks>80 - excellent, marks>60 - good, marks 60 to 40 - avarage marks<40 bad

marks = 89
if marks >= 80:
    print("Excellent")
elif marks >= 60:
    print("Good")
elif marks < 60 and marks >40:
    print("Avarage")
else:
    print("Bad")
    