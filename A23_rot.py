"""
- Lớp:D19CQAT01-N
- MSSV:N19DCAT032
- Họ và tên: Phạm Tấn Hoàng
- Nhóm TH:2


Điểm: 3

A23 
ROT13 là một dạng mã hóa yếu liên quan đến việc "xoay" từng chữ cái trong một từ 
theo 13 vị trí. Để xoay một chữ cái có nghĩa là di chuyển nó qua bảng chữ cái, quấn 
quanh đầu nếu cần thiết, do đó, 'A' được dịch bởi 3 là 'D' và 'Z' được dịch bởi 1 là 'A'.
Viết chương trình lấy một chuỗi và một số nguyên làm tham số và in ra một chuỗi 
mới có chứa các ký tự từ chuỗi ban đầu được “xoay vòng” theo số lượng đã cho.

Thông báo lỗi nếu giá trị nhập vào không hợp lệs

Ví dụ
C:\\>python A23_rot.py
Take input string: ABCDR
Take input key: 13
ROT13 of ABCDR are NOPQE

C:\\>python A23_rot.py
Take input string: ABCDR2
Take input key: 13
ROT13 of ABCDR2 are NOPQE2

C:\\>python A23_rot.py ABCDR 13
ROT13 of ABCDR are NOPQE

C:\\>python A23_rot.py ABCDR2 13
ROT13 of ABCDR2 are NOPQE2
"""

try:
    string = input("Take input String: ")
    key = int(input("Take input key: "))
    output = ""
    alphabet = {}

    for i in range(26):
        alphabet[chr(65 + i)] = chr(65 + (i + key) % 26)
        alphabet[chr(97 + i)] = chr(97 + (i + key) % 26)

    for char in string:
        if char in alphabet:
            output += alphabet[char]
        else:
            output += char
    print(output)
except:
    print('Error')
