testcase = int(input())

for i in range(testcase):
    p = int(input())
    info = {}
    for k in range(p):
        info_money, info_name = input().split()
        info[int(info_money)] = info_name
    print(info[max(info.keys())])
