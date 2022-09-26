import sys

N = int(input()) #Test case
for i in range(N):
        a,b = map(int, sys.stdin.readline().split())
        print(a+b)