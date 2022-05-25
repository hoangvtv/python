"""
- Lớp:D19CQAT01-N
- MSSV:N19DCAT032
- Họ và tên: Phạm Tấn Hoàng
- Nhóm TH:2


Điểm: 1

Bài A.3: Viết chương trình Python in ra dãy số Fibonacci với số n là số lượng dãy số Fibonacci mà không dùng đệ quy.
Yêu cầu:s
Dữ liệu nhập từ bàn phím
Thông báo lỗi nếu giá trị nhập vào không hợp lệ

Ví dụ
C:\\> python fibonacci.py
Type length of Fibonacci: 4
The first 5 numbers of the Fibonacci sequence are: 0 1 1 2 3
"""


def fibonacci(n: int) -> int:
    if 0 <= n <= 1:
        return n
    n_minus1, n_minus2 = 1, 0
    result = None
    for index in range(n - 1):
        result = n_minus1 + n_minus2
        n_minus2 = n_minus1
        n_minus1 = result
    return result


try:
    list = []
    number = int(input('Enter an integer number: '))
    for x in range(number):
        temp = fibonacci(x)
        list.append(temp)
    print('The first {} numbers of the Fibonacci sequence are: {}'.format(number, list))

except:
    print('ERROR')
