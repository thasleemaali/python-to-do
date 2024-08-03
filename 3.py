count = 0 
number = 3  

while count < 5:
    if number % 4 == 0:  
        number += 3 
        continue
    print(number) 
    count += 1 
    number += 3 