# This app manipulates 3 positive integers and is calculatingc the sum of all
# positive integers between x1 and x2 that are multiple of x3 
x1 = int(input("Please type the first positive integer:"))
x2 = int(input("Please type the second positive integer:"))
x3 = int(input("Please type the multiplier you want to use:"))

if isinstance(x1, int) and x1 >= 0:
    x1_check = True
else:
    x1_check = False

if isinstance(x2, int) and x2 >= x1:
    x2_check = True
else:
    x2_check = False 

if isinstance(x3, int) and x3 > 0:
    x3_check = True
else:
    x3_check = False

if x1_check and x2_check and x3_check:
    total_sum = 0
    for number in range(x1, x2):
     if number % x3 == 0:
        total_sum += number
    print(f"{total_sum}")
else:
    print("Error, try again")


