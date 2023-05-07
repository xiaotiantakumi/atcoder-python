n = int(input())
s = list(map(int, input().split()))
p = 0

for i in range(n):
    sum = 0
    for j in range(i, n):
        sum += int(s[j])
        if sum > 3:
            p += 1
            break

print(p)
