<<<<<<< HEAD
import sys
from termcolor import colored
from colorama import init, Fore, Back, Style
# Creating System

print(Fore.BLUE)
print(Style.BRIGHT)

system = 'System'

# Making characters

user = 'Me'
ghost = 'Debonshi'

print("Hello, I am", ghost)
print("I am a ghost! A friendly ghost")


#Scene 1

# Asking Name

name = input("What's your name human?\n")
if name.isalpha() is False:
 print("Only letters are allowed!")
 sys.exit()
else:
 print("Nice name "+name)

# Asking age

try:
  age = int(input ("What's your age?\n"))
  print("Young Indeed", name)
except ValueError:
    print("Please enter a number.")
    sys.exit()
# Asking if user is scared of the ghost

question1 = input ("Are you scared of me? I am very scary: 1. I am scared. 2. No I am very brave\n")

if question1 == "1":
  print("Don't worry, I am a friendly ghost! I won't haunt you",name + ".\n")

elif question1 == "2":
  print("That's very brave of you",name + " year old. Always stay brave!\n")

else:
  sys.exit()
  print("Invalid Input")

# Asking usual questions

favfood = input("What's your favorite food?\n")
if favfood.isalpha() is False:
 print("Only letters are allowed!")
 sys.exit()
else:
 print("My favorite food is also", favfood + " and beef chops.")


hobby = input("What's your hobby?\n")
if name.isalpha() is False:
 print("Only letters are allowed!")
 sys.exit()
else:
 print("Interesting... my hobby is to haunt bad people.")



# Asking if user wants to scare someone.


wish1 = input ("Do you want me to scare any of your friends,\ntell me their name and I will haunt them until they become good people!")


haunt1 = input ("Who is the first person you want me to haunt?\n")
haunt2 = input ("Who is the second person you want me to haunt?\n")
haunt3 = input ("Who is the third person you want me to haunt?\n")
  
print("Okay, I will start haunting",haunt1 + ",", haunt2 + " and", haunt3 + " at midnight!\n")





# Scene 2
=======
>>>>>>> origin/main

print(system + ": The next day at 9 am.\n")

print(user + ": I wonder if",ghost + " scared them")

print(ghost + ": Hello",name + ", last night I scared your friends, like a lot. Eh.. might have broken a few things, but let's not get into it here.")

print(system + ": Ghost disappears")
print(system + ": ", haunt1, haunt2, haunt3 + " appear.")