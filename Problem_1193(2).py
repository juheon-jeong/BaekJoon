X = int(input())

k, stage = 1, 1

while True:
    if X-k < stage:
        break
    else:
        k += stage
        stage += 1

order = X-k+1             #stage의 몇번째 순서인지를 나타내줌.
left = stage-order+1

if stage%2==0:            #stage가 짝수이면
    print("{}/{}".format(order,left))
else:
    print("{}/{}".format(left,order))

