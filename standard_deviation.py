import math
size = int(input())
numbers = list(map(int,input().split()))

def get_mean(data):
    return sum(data) / len(data)

def standard_deviation(data, size):
    sum = 0
    for i in range(size):
        sum = sum + (data[i]-get_mean(data)) ** 2 
    return math.sqrt(sum/size)

print(round(standard_deviation(numbers,size),1))