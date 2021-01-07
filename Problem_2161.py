import sys

N = int(sys.stdin.readline())

card = []
throw = []
for i in range(1 , N+1):
    card.append(str(i))

while len(card) > 1:
    th = card.pop(0)
    throw.append(th)
    change = card.pop(0)
    card.append(change)

answer = throw + card


print(" ".join(answer))