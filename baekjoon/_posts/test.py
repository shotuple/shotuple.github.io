# S = input()
# A = []
# cnt = 0

# for i in S:
#     A.append((ord(i)-63))
#     print(A)
#     for j in A:
#         cnt += j
    
# #print(cnt)

S = input()
dial = ["ABC", "DEF", "GHI", "JKL", "MNO", "PQRS", "TUV", "WXYZ"]
cnt = 0
for i in range(len(S)):
    for j in dial:
        if S[i] in j:
            cnt += dial.index(j)+3
print(cnt)
