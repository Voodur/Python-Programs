#this is post your example

total =  0
number = 1
max_num = int(input('What is the max number '))
while number < max_num:
    if number % 3 == 0 or number % 5 == 0:
        total = total + number
    number = number + 1

print(total)
