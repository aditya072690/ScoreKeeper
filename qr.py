from tkinter import*
import qrcode
from PIL import Image, ImageTk
from resizeimage import resizeimage
from tkinter import ttk, messagebox
import sqlite3


class Qr_Generater():

    def __init__(self, root):
        self.__root = root
        # To give a title of window
        self.__root.title("Student Management System")
        # geometry For give a width and Height
        self.__root.geometry("1200x630+40+170")
        self.__root.config(bg="white")
        self.__root.focus_force()


# ============================ Title ============================ #

        self.__title = Label(self.__root, text=" Genrate Student Result QR Code ", font=(
            "goudy old style", 20, "bold"), bg="orange", fg="#262626").place(x=10, y=15, width=1180, height=50)


# ============================ Variable ============================ #
        self.__var_enrollId = StringVar()
        self.__var_name = StringVar()
        self.__var_course = StringVar()
        self.__var_marks = StringVar()
        self.__var_full_marks = StringVar()
        self.__var_per = StringVar()

# ============================ Title ============================ #

        self.__enrollId_List = []
        self.fetch_enrollId()


# ============================ Title ============================ #

        self.__lab_select = Label(self.__root, text="Select Student", font=(
            "goudy old style", 15, "bold"), fg="black", bg="white").place(x=60, y=100)
        self.__lab_name = Label(self.__root, text="Name", font=(
            "goudy old style", 15, "bold"), fg="black", bg="white").place(x=60, y=160)
        self.__lab_course = Label(self.__root, text="Course", font=(
            "goudy old style", 15, "bold"), fg="black", bg="white").place(x=60, y=220)
        self.__lab_marks_ob = Label(self.__root, text="Marks Obtained", font=(
            "goudy old style", 15, "bold"), fg="black", bg="white").place(x=60, y=280)
        self.__lab_full_marks = Label(self.__root, text="Full Marks", font=(
            "goudy old style", 15, "bold"), fg="black", bg="white").place(x=60, y=340)

        self.__txt_student = ttk.Combobox(self.__root, textvariable=self.__var_enrollId, values=self.__enrollId_List, font=(
            "goudy old style", 12, "bold"), state='readonly', justify=CENTER)
        self.__txt_student.place(x=250, y=100, width=175, height=30)
        self.__txt_student.set("Select")

        self.__txt_name = Entry(self.__root, textvariable=self.__var_name, font=(
            "goudy old style", 12, "bold"), state='readonly', bg="white")
        self.__txt_name.place(x=250, y=160, width=300, height=30)

        self.__txt_course = Entry(self.__root, textvariable=self.__var_course, font=(
            "goudy old style", 12, "bold"), state='readonly', bg="white")
        self.__txt_course.place(x=250, y=220, width=300, height=30)

        self.__txt_marks_ob = Entry(self.__root, textvariable=self.__var_marks, font=(
            "goudy old style", 12, "bold"), state='readonly', bg="white")
        self.__txt_marks_ob.place(x=250, y=280, width=300, height=30)

        self.__txt_full_marks = Entry(self.__root, textvariable=self.__var_full_marks, font=(
            "goudy old style", 12, "bold"), state='readonly', bg="white")
        self.__txt_full_marks.place(x=250, y=340, width=300, height=30)


# ============================ Title ============================ #

        self.__btn_search = Button(self.__root, text="Search", font=(
            "goudy old style", 15, "bold"), command=self.search, bg="#214545", fg="white", cursor="hand2")
        self.__btn_search.place(x=430, y=100, width=120, height=30)


# ============================ Button ============================ #

        self.__btn_add = Button(
            self.__root, text="Genrate", font=("times new roman", 15), bg="lightgreen", activebackground="lightgreen", cursor="hand2", command=self.generate)
        self.__btn_add.place(x=300, y=420, width=120, height=35)

        self.__btn_clear = Button(
            self.__root, text="Clear", font=("times new roman", 15), bg="lightgray", activebackground="lightgray", cursor="hand2", command=self.clear)
        self.__btn_clear.place(x=430, y=420, width=120, height=35)


# ============================ Content Window ============================ #

        self.__bg_img = Image.open("Images/result.png")
        self.__bg_img = self.__bg_img.resize((550, 350), Image.ANTIALIAS)
        self.__bg_img = ImageTk.PhotoImage(self.__bg_img)

        self.__lbl_bg = Label(self.__root, image=self.__bg_img).place(
            x=600, y=90)

 
# ==== student Details window========

    def fetch_enrollId(self):
        self.__connection = sqlite3.connect(database="My_DB")
        self.__cursor = self.__connection.cursor()
        try:
            self.__cursor.execute(
                "select enrollId from student ")
            self.__rows = self.__cursor.fetchall()
            if len(self.__rows) > 0:
                for self.__row in self.__rows:
                    self.__enrollId_List.append(self.__row[0])

        except Exception as ex:
            messagebox.showerror("Error", f"Error due to {str(ex)}")


# ============================ Search  ============================ #

    def search(self):
        self.__connection = sqlite3.connect(database="My_DB")
        self.__cursor = self.__connection.cursor()
        try:
            self.__cursor.execute(
                "select name,course,marks_ob,full_marks,per from result where enrollmentId=?", (self.__var_enrollId.get(),))
            self.__row = self.__cursor.fetchone()
            if self.__row != None:
                self.__var_name.set(self.__row[0])
                self.__var_course.set(self.__row[1])
                self.__var_marks.set(self.__row[2])
                self.__var_full_marks.set(self.__row[3])
                self.__var_per.set(self.__row[4])
            else:
                messagebox.showerror(
                    "Error", "Select Student Enrollment ID First 😅", parent=self.__root)

        except Exception as ex:
            messagebox.showerror("Error", f"Error due to {str(ex)}")

    def clear(self):
        self.__var_enrollId.set('')
        self.__var_name.set('')
        self.__var_course.set('')
        self.__var_marks.set('')
        self.__var_full_marks.set('')
        self.__var_per.set('')
        self.__msg = ''
        self.__lbl_mgs.config(text=self.__msg)

    def generate(self):
        if self.__var_enrollId.get() == '':
            self.__msg = 'Enrollment ID Should Be Required!!!'
            self.__lbl_mgs.config(text=self.__msg, fg='red')
        else:
            self.__qr_data = (
                f"Student Id:{self.__var_enrollId.get()}\nStudent Name:{self.__var_name.get()}\nCourse:{self.__var_course.get()}\nMarks Obtained:{self.__var_marks.get()}\nFull Marks:{self.__var_full_marks.get()}\nPercentage:{self.__var_per.get()}")
            self.__qr_code = qrcode.make(self.__qr_data)
            # print(qr_code)
            self.__qr_code = resizeimage.resize_cover(
                self.__qr_code, [180, 180])
            self.__qr_code.save("Student_" +
                                str(self.__var_enrollId.get())+".png")
            # ======QR CODE IMAGE UPDATE=======
            self.__im = ImageTk.PhotoImage(
                file="Student_" + str(self.__var_enrollId.get())+".png")

            self.__msg = 'QR Genrated Successfully!!!'
            self.__lbl_mgs = Label(self.__root, text=self.__msg, font=(
                "time new roman", 20), bg='white', fg='green')
            self.__lbl_mgs.place(x=100, y=510,)

            # ======Updating Notification=======
            self.__msg = 'QR Genrated Successfully!!!'
            self.__lbl_mgs.config(text=self.__msg, fg='green')


if __name__ == "__main__":
    root = Tk()
    obj = Qr_Generater(root)
    root.mainloop()
