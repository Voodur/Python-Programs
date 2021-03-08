import random
print('** Rolls  5 dice  **')
print()
print()

rolls = []

i =0
while i < 5:
    print('Your roll is', random.randint(1,6))
    rolls.append(random.randint(1,6))
    i += 1


print(rolls)
