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


# <Tabs>
# <TabItem label="내 풀이">

# ```py
# N, X = map(int, input().split())
# A = list(map(int, input().split()))

# for i in range(N):
#     if A[i] < X:
#         print(A[i], end=" ")
# ```

# </TabItem>
# <TabItem label="다른 풀이">

# ```py
# n,x=map(int,input().split())
# #a=map(int,list(input().split()))
# a = list(map(int, input().split()))
# for i in a:
#     if i<x:
#         print(i,end=" ")
# ```

# </TabItem>