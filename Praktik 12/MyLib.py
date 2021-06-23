
def HitunganSum(x):
    print(int(sum(x)))


def RataRata(x, N):
    print(int(sum(x)) / N)


def Median(x, N):
    x.sort()
    if N % 2 == 0:
        median1 = x[N//2]
        median2 = x[N//2-1]
        median = (median1 + median2)/2
    else:
        median = x[N//2]
    print(int(median))


def Min(x):
    min_ = None
    for i in x:
        if min_ is None or i < min_:
            min_ = i
    print(int(min_))


def Max(x):
    min_ = None
    for i in x:
        if min_ is None or i > min_:
            min_ = i
    print(min_)
