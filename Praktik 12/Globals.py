N = int(input('Masukan Batas Array : '))
x = [float]*N
for i in range(N):
    x[i] = float(input())

print(sum(x))

# min_ = None
# for i in x:
# if min_ is None or i < min_:
# min_ = i
# print('Smallest:', min_)
min_ = None
for i in x:
    if min_ is None or i > min_:
        min_ = i
print(int(min_))
# x.sort()
# if N % 2 == 0:
#       median1 = x[N//2]
#      median2 = x[N//2-1]
#     median = (median1 + median2)/2
# else:
#   median = x[N//2]
# print(str(median))


# index = N // 2
# if N % 2:
# return sorted(x)[index]
# return sum(sorted(x)[index-1:index+1])/2
