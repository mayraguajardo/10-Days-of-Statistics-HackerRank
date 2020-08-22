size = int(input())
numbers = sorted(list(map(int,input().split())))

def get_median(size, numbers):
    if size %2 == 0:
        median = (numbers[int(size/2)-1] + numbers[int(size/2)]) / 2
    else:
        median = numbers[int(size/2)]
    return int(median)

# verifiy even or odd list
if size % 2 == 0:
    data_low = numbers[0:int(size/2)]
    data_high = numbers[int(size/2):size]
else:
    data_low = numbers[0:int(size/2)]
    data_high = numbers[int(size/2)+1:size]

print(get_median(len(data_low),data_low))
print(get_median(size,numbers))
print(get_median(len(data_high),data_high))

    

