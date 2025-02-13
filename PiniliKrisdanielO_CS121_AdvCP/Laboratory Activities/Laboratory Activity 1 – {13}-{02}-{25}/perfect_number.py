num = int(input("Enter a number: "))
sum_divisor = 0
i = 1

for i in range (1,num):
    if num % 1 == 0:
        sum_divisor += i
if (num == sum_divisor):
    print(f"{num} is a perfect number")
else:
    print(f"{num} is not a perfect number")