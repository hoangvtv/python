"""
Lớp:D19CAQT01-N
MSSV:N19DCAT032
Họ và tên:Phạm Tấn Hoàng
Nhóm TH:02

Bài C.1: Viết chương trình đọc words.txt và 
chỉ in các từ có hơn n ký tự (không tính khoảng trắng). 

"""


def print_word_more_n(path, lenght: int) -> None:
    _file = open(path)
    read_file = _file.read()
    _file.close()
    for x in read_file.split():
        if len(x) > lenght:
            print(x)


lenght = int(input('Enter length of word: '))

# path: I run it on Pycharm. If you run it on Vscode ... don't work =)
print_word_more_n(r"words.txt", lenght)
