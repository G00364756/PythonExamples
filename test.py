#def ask_ok(prompt, retries=4, reminder='Please try again!'):
    #while True:
        #ok = input(prompt)
        #if ok in ('y', 'ye', 'yes'):
            #return True
        #if ok in ('n', 'no', 'nop', 'nope'):
            #return False
        #retries = retries - 1
        #if retries < 0:
            #raise ValueError('invalid user response')
        #print(reminder)

#ask_ok("overwrite file?")

#-------------------------------------------------------------------------------

#s = 9
#x = str(s)
#z = x[::-1]
#print(z)

#--------------------------------------------------------------------------------

#Alps = range(1,5,1)
#Rockies = range(1,5,1)
#for a,b in zip(Alps,Rockies):
    #p = a*b
    #newRange = [p]
#print(newRange)

#----------------------------------------------------------------------------------
#def isPalin(n):
#    """Function tests whether a number is a palindrome or not"""
#    z = str(n) # creates a string from number,integer,etc.
#    s = z[::-1] # this reverses the order of the string
#    if z == s:
#        return "True"
#    else:
#        return "False"

#-----------------------------------------------------------------------------
#def isPalarray(x):
#    """Function returns a list of palindromes"""
#    palindromes = []
#    while x < 100: # this loop adds palindromes to the list if it is one
#        if isPalin(x) == "True": # see isPalin definition
#            palindromes.append(x)
#            x = x + 1
#        elif isPalin(x) == "False":
#            x = x + 1
#    return(palindromes)

#def iterate(t):
 #   """Function iterate i and then j"""
 #   myRange = []
 #   q = 1000 # limits the range for a
 #   r = 1000 # limit the range for b
 #   for b in range (899,q,1):
 #       for a in range(899,r,1):
 #           p = a*b
 #           myRange.append(p) # adds p to the range "myRange"
 #   myRange.sort() # sorts the range
 #   v = []
 #   for l in myRange: 
 #       if l not in v: # creates a new list that takes away all the duplicates from the original list
 #           v.append(l)
 #   return (v)

#y = 1
#ans = iterate(y)
#print(ans)

#x = 1
#u = isPalarray(x)
#print(u)
#------------------------------------------------------------------------------------------

#Range1 = []
#i = 3
#while i < 100:
#    i = i + 2
#    Range1.append(i)

#Range2 = []
#x = 2
#y = 1
#j = 2*(x*y)
#while j < 100:
#    Range2.append(j)
#    x = x + 1
#    y = y + 1
#    j = 2*(x*y)
#---------------------------------------------------------------------------------

#n = 20
#Alps = []
#while n != 0:
#    for b in range (1,21,1):
#        if n % b == 0:
#            print(n)
#            break
#        else:
#            n = n + 20
cubes = [0,1,2,3,4]
letters = cubes
print(letters)

hi=[]
pp=[]
def splits(name):
    if name == hi:
        return("hi")
    elif name == pp:
        return("heya!")
    else:
        pass

print(splits(pp))