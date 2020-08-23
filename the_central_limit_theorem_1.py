import math

def normal_dtb(x,mean, std):
    return 0.5 * (1 + math.erf((x - mean) / (math.sqrt(2) * std)))

max_weight = float(input())
n = float(input())
mean = float(input())
std = float(input())

new_mean = mean * n
new_std = math.sqrt(n) * std

print(round(normal_dtb(max_weight,new_mean,new_std),4))