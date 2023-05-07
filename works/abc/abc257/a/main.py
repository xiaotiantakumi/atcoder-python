list = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
N, X = map(int, input().split())
count = 0
for i in range(len(list)):
    c = list[i]
    for j in range(N):
        count += 1
        if(X == count):
            print(c)
            exit()