numbers = list(map(float,input().split()))
p = (numbers[0] / 100)
n = int(numbers[1])

def factorial(n):
    if n==1 or n==0:
        return 1
    elif n>1:
        return factorial(n-1)*n

def binomial(x,n,p):
    f = factorial(n) / (factorial(n-x) * factorial(x))
    return (f * p**x * (1.0 - p)**(n-x))


#no more than 2 rejects 
no_more_than_2_rejects = 0
for i in range(n):
    if i < 3:
        no_more_than_2_rejects = no_more_than_2_rejects + binomial(i,n,p)
print(round(no_more_than_2_rejects,3))

#more than 2 rejects
more_than_2_rejects = 0
for i in range(n):
    if i>1:
        more_than_2_rejects = more_than_2_rejects + binomial(i,n,p)
print(round(more_than_2_rejects,3))
