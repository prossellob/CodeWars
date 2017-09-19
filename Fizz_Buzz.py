'''Return an array containing the numbers from 1 to N, where N is the parametered value. N will never be less than 1.

Replace certain values however if any of the following conditions are met:

    If the value is a multiple of 3: use the value 'Fizz' instead
    If the value is a multiple of 5: use the value 'Buzz' instead
    If the value is a multiple of 3 & 5: use the value 'FizzBuzz' instead

'''


def fizzbuzz(n):
    l = []
    i = 1
    while i <= n:
        if (i % 3 == 0) and (i % 5 == 0):
            l.append('FizzBuzz')
        elif i % 3 == 0:
            l.append('Fizz')
        elif i % 5 == 0:
            l.append('Buzz')
        else:
            l.append(i)
        i += 1
        
    return l
