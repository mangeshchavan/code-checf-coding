T = int(input())

for i in range(T):
    A,B,X,Y = map(int,input().split())
    if(A<B):
        if(X<Y):
            print("CHEF")
        else:
            print("CHEFINA")
    elif A>B:
        if(X>Y):
            print("CHEF")
        else:
            print("CHEFINA")
    else:
        print("BOTH")
