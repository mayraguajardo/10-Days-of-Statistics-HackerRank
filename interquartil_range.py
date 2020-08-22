size =  int(input())
numbers = list(map(int,input().split()))
frequencies = list(map(int,input().split()))

def get_median(size, numbers):
    if size %2 == 0:
        median = (numbers[int(size/2)-1] + numbers[int(size/2)]) / 2
    else:
        median = float(numbers[int(size/2)])
    return median

data = []
for i in range(len(numbers)):
    for j in range(frequencies[i]):
        data.append(numbers[i])
data = sorted(data)


# verifiy even or odd list
size = int(len(data))
if size % 2 == 0:
    data_low = data[0:int(size/2)]
    data_high = data[int(size/2):size]
else:
    data_low = data[0:int(size/2)]
    data_high = data[int(size/2)+1:size]

low = get_median(len(data_low),data_low)
high = get_median(len(data_high),data_high)
print(high-low)