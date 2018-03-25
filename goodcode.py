#good code

def isPalin(n):
    """Function tests whether a number is a palindrome or not"""
    z = str(n) # creates a string from number,integer,etc.
    s = z[::-1] # this reverses the order of the string
    if z == s:
        return "True"
    else:
        return "False"

def isPalarray(x):
    """Function returns a list of palindromes"""
    palindromes = []
    while x < 100: # this loop adds palindromes to the list if it is one
        if isPalin(x) == "True": # see isPalin definition
            palindromes.append(x)
            x = x + 1
        elif isPalin(x) == "False":
            x = x + 1
    return(palindromes)

def iterate(t):
    """Function iterate i and then j"""
    myRange = []
    q = 5 # limits the range for a
    r = 5 # limit the range for b
    for b in range (100,q,1):
        for a in range(100,r,1):
            p = a*b
            myRange.append(p) # adds p to the range "myRange"
    myRange.sort() # sorts the range
    v = []
    for l in myRange: 
        if l not in v: # creates a new list that takes away all the duplicates from the original list
            v.append(l)
    return (v)

y = 1
ans = iterate(y)
print(ans)

x = 1
u = isPalarray(x)
print(u)

def Primenumbers(number):
        """This function returns the factors of any number"""
        primes = []
        factors = []
        j = 1
        while len(primes) < 20:
            for a in range(j,0,-1):
                if j % a == 0:
                    factors.append(a)
                else:
                    continue
            if len(factors) == 2:
                primes.append(j)
                factors = []
            else:
                factors = []    
            j = j + 1
        return primes

ans = Primenumbers(1)
print(ans)