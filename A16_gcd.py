"""
Lớp:
MSSV:
Họ và tên:
Nhóm TH:

Điểm: 2

A16
Tìm ước số chung lớn nhất – GCD (Greatest common divisor)
Trong toán học, ước số chung lớn nhất (ƯSCLN) hay ước chung lớn nhất (ƯCLN) 
của hai hay nhiều số nguyên là số nguyên dương lớn nhất là ước số chung của các số 
đó. Ví dụ, ước chung lớn nhất của 6 và 15 là 3 vì 6:3=2 và 15:3=5. Hãy viết một script 
tính ước số chung lớn nhất giữa hai số a và b
Thông báo lỗi nếu giá trị nhập vào không hợp lệ
Ví dụ
C:\\>python A16_gcd.py 15 6
-----------------------------------------
GCD(15, 6): 3
-----------------------------------------

C:\\>python A16_gcd.py
-----------------------------------------
Please input number a: 15
Please input number b: 6
GCD(15, 6): 3
-----------------------------------------

"""

import sys


def gcd(x, y):
    while x*y != 0:
        if x > y:
            x %= y
        else:
            y %= x
    return x + y


program_name = sys.argv[0]
arguments = sys.argv[1:]
print(program_name)
if len(arguments) > 2:
    n1, n2 = int(sys.argv[1]), int(sys.argv[2])
    print('gcd({},{}): {}'.format(n1, n2, gcd(n1, n2)))
else:
    n1 = int(input('Please enter number a: '))
    n2 = int(input('Please enter number b: '))
    print('gcd({},{}): {}'.format(n1, n2, gcd(n1, n2)))
