#Aidan O'Connor - G00364756 - 14/02/2018
#Additional Exercise: The Guessing Game
# Dr. Ian McGloughlin created more comprehensive code in a video
# lecture where the computer randomly determines the number of i
# Below is original code and was created intuitively.

i = 2
n = int(input("Please enter an integer: "))
while n != i:
  if n != i:
    print("You guessed incorrectly, try again!")
    n = int(input("Please enter an integer: "))
else:
  print("You guessed correctly, the answer is", i)    
