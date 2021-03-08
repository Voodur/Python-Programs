numbers_list = []
number = int(input('Enter a positive integer'))

while number > 0:
    numbers_list.append(number)
    number = int(input('Enter a positive integer'))

numbers_list.sort()
print(numbers_list)

print()

print('Smallest number:', numbers_list[0])

print('Largest number: ',numbers_list[len(numbers_list)-1])
      
