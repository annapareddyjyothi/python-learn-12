word = "APPLE"

letter = input("Guess a letter in the secret word: ")

if letter in word:
   print(f"There is a {letter}")
else:
   print(f"{letter} was not found")
   #EXAMPLE 2
students = {"Spongebob", "Patrick", "Sandy"}

student = input("Enter the name of a student: ")

if student in students:
   print(f"{student} is in this class")
else:
   print(f"{student} is NOT in this class")
#EXAMPLE 3
grades = {
   "Sandy": 'A',
   "Squidward": 'B',
   "Spongebob": 'C',
   "Patrick": 'D'
}

student = input("Enter the name of a student: ")

if student in grades:
   print(f"{student}'s grade is {grades[student]}.")
else:
   print(f"{student} is not in the dictionary")
#EXAMPLE 4
email = "BroCode@gmail.com"
if "@" in email and "." in email:
    print("Valid email")
else:
    print("Invalid email")