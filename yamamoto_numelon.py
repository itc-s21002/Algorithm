import random

num = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

ans = random.sample(num, 3)

answer = []
count = 1

while True:
    while True:
        print("ヌメロン" + str(count) + "回目の挑戦！")
        a = input("3桁の異なる数字を入力してださい>>\n")

        for i in range(3):
            answer.append(int(a[i]))

        if a[0] == a[1] == a[2]:
            print("異なる数字を入力してね\n")
            answer.clear()
        elif a[0] == a[1] or a[0] == a[2] or a[1] == a[2]:
            print("異なる数字を入力してね\n")
            answer.clear()
        else:
            break

    EAT = 0
    BITE = 0

    for i in range(3):
        if answer[i] == ans[i]:
            EAT += 1
        elif answer[i] in ans:
            BITE += 1
        else:
            pass
    print(str(answer) + " 判定:" + str(EAT) + "EAT," + str(BITE) + "BITE\n")
    answer.clear()

    if EAT == 3:
        print("お疲れ様でした！")
        break
    else:
        count += 1