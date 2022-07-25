t = int(input())
while(t):
    n, m = map(int, input().split())
    a = list(map(int, input().split()))
    q = 1000000
    for i in range(m):
        x, y = map(int, input().split())
        q = min(a[x-1], min(a[y-1], q))
    if m % 2 == 0:
        print(0)
    else:
        print(q)
    t = t-14