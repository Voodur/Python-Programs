import random
ask = 'y'

print('Hello my name is Tom')
print('I can see the future and I would love to share that with you')
print()
while ask == 'y':
    question = input('What would you like to know : \n')
    print('\nYou ask me','"' + question + '". . .')
    print()


    rand_num = random.randint(1,9)

    if rand_num == 1:
        print('The anwser will reveal itself to you, in time')
        print()
    elif rand_num == 2:
        print('Your chances are not looking good')
        print()
    elif rand_num == 3:
        print('The odds are in your favor')
        print()
    elif rand_num == 4:
        print('These are dark times for you')
        print()
    elif rand_num == 5:
        print('This part of your life remains undetermined')
        print()
    elif rand_num == 6:
        print('If you follow this path it will not end well for you')
        print()
    elif rand_num == 7:
        print('You are in line to receive a great award')
        print()
    elif rand_num == 8:
        print('This is true')
        print()
    elif rand_num == 9:
        print('This is false')
        print()
    

    ask = input('\nWant to know more ?  (y/n): ')
print()
print(' Ok then . . . Goodbye')
                                             
