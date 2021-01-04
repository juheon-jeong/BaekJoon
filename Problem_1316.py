num = int(input())
count = 0 #그룹단어 카운팅
for i in range(num):
    s = input()
    fault =0
    for i in range(len(s)-1):
        if s[i] != s[i+1]:
            new_s = s[i+1:]
            if new_s.count(s[i]) > 0:
                fault += 1
    if fault ==0:
        count += 1

print(count)