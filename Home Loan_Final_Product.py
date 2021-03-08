# home loan qualifications

anwser = input('Are you a first time home buyer? ')
print()
home_cost = int(input('What was the cost of your home? '))
print()
income = int(input('What was your combined income last year? '))
print()
prev_home = input('Have you owned a primary reidence in the last three years? ')
print()

if anwser in('y','Y','yes','YES','Yes') and home_cost < 800000 and income < 255000 and prev_home in('n','N','no','NO','No'):
    print('Based on your anwsers you are qualified for credit')
else:
    print('Based on your anwsers you are not qualified for credit')

