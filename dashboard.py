from tkinter import*
from PIL import Image, ImageTk  # Pillow Libaray to use images in python code
from course import CourseDetails  # TO export other python file
from student import StudentDetails
from result import ResultDetails
from qr import Qr_Generater
from report import ReportDetails
import sqlite3
from tkinter import ttk, messagebox
import sys


class RMS:

    def __init__(self, root):
        self.__root = root
        # To give a title of window
        self.__root.title("Student Management System")
        # geometry For give a width and Height
        self.__root.geometry("1300x800+0+0")
        self.__root.config(bg="white")

# ============================ Icons ============================ #

        self.__logo = ImageTk.PhotoImage(file="Images/content.jpg")

# ============================ Title ============================ #

        self.__title = Label(self.__root, text="Student Result", font=(
            "goudy old style", 20, "bold"), bg="#033054", fg="white").place(x=0, y=0, relwidth=1, height=50)

# ============================= Menus ============================= #

        self.__main_frame = LabelFrame(self.__root, text="Menus",
                                       font=("times new roman", 15), bg="white")
        self.__main_frame.place(x=10, y=50, width=1340, height=80)

# ============================ Buttons ============================ #

        self.__btn_course = Button(self.__main_frame, text="Course", font=("goudy old style", 15, "bold"),
                                   bg="#0b5377", fg="white", cursor="hand2", command=(self.add_course)).place(x=20, y=5, width=200, height=45)
        self.__btn_student = Button(self.__main_frame, text="Student", font=("goudy old style", 15, "bold"),
                                    bg="#0b5377", fg="white", cursor="hand2", command=(self.add_student)).place(x=225, y=5, width=200, height=45)
        self.__btn_result = Button(self.__main_frame, text="Result", font=("goudy old style", 15, "bold"),
                                   bg="#0b5377", fg="white", cursor="hand2", command=(self.add_result)).place(x=430, y=5, width=200, height=45)
        self.__btn_view = Button(self.__main_frame, text="Student Result", font=("goudy old style", 15, "bold"),
                                 bg="#0b5377", fg="white", cursor="hand2", command=self.add_report).place(x=635, y=5, width=200, height=45)
        self.__btn_qrcode = Button(self.__main_frame, text="Genrate Result\nQR", font=("goudy old style", 15, "bold"),
                                   bg="#0b5377", fg="white", cursor="hand2", command=self.add_qr).place(x=840, y=5, width=200, height=45)
        self.__btn_exit = Button(self.__main_frame, text="Exit", font=("goudy old style", 15, "bold"),
                                 bg="#0b5377", fg="white", cursor="hand2", command=self.exit).place(x=1045, y=5, width=200, height=45)


# ============================ Footer ============================ #

        self.__footer = Label(self.__root, text="Student Management System \n Contact For Any Technical Issues : 9725XXXX96", font=(
            "goudy old style", 12, "bold"), bg="#262626", fg="white").pack(side=BOTTOM, fill=X)


# ============================ Content Image 1 ============================ #

        self.__bg_img = Image.open("Images/content.jpg")
        self.__bg_img = self.__bg_img.resize((920, 350), Image.ANTIALIAS)
        self.__bg_img = ImageTk.PhotoImage(self.__bg_img)

        self.__lbl_bg = Label(self.__root, image=self.__bg_img).place(
            x=20, y=200, width=850, height=350)

# ============================ Content Image 2 ============================ #

        self.__bg_img2 = Image.open("Images/thelearnr.png")
        self.__bg_img2 = self.__bg_img2.resize((540, 960), Image.ANTIALIAS)
        self.__bg_img2 = ImageTk.PhotoImage(self.__bg_img2)

        self.__lbl_bg2 = Label(self.__root, image=self.__bg_img2).place(
            x=825, y=200, width=440, height=460)


# ============================ Display Detalis  ============================ #

        self.__lbl_course = Label(self.__root, text="Total Courses \n [0]", font=(
            "goudy old style", 20), bd=10, relief=RIDGE, bg="#e43b06")
        self.__lbl_course.place(x=25, y=600, width=245, height=100)

        self.__lbl_student = Label(self.__root, text="Total Students \n [0]", font=(
            "goudy old style", 20), bd=10, relief=RIDGE, bg="#0676ad")
        self.__lbl_student.place(x=300, y=600, width=245, height=100)

        self.__lbl_result = Label(self.__root, text="Total Results \n [0]", font=(
            "goudy old style", 20), bd=10, relief=RIDGE, bg="#038074")
        self.__lbl_result.place(x=575, y=600, width=245, height=100)

        self.update_details()

    def update_details(self):
        self.__conn = sqlite3.connect(database="My_DB")
        self.__curr = self.__conn.cursor()
        try:
            self.__curr.execute("select * from course")
            self.__cr = self.__curr.fetchall()
            self.__lbl_course.config(
                text=f"Total Courses\n[{str(len(self.__cr))}]")

            self.__curr.execute("select * from student")
            self.__cr = self.__curr.fetchall()
            self.__lbl_student.config(
                text=f"Total Students\n[{str(len(self.__cr))}]")

            self.__curr.execute("select * from result")
            self.__cr = self.__curr.fetchall()
            self.__lbl_result.config(
                text=f"Total Results\n[{str(len(self.__cr))}]")

        except Exception as ex:
            messagebox.showerror("Error", f"Error due to {str(ex)}")

    def add_course(self):
        self.__new_win = Toplevel(self.__root)
        self.__new_obj = CourseDetails(self.__new_win)

    def add_student(self):
        self.__new_win = Toplevel(self.__root)
        self.__new_obj = StudentDetails(self.__new_win)

    def add_result(self):
        self.__new_win = Toplevel(self.__root)
        self.__new_obj = ResultDetails(self.__new_win)

    def add_report(self):
        self.__new_win = Toplevel(self.__root)
        self.__new_obj = ReportDetails(self.__new_win)

    def add_qr(self):
        self.__new_win = Toplevel(self.__root)
        self.__new_obj = Qr_Generater(self.__new_win)


# ============================ Update Details ============================ #


# ============================ Exit ============================ #

    def exit(self):
        self.__op = messagebox.askyesno("You want to Really Exit?")
        if self.__op == True:
            sys.exit()


if __name__ == "__main__":
    root = Tk()
    obj = RMS(root)
    root.mainloop()   # To Stable our display window
