"""
Thông tin người dùng được nhập từ giao diện bao gồm:
Mã sinh viên N19DCAT032
Mã lớp  D19CQAT01-N
Họ và tên: Phạm Tấn Hoàng

Hãy tạo giao diện dùng Tkinter nhập thông tin từ dữ liệu phía trên và 3 nút
Lưu: Lưu trữ thông tin từ thông tin nhập vào
Làm lại: Xóa các dữ liệu hiện có trên form
Thoát: Thoát chương trình
Dữ liệu khi bấm vào nút “Lưu” sẽ được lưu trữ vào tập tin data.json
"""

from tkinter import *
from tkinter import ttk, messagebox
import json


def check(num):
    try:
        float(num)
        return True
    except ValueError:
        return False


class bang_Diem:
    def __init__(self, root):
        self.root = root
        self.root.title("B3")
        self.root.geometry("1350x700+0+0")
        self.root.config(bg="white")

        # === Frame===
        frame1 = Frame(self.root, bg="blue")
        frame1.place(x=480, y=85, width=900, height=550)

        Label(frame1, text="Academic Transcript", font=("times new roman", 20, "bold"), bg="white",
              fg="green").place(x=230, y=30)

        # --------First  n
        Label(frame1, text="First Name", font=("times new roman", 15, "bold"), bg="white", fg="gray").place(
            x=50, y=100)
        self.txt_fname = Entry(frame1, font=("times new roman", 15), bg="lightgray")
        self.txt_fname.place(x=220, y=100, width=250)

        # --------Lass n
        Label(frame1, text="Last Name", font=("times new roman", 15, "bold"), bg="white", fg="gray").place(
            x=50, y=140)
        self.txt_lname = Entry(frame1, font=("times new roman", 15), bg="lightgray")
        self.txt_lname.place(x=220, y=140, width=250)

        # --------Class
        Label(frame1, text="Class", font=("times new roman", 15, "bold"), bg="white", fg="gray").place(x=50,
                                                                                                       y=180)
        self.txt_class = Entry(frame1, font=("times new roman", 15), bg="lightgray")
        self.txt_class.place(x=220, y=180, width=250)

        # -------Gender
        Label(frame1, text="Gender", font=("times new roman", 15, "bold"), bg="white", fg="gray").place(x=50,
                                                                                                        y=220)
        self.cmb_gender = ttk.Combobox(frame1, font=("times new roman", 13), state='readonly', justify=CENTER)
        self.cmb_gender['values'] = ("Select", "Male", "Female", "Other")
        self.cmb_gender.place(x=220, y=220, width=250)
        self.cmb_gender.current(0)

        # -------History
        Label(frame1, text="History ", font=("times new roman", 15, "bold"), bg="white", fg="gray").place(
            x=50, y=260)
        self.txt_his = Entry(frame1, font=("times new roman", 15), bg="lightgray")
        self.txt_his.place(x=220, y=260, width=250)

        # -------Physical
        Label(frame1, text="Physical", font=("times new roman", 15, "bold"), bg="white", fg="gray").place(
            x=50, y=300)
        self.txt_physic = Entry(frame1, font=("times new roman", 15), bg="lightgray")
        self.txt_physic.place(x=220, y=300, width=250)

        # -------Math A1
        Label(frame1, text="Math A1", font=("times new roman", 15, "bold"), bg="white", fg="gray").place(x=50,
                                                                                                         y=340)
        self.txt_ma1 = Entry(frame1, font=("times new roman", 15), bg="lightgray")
        self.txt_ma1.place(x=220, y=340, width=250)
        # -------Math A2
        Label(frame1, text="Math A2", font=("times new roman", 15, "bold"), bg="white", fg="gray").place(x=50,
                                                                                                         y=380)
        self.txt_ma2 = Entry(frame1, font=("times new roman", 15), bg="lightgray")
        self.txt_ma2.place(x=220, y=380, width=250)

        # -------Button-----
        Button(frame1, text="SAVE", command=self.save_data, font=("times new roman", 20), bd=0,
               cursor="hand2").place(x=50, y=490)
        Button(frame1, text="RESET", command=self.clear_data, font=("times new roman", 20), bd=0,
               cursor="hand2").place(x=200, y=490)
        Button(frame1, text="EXIT", command=quit, font=("times new roman", 20), bd=0, cursor="hand2").place(
            x=350, y=490)

        # -------Read json-----

    def read_data(self):
        with open('data.json') as json_file:
            json_data = json.load(json_file)
            return json_data
        # -------Read id_ max-----

    def read_id_max(self):
        with open('data.json') as json_file:
            k = 0
            json_data = json.load(json_file)
            for item in json_data:
                k = int(item['id'])
            return k
        # -------Read MSSV-----

    def read_MSSV(self):
        with open('data.json') as json_file:
            k = ""
            json_data = json.load(json_file)
            for item in json_data:
                k = item['st_code']
            return k

        # -------Write json-----

    def write_data(self):
        data = {'first_name': self.txt_fname.get(), "last_name": self.txt_lname.get(), "id": self.read_id_max() + 1,
                "st_code": self.txt_class.get(), "gender": self.cmb_gender.get(),
                "scores": [{"name": "History", "score": float(self.txt_his.get()), "code": "HI", "id": 1},
                           {"name": "Physical", "score": float(self.txt_physic.get()), "code": "PH", "id": 2},
                           {"name": "Math A1", "score": float(self.txt_ma1.get()), "code": "M1", "id": 3},
                           {"name": "Math A2", "score": float(self.txt_ma2.get()), "code": "M2", "id": 4}]}
        list = []
        list = self.read_data()
        list.append(data)
        with open('data.json', 'w') as fs:
            json.dump(list, fs, indent=4)

            # list.append(json_string)
        # X = [json.loads(s) for s in list]
        # -------Clean-----

    def clear_data(self):
        self.txt_fname.delete(0, END)
        self.txt_lname.delete(0, END)
        self.txt_class.delete(0, END)
        self.cmb_gender.current(0)
        self.txt_his.delete(0, END)
        self.txt_physic.delete(0, END)
        self.txt_ma1.delete(0, END)
        self.txt_ma2.delete(0, END)
        # -------Save-----

    def save_data(self):

        if self.txt_fname.get() == "" or self.txt_lname.get() == "" or self.txt_class.get() == "" or self.txt_his.get() == "" or self.txt_physic.get() == "" or self.txt_ma1.get() == "" or self.cmb_gender.get() == "" or self.txt_ma2.get() == "":
            messagebox.showerror("ERROR !", "Khong duoc bo trong!", parent=self.root)
        elif self.read_MSSV() == self.txt_class.get():
            messagebox.showerror("ERROR !", "DA TON TAI SINH VIEN!", parent=self.root)
            # elif isinstance(self.txt_his.get(), (int, float))== False or isinstance(self.txt_physic.get(), (int, float))== False or isinstance(self.txt_ma1.get(), (int, float))== False or isinstance(self.txt_ma2.get(), (int, float))== False:
        elif check(self.txt_his.get()) == False or check(self.txt_physic.get()) == False or check(
                self.txt_ma1.get()) == False or check(self.txt_ma2.get()) == False:
            messagebox.showerror("ERROR !", "Nhap diem bang so!", parent=self.root)
        else:
            self.write_data()
            messagebox.showerror("SUCCESS !", "DA THEM THANH CONG!", parent=self.root)


root = Tk()
obj = bang_Diem(root)
root.mainloop()
