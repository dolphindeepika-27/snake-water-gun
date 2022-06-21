#Snake_water_gun
import random

list1 =  ["snake", "water", "gun"]

i = 1
computer_score = 0
human_score = 0
while(i<=4):
    computer_choice = random.choice(list1)
    print("Enter Computer's choice\n", computer_choice)
    human_choice = input("Enter your choice\n")
    if computer_choice == "snake" and human_choice == "water":
            computer_score = computer_score + 1
            print("computer_score is ", computer_score)
            print("human_score is ", human_score)
    elif computer_choice == "water" and human_choice == "gun":
            computer_score = computer_score + 1
            print("computer_score is ", computer_score)
            print("human_score is ", human_score)
    elif computer_choice == "gun" and human_choice == "snake":
            computer_score = computer_score + 1
            print("computer_score is ", computer_score)
            print("human_score is ", human_score)
    elif computer_choice == human_choice:
            print("Try again")
    else:
        human_score = human_score + 1
        print("computer_score is ", computer_score)
        print("human_score is ", human_score)
    i=i+1

print ("Total_Computer_Score = ", computer_score)
print ("Total_Human_Score = ", human_score)
if computer_score > human_score:
    print("computer WON!!!!")
elif computer_score == human_score:
    print("TIE")
else:
    print("human WON!!!!")