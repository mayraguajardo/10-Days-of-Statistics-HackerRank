import math

mean = float(input())
k = float(input())

def factorial(n):
    if n==1 or n==0:
        return 1
    elif n>1:
        return factorial(n-1)*n

def poisson_distribution(mean,k):
    temp = (mean**k) * (math.e **(-mean))/factorial(k)
    return temp

distribution = poisson_distribution(mean,k)
print(round(distribution,3))