n,m = map(int,input().split())

new_n = str(n)*n

if len(new_n) < m:
    print(new_n)

else:
    print(new_n[:m])