import math


T = int(input())

for i in range(T):
    N,X = map(int,input().split())
    S=N*X
    print(math.ceil(S/4))