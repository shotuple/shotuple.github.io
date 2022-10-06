# A = map(int,list(input().split()))
# A = list(map(int, input().split()))
# print(next(A))
# print(next(A))
# print(next(A))

n,x=map(int,input().split())
#a=map(int,list(input().split()))
a = list(map(int, input().split()))
for i in a:
    if i<x:
        print(i,end=" ")