probability = list(map(int,input().split()))
p = probability[0] / probability[1]
q = 1-p
n = int(input())

result = q ** (n-1) * p
print(round(result,3))