# -*- coding: UTF-8 -*-

# Calculaction N-th prime number from input number. Also, N is position of number in array.


def isprime(number):  # Is number prime?
    primenumber = True  # Testing variable. Let it TRUE.
    for divisor in range(2, number - 1):  # Checking divisors.
        if number % divisor == 0:  # If remainder equals 0...
            primenumber = False  # This number is composite! Testing variable is FALSE.
    return primenumber  # Returning result.


def nthprime(start, position):  # Searching N-th prime number from start number.
    count = 0  # Position counter.
    testingnumber = start  # Control number.
    while count < position:  # While position counter dont reached target position...
        testingnumber += 1  # We increment testing number by 1...
        if isprime(testingnumber):  # And if our number is prime...
            count += 1  # ...We increment position counter by 1.
    return testingnumber  # Returning our counter.

inarray = []  # Creating array for input numbers
outarray = []  # Creating array for output numbers
k = int(input('Количество чисел: '))  # Requesting quantity of numbers

for i in range(k):  # Step-by-step...
    ni = int(input('Число номер ' + str(i + 1) + ': '))  # ...inputing numbers...
    inarray.append(ni)  # ...appending it to input array...
    outarray.append(nthprime(ni, i))  # ...and calculation values for outut array.

for i in range(k):  # Step-by-step print...
    print 'Простое число №' + str(i + 1) + ' для числа ' + str(inarray[i]) + ' равно ' + str(outarray[i])  # ...result.
