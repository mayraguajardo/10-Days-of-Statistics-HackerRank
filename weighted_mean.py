n = int(input()) # size of arrays
x = list(map(int, input().split())) # integers of the array
w = list(map(int, input().split())) # weighted mean of x's elements

def weighted_mean(n,w,x):
    sum = 0 
    sum_w = 0
    i = 0

    while i < n:
        sum += x[i] * w[i]
        sum_w += w[i]
        i+=1
    return float(sum/sum_w)

print ("%0.1f" % weighted_mean(n,w,x)) # limited to the first decimal