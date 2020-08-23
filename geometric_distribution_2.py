probability = list(map(int,input().split()))
p = probability[0] / probability[1]
q = 1-p
n = int(input())

result = 0
for i in range(n + 1):
    if i > 0:
        result = result + (q ** (i - 1) * p)

print(round(result,3))