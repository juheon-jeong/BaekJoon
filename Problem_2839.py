N = int(input())

count = 0

while True:
    if N%5 ==0:               #5로 나누어 떨어진다면
        count = count + int(N/5)
        print(count)
        break
    N -= 3
    count +=1
    if N <0:
        print(-1)
        break

