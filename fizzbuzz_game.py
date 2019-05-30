import time

def fizz(number):
    if number % 3 == 0:
        print('FIZZ!')

def buzz(number):
    if number % 5 == 0:
        print('BUZZ!')

def fizzbuzz(number):
    if number % 3 == 0 and number % 5 == 0:
        print('FIZZBUZZ!')

def none(number):
    if number % 3 != 0 and number % 5 != 0:
        print(number)

integer = 0
while integer <= 100:
    fizzbuzz(integer)
    fizz(integer)
    buzz(integer)
    none(integer)
    integer += 1
    time.sleep(0.5)