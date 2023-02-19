def approx_equals(a, b):
    rz = abs(a - b)
    a = round(a, 3)
    b = round(b, 3)
    nrz = round(rz, 5)
    if (nrz > 0.001):
        return False
    else:
        return True 
