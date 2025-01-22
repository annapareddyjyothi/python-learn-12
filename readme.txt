This test file and learning python course
weight=float(input("enter the weight:"))
unit = input("kilograms or pounds?(K or L):")
if unit == "K":
   weight = weight*2.205
   unit = "Lbs"
   print(f"your weight is: {weight} {unit}")
elif unit =="L":
    weight = weight/2.205
    unit = "kg"
    print(f"your weight is :{weight} {unit}")
else :
    print(f"{unit} was not valid")
