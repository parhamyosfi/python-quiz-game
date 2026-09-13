import os
from dotenv import load_dotenv
from question import questions



load_dotenv()
admin_password = os.getenv("quiz_admin_password")
open_admin = input("do you want to move to admin move y/n: ")
if open_admin.lower == "y" or "yes":
    entered_pasword = input("enter admin pasword")


    if entered_pasword == admin_password:
        print("hi admin")

    else:
        print("sorry but you are not admin")


name = input("what's your name? ")

print("welcome")

score = 0

for item in questions:
    answer = input(item["questions"])
    
    if answer.lower() == item["answer"]:
        print("correct")
        score += 1
    else:
        print("wrong")

print("your score is: ", score, "out of", len(questions))

if score == len(questions):
    print("excellent job, ", name,"!")
if score >= 2:
    print("good job, ", name,"!")
else:
    print("keep practing", name,".")
    
with open("results.txt", "a") as file:
    file.write(f"{name} - {score}/{len(questions)}\n")