import statistics, math

maths, stats = [],[]
for i in range(5):
    m, s= map(int,input().split())
    maths.append(m)
    stats.append(s)

n = 5
mean_maths = statistics.mean(maths)
mean_stats = statistics.mean(stats)

maths_squared = sum([maths[i] ** 2 for i in range(5)])
x = sum([maths[i] * stats[i] for i in range(5)])

b = (n * x - sum(maths) * sum(stats)) / (n * maths_squared - (sum(maths)**2))

a = mean_stats - b * mean_maths

print(round(a + 80 * b,3))