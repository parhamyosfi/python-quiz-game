from question import qouestions


name = input("whats your name")


print("welcome")


score = 0

for  item in qouestions:
    answer = input(item["question"])
    if answer.lower() == item["answer"]:
        print("corect")
        score += 1

    else:
        print("wrong")


print("your score is: ", score, " out of ", len(qouestions))


if score == len(qouestions):
    print("exelent job", name)

if score == len(qouestions):
    print("good job", name)


if score == len(qouestions):
    print("keep trying job", name)