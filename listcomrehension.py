#List comprehension = A concise way to create lists in Python
#Compact and easier to read than traditional loops
#[expression for value in iterable if condition]

doubles = [x * 2 for x in range(1, 11)]
triples = [y * 3 for y in range(1, 11)]
squares = [z * z for z in range(1, 11)]

fruits = ["apple", "orange", "banana", "coconut"]
uppercase_words = [fruit.upper() for fruit in fruits]
fruit_chars = [fruit[0] for fruit in fruits]
numbers = [1, -2, 3, -4, 5, -6, 8, -7]
positive_numbers = [x for x in numbers if x >= 0]
negative_numbers = [x for x in numbers if x < 0]
even_numbers = [x for x in numbers if x % 2 == 0]
odd_numbers = [x for x in numbers if x % 2 == 1]

grades = [85, 42, 79, 90, 56, 61, 30]
passing_grades = [grade for grade in grades if grade >= 60]