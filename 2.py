def sum_positive_numbers():
    total = 0 
    while True:
        number = float(input("Enter a number (negative to quit): "))
        if number < 0:
            break
        total += number 
    print("The sum of all positive numbers is:", total)
sum_positive_numbers()