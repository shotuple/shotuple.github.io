X = int(input())
N = int(input())
R = int()

for i in range(N):
  A, B = map(int, input().split())
  R += A*B
if X == R:
  print("Yes")
elif X != R:
  print("NO")
