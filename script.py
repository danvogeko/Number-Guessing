import random

num = random.randint(1,10) #correct number

lives = 3

def guess(): #Allows user to guess
  global lives;

  if lives > 0:
    i = input("What is your guess? ") 
  else:
    print("You are out of lives. Game over!")

  if int(i) < num:
   print("Too low. Try a higher number!")
   lives -= 1;
   print("You have %s lives left." % lives)
   guess()

  if int(i) > num:
   print("Too high. Try a lower number!")
   lives -= 1
   print("You have %s lives left." % lives)

   
   guess()
  
  if int(i) == num:
   print("You win! The correct number was %s." %num)
   
guess() #start 
