"""
Lớp:
MSSV:
Họ và tên:
Nhóm TH:

Bài C.2: Viết chương trình đọc một tệp, 
ngắt từng dòng thành các từ, 
tách khoảng trắng và dấu câu khỏi các từ 
và chuyển chúng thành chữ thường. 
Lưu trữ chúng ở dạng văn bản "split_word.txt".
"""


def bind(_string):
    _list = list(_string.split())
    _list1 = []
    for index1 in _list:
        index1 = index1.lower()
        for index2 in range(0, len(index1)):
            if (97 <= ord(index1[index2]) <= 122) or (48 <= ord(index1[index2]) <= 57):
                pass
            else:
                index1 = index1.strip(index1[index2])
                break
        print(index1)
        _list1.append(index1)
        f = open('split_word.txt', 'a')
        f.write(index1 + '\n')
    return _list1


f = open("non_split_word.txt", "r")
_string = f.read()
print(bind(_string))
print("Done!")
