# Input from user
n = int(input("Enter the number of terms: "))

# Initialize the first two terms
a, b = 0, 1
count = 0

# Generate the sequence
print("Fibonacci sequence:")
while count < n:
    print(a, end=" ")
    a, b = b, a + b
    count += 1
