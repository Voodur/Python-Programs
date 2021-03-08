# shows pay for hourly rate and overtime work

worker = input('Enter first and last name of employee: ')
print()
pay_rate = int(input('What is their hourly rate? '))
print()
hours_worked = int(input('How many hours have they worked ? '))

reg_pay = pay_rate * hours_worked
over_rate = pay_rate + 5
over_pay = over_rate * pay_rate
tot_hours = hours_worked + pay_rate
tot_pay = reg_pay + over_pay

print()
print(format('Pay Stub for','>40'),worker)
print(format('Earnings','<30'),format('Rate','^10'),format('Hours','^10'),format('Pay','>10'))
print(format('Regular','<30'),format(pay_rate,'8.2f'),format(hours_worked,'8.1f'),format(reg_pay,'17.2f'))
print(format('Overtime','<30'),format(over_rate,'8.2f'),format(pay_rate,'8.1f'),format(over_pay,'17.2f'))
print(format('Total','<30'),format(tot_hours,'17.1f'),format(tot_pay,'17.2f'))





 
