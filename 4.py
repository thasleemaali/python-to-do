sum = 0
while True:
    num = int(input("Enter a number (0 to stop): "))
    if num == 0:
        break
    if num == 7:
        continue
    sum += num

print("Sum of numbers (except 7):", sum)