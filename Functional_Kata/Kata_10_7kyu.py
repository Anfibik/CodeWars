def fizzbuzz(value):
    res = []
    for i in range(1, value+1):
        if i % 3 == 0 and i % 5 == 0:
            res.append("FizzBuzz")
        elif i % 5 == 0:
            res.append("Buzz")
        elif i % 3 == 0:
            res.append("Fizz")
        else:
            res.append(i)


    return res

print(fizzbuzz(30))