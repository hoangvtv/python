"""
- Lớp:D19CQAT01-N
- MSSV:N19DCAT032
- Họ và tên: Phạm Tấn Hoàng
- Nhóm TH:2

Điểm: 1

Bài A.8 Tính số lượng các số lẻ và số chẵn của một số
Cho một biến a là một số, hãy in ra số lượng các số lẻ và số lượng các số chẵn.

Thông báo lỗi nếu giá trị nhập vào không hợp lệ

Ví dụ
C:\\> python A08_odd_even.py
Type Number: 1234567
So luong so le la: 4
So luong so chan la: 3


"""

def check_odd_even(n):
    if n % 2 == 0:
        return True
    else:
        return False

try:
    number = int(input('Enter an integer number: '))
    odd_number_count = 0
    even_number_count = 0
    while number != 0:
        temp = number % 10
        if check_odd_even(temp):
            even_number_count += 1
        else:
            odd_number_count += 1
        number //= 10

    print('The number of even numbers is {}'.format(even_number_count))
    print('The number of odd numbers is {}'.format(odd_number_count))
except:
    print("ERROR")