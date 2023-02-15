def fizzbuzz(n):
    arr = []
    for i in range(n+1):
        if (i != 0):
            if (i % 3 == 0 and i % 5 != 0):
                arr.append("Fizz")
            elif (i % 5 == 0 and i % 3 != 0):
                arr.append("Buzz")
            elif (i % 3 == 0 and i % 5 == 0):
                arr.append("FizzBuzz")
            else:
                arr.append(i)
                
                
    return arr
