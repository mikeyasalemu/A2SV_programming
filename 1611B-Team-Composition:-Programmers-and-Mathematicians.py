tests = int(input())
for i in range(tests):
  a,b = map(int, input().split())
  print(int(min(min(a,b),(a+b)/4)))
