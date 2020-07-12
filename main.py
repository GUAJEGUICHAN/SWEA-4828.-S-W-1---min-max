T = int(input())
A = []
for test_case in range(1, T + 1):
  N = int(input())
  An = list(map(int, input().split()))[:N]
  A+=[An]
for test_case in range(1, T + 1):
  print("#"+str(test_case), max(A[test_case-1])-min(A[test_case-1]))