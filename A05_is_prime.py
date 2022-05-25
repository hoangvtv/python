"""
- Lớp:D19CQAT01-N
- MSSV:N19DCAT032
- Họ và tên: Phạm Tấn Hoàng
- Nhóm TH:2

Điểm: 2

Bài A.5: Kiểm tra một số của phải là số nguyên tố hay không. Nếu đúng thì 
in True, nếu sai thì in False
Thông báo lỗi nếu giá trị nhập vào không hợp lệ

Ví dụ
C:\\> python A05_is_prime.py
Type number: 4
False

C:\\> python A05_is_prime.py
Type number: 5
True
"""


def check_prime(n):
    if n < 2:
        return False
    for i in range(2, n):
        if n % i == 0:
            return False
    return True


try:
    number = int(input("Type number: "))
    TF = check_prime(number)
    print(TF)

except:
    print("ERROR")
