MAX,K,Q = map(int, input().split())
As = list(map(int,input().split()))
Qs = list(map(int,input().split()))
for i in range(len(Qs)):
    cur = As[Qs[i] - 1]
    if i < len(Qs) - 1:
        next = As[Qs[i + 1] - 1]
    else:
        next = MAX
    if cur + 1 == next or cur == MAX:
        continue
    else:
        As[Qs[i] - 1] = cur + 1

print(*As)
