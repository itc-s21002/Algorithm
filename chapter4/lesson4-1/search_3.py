data = [
    ["佐藤", "000-0000-0000"],
    ["鈴木", "111-1111-1111"],
    ["高橋", "222-2222-2222"],
    ["田中", "333-3333-3333"],
    [None]
]
while True:
    s = input("検索する相手の苗字は？ ")
    i = 0
    while data[i][0]!= None and data[i][0] != s:
        i += 1
    if data[i][0] == None:
        print("その名は登録されていません")
        a = input("電話番号を入れてください")
        data.pop(-1)
        data.append([s, a])
        data.append([None])


    else:
        print(data[i][0]+"さんの番号は "+data[i][1]+"です")