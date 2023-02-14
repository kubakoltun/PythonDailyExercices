def count_by(x, n):
    tmp = 0
    arr = []
    for i in range(n):
        tmp += x
        arr += [tmp]
    
    return arr
