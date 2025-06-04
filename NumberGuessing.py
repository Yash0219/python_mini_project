import random

real_no = random.randint(1,100)
while True:
   try:
     guessed_no = int(input("guess a number between 1 to 100:"))
     if guessed_no == real_no:
       print('Congratulations! you guessed the number')
       break
     elif guessed_no< real_no:
      print('too low')
     else:
      print('too high') 
   except ValueError:
      print("invalid no please enter correct number")   