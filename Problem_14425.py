N,M = map(int,input().split())

list_N = []
list_M = []
count = 0

for i in range(N):
    n_temp = input()
    list_N.append(n_temp)

for j in range(M):
    m_temp = input()
    list_M.append(m_temp)

for element in list_M:
    if element in list_N:
        count += 1

print(count)