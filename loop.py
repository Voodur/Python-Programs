# Two methods of printing a 10x10 grid of numbers 1-100

# method 1
# This uses a single loop that counts 

print("Method 1")
i = 1
while i <= 100:
    print(format(i,'3'),end='')
    if i % 10 == 0: # will be true on 10, 20, 30, etc
        print()
    i+=1


# method 2
# use nested loops
print("Method 2")
i = 0
while i < 10:
    j = 1
    while j <= 10:
        print(format(i*10 + j,'3'),end='')
        j +=1
    print()
    i+=1

        
