import math


def normal_dtb(x,mean, std):
    return 0.5 * (1 + math.erf((x - mean) / (math.sqrt(2) * std)))


mean,std = map(float, input().split())
val1=float(input())
val2=float(input())

print (round(100 - (normal_dtb(val1,mean, std)) * 100,2))
print (round(100 - (normal_dtb(val2,mean, std)) * 100,2))
print (round(normal_dtb(val2,mean, std) * 100,2))