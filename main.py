print("welcome")


score = 0

answer1 = input("what language are we using? ")
if answer1.lower() == "python":
    print("bravo")
    score += 1
answer2 = input("what command start git? ")
if answer2.lower() == "git init":
    score += 1


    
else:
    print("sory but that was wrong")




print("your score is: ", score)