from question import questions


print("welcome")


score = 0

for  item in questions:
    answer = input(item["question"])
    if answer.lower() == item["answer"]:
        print("corect")
        score += 1

    else:
        print("wrong")


print("your score is: ", score)