def create_phone_number(n):
    number = "("
    for i in range(len(n)):
        number += str(n[i])
        if i == 2:
            number += ") "
        if i == 5:
            number += "-"       
    return number
