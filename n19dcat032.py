import math
from typing import List


def convert_m_to_yd(minutes) -> List:
    l = []
    y = minutes // (365 * 24 * 60)
    l.append(y)
    minutes -= (y * 365 * 24 * 60)
    d = minutes // (24 * 60)
    l.append(d)
    return l


def fibonacci(number: int) -> list:
    _list = [0, 1]
    i = 1
    while i < number:
        i += 1
        x = _list[i - 1] + _list[i - 2]
        _list.append(x)
    return _list


def is_prime(n):
    if n < 2:
        return False
    for i in range(2, n):
        if n % i == 0:
            return False
    return True


def count_o_e_d(n):
    odd_number_count = 0
    even_number_count = 0
    while n != 0:
        temp = n % 10
        if temp % 2 == 0:
            even_number_count += 1
        else:
            odd_number_count += 1
        n //= 10

    print('The number of even numbers is {}'.format(even_number_count))
    print('The number of odd numbers is {}'.format(odd_number_count))


def is_triangle(a, b, c):
    if a + b > c or a + c > b or b + c > a:
        p = (a + b + c) / 2
        return True
    else:
        return False


def area_triangle(a, b, c):
    if a + b > c or a + c > b or b + c > a:
        p = (a + b + c) / 2
        return math.sqrt(p * (p - a) * (p - b) * (p - c))
    else:
        return 0


def factorial(x):
    if x == 0:
        return x
    else:
        fac = 1
        for i in range(1, x + 1):
            fac *= i
        return fac


def area_rectangle(width, height):
    return width * height


def gcd(a, b):
    while a * b != 0:
        if a > b:
            a %= b
        else:
            b %= a
    return a + b


def rotate(string: str, number) -> str:
    string = string.upper()
    string_output = ""
    for i in range(0, len(string)):
        if (ord(string[i]) + 13) > 90:
            string_output += chr(64 + (ord(string[i]) + number) - 90)
        else:
            string_output += chr((ord(string[i]) + number) % 90)
    return string_output
