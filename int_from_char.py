def get_age(age):
    yearsOld = 0
    for i in range(len(age)):
        if i == 0:
            yearsOld = age[i]
    return int(yearsOld)
