N = int(input())

i=1
room = N-1
if room == 0:
    print(1)
else:
    while room > 6 * i:
        room -= 6 * i
        i += 1
    print(i + 1)
