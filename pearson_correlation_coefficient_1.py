import statistics

def correlation_coefficient(n, val_x, val_y):
    mean_x = statistics.mean(val_x)
    mean_y = statistics.mean(val_y)
    std_x = statistics.pstdev(val_x)
    std_y = statistics.pstdev(val_y)
    c = 0
    for i in range(n):
        c = c + (val_x[i] - mean_x) * (val_y[i] - mean_y) 
    return c / (n * std_x * std_y)

n = int(float(input()))
data_x = list(map(float,input().split()))
data_y = list(map(float,input().split()))

print(round(correlation_coefficient(n,data_x,data_y),3))