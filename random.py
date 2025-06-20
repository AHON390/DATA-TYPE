'''
import random
option = ["rock","paper","scissor"]
user_choice=input("enter your choice paper,rock,scissor: ").lower()
computer_choice = random.choice(option)
print("user_choice:",user_choice)
print("computer_choice:",computer_choice)
if user_choice == computer_choice:
    print("its a tie")
elif user_choice=="rock" and computer_choice=="scissor":
    print("rock smashes scissor")
elif user_choice=="paper" and computer_choice=="rock":
    print("paper covered the rock")
elif user_choice=="scissor" and computer_choice=="paper":
    print("scissor cut the paper")
else:
    print("you are loss")
'''

'''
import math
math.sqrt(4)
'''
'''
import random
playing = True
number=str(random.randint(11,56))
while playing:
    guess=input("guess number: ")
    if number==guess:
        print("you win!!")
        break
    else:
        print("you are loss")
'''
import math
print(math.sin(45))
print(math.cos(45))
print(math.tan(45))

print(math.ceil(45.490))
print(math.floor(45.890))
print(math.factorial(5))
