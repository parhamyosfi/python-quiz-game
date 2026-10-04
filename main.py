import os
from dotenv import load_dotenv
from question import questions


load_dotenv()
admin_password = os.getenv("QUIZ_ADMIN_PASSWORD")

open_admin = input("do you want to open admin mode? yes/no: ")

if open_admin == "yes":
    entered_password = input("enter admin password: ")
    
    if entered_password == admin_password:
        print("admin! hi...")
    else:
        print("wrong password")

name = input("what's your name? ")

print("welcome")

score = 0

for item in questions:
    answer = input(item["question"])
    
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