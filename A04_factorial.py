"""
- Lớp:D19CQAT01-N
- MSSV:N19DCAT032
- Họ và tên: Phạm Tấn Hoàng
- Nhóm TH:2

Điểm: 1

Bài A.4: Tính giai thừa của một số không sử dụng đệ quy
Dữ liệu nhập từ bàn phím
Thông báo lỗi nếu giá trị nhập vào không hợp lệ

Ví dụ
C:\\> python factorial.py
Type number: 4
The factorial of 4 is 24
"""


def factorial(x):
    if x == 0:
        return x
    else:
        fac = 1
        for i in range(1, x + 1):
            fac *= i
        return fac


try:
    number = int(input("Type Number: "))
    gt = factorial(number)
    print('the factorial of ' + str(number) + ' is ' + str(gt))
except:
    print('ERROR')
