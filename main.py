import sys
import re

# Creating System

system = 'System'

# Making characters

user = 'Me'
ghost = 'Debonshi'

print("Hello, I am", ghost)
print("I am a ghost! A friendly ghost")


#Scene 1

# Asking Name

name = input 

while(not(name == "")):
    name = input("What is your name human?\n")
    if not re.match("^[a-z]*$", name):
        print("Only letters are allowed")
        sys.exit()
    elif len(name) == 0:
        print("Insufficient characters.")
        sys.exit()
    else:
        name.append(name)

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
  print("That's very brave of a", age + " year old. Always stay brave!\n")

else:
  sys.exit()
  print("Invalid Input")

# Asking usual questions

favfood = input ("What's your favorite food?\n")
print("Oh my favorite food is also",favfood + " and beef chops\n")

hobbies = input ("Don't mind me asking but what's your hobby?\n")
print("Interesting... My hobby is to haunt bad and rude people.\n")


# Asking if user wants to scare someone.


wish1 = input ("Do you want me to scare any of your friends,\ntell me their name and I will haunt them until they become good people! 1. Yes. 2.No\n")

if wish1 == "1":

  haunt1 = input ("Who is the first person you want me to haunt?\n")
  haunt2 = input ("Who is the second person you want me to haunt?\n")
  haunt3 = input ("Who is the third person you want me to haunt?\n")
  
  print("Okay, I will start haunting",haunt1 + ",", haunt2 + " and", haunt3 + " at midnight!\n")
  hauntlist = haunt1, haunt2, haunt3

elif wish1 == "2":
  print("Okay I won't scare anyone!")




# Scene 2

print(system + ": The next day at 9 pm.\n")

print(user + ": I wonder if",ghost + " scared", hauntlist)

print("Hello",name + ", last night I scared your friends, like a lot. Eh.. might have broken a few things, but let's not get into it here.")
