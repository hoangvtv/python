"""
Lớp:D19CQAT01-N
MSSV:N19DCAT032
Họ và tên:Phạm Tấn Hoàng
Nhóm TH:02

Bài C.3: Cho một tệp văn bản tiếng Anh, hãy viết chương trình đếm: 
- Tổng số từ trong sách 
- Số lần mỗi từ được sử dụng. 
- Số lượng các từ khác nhau được sử dụng
"""

f = open("English.txt", "r")
_string = f.read()
_string = list(_string.split())
print("[=>] Total words: ", len(_string))
_list = list(set(_string))
print("[=>] Frequency of occurrence: ")
for index1 in _list:
    count = 0
    for index2 in _string:
        if index1 == index2:
            count += 1
    print("[+]", index1, "=", count)

print("[=>] Total words difference: ", len(_list))
