num = int(input("Enter the number of terms: "))

a, b = 0, 1
count = 0

while count <  num:
    print(a, end=" ")
    a, b = b, a + b
    count += 1


