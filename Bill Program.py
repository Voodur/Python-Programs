m1 = float(input('What was payed: '))
m2 = float(input('What is due:  '))

c = m1 - m2



adp = int(c * 100)

twenties = adp //2000
remaining = adp % 2000

tens = remaining // 1000
remaining = remaining % 1000

fives = remaining // 500
remaining = remaining % 500

ones = remaining // 100
remaining = remaining % 100

quarts = remaining // 25
remaining = remaining % 25

dimes = remaining // 10
remaining = remaining % 10

nickels = remaining // 5

pennies = remaining % 5





print(format('Money Given: ','10'),'$', format(m1,'5.2f'))
print(format('Amount Due:  ','10'),'$', format(m2,'5.2f'))
print(format('Change Due: ','10'),'$', format(c,'5.2f'))
print(format('20s','16'),twenties)
print(format('10s','16'),tens)
print(format('5s','16'), fives)
print(format('Quarters','16'),quarts)
print(format('Dimes','16'),dimes)
print(format('Nickels','16'),nickels)
print(format('Pennies','16'),pennies)





