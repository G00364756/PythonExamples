# The prime factors of 13195 are 5, 7, 13 and 29.
# What is the largest prime factor of the number 600851475143 ?

n = 13195
i = 13195
j = 13195

while i > 0:
    if n % i == 0:
        print(i)
        i = i - 1    
    elif n % i != 0:
        i = i - 1
