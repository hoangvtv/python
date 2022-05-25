"""
- Lớp:
- MSSV:
- Họ và tên:
- Nhóm TH:

Bài A.11
Điểm: 2

Viết script cho phép nhập độ dài 3 cạnh của một hình tam giác dùng đối số sau đó 
kiểm tra 3 cạnh đó có thể lập nên một tam giác hay không dựa vào định lý trên. Nếu 
không thỏa trả về thông tin: Độ dài của 3 cạnh không thỏa điều kiện của một tam 
giác. Nếu thỏa thì tìm diện tích của tam giác theo công thức Heron.
Thông báo lỗi nếu giá trị nhập vào không hợp lệ

Dùng Input

Ví dụ
C:\\> python A11_is_triangle_sol2.py
Edge a: 12
Edge b: 13
Edge c: 15
The area is 4
"""
import math

try:
    a = int(input("Nhap a:"))
    b = int(input("Nhap b: "))
    c = int(input("Nhap c: "))

    if a + b > c or a + c > b or b + c > a:
        p = (a + b + c) / 2
        s = math.sqrt(p * (p - a) * (p - b) * (p - c))
        print("The area is: ", s)
    else:
        print("Độ dài của 3 cạnh không thỏa điều kiện của một tam giác")
except:
    print("ERROR")
