import sys
C = int(sys.stdin.readline())

for _ in range(C):
    A = list(map(int, sys.stdin.readline().split()))
    cnt = 0

    for i in range(1, len(A)):
        if A[i] > sum(A[1:])/A[0]:
            cnt += 1
    
    rate = (cnt/A[0]*100)
    #print('%.3f%%'%rate) 
    print('%.3f' % rate + '%')