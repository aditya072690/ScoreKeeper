from tkinter import*
from tkinter import font
from PIL import Image, ImageTk  # Pillow Libaray to use images in python code
from tkinter import ttk, messagebox
import sqlite3


class ReportDetails:

    def __init__(self, root):
        self.__root = root
        # To give a title of window
        self.__root.title("Student Management System")
        # geometry For give a width and Height
        self.__root.geometry("1200x630+40+170")
        self.__root.config(bg="white")
        self.__root.focus_force()


# ============================ Title ============================ #

        self.__title = Label(self.__root, text="View Student Result", font=(
            "goudy old style", 20, "bold"), bg="orange", fg="#262626").place(x=10, y=15, width=1180, height=50)


# ============================ Search ============================ #

        self.__var_search = StringVar()
        self.__var_id = ""
        self.__lab_search = Label(self.__root, text="Search By Roll NO.", font=(
            "goudy old style", 15, "bold"), fg="black", bg="white").place(x=280, y=100)

        self.__lab_search = Entry(self.__root, textvariable=self.__var_search, font=(
            "goudy old style", 15, ), fg="black", bg="lightyellow").place(x=520, y=100, width=150)

        self.__btn_search = Button(self.__root, text="Search", font=(
            "goudy old style", 15, "bold"), bg="#214545", fg="white", cursor="hand2", command=self.search)
        self.__btn_search.place(x=680, y=100, width=120, height=28)

        self.__btn_clear = Button(self.__root, text="Clear", font=(
            "goudy old style", 15, "bold"), bg="red", fg="white", cursor="hand2", command=self.clear)
        self.__btn_clear.place(x=810, y=100, width=120, height=28)

# ============================ Result_labels============================ #
# 1
        self.__lab_roll = Label(self.__root, text="Roll No.", font=(
            "goudy old style", 15, "bold"), bg="white", bd=2, relief=GROOVE)
        self.__lab_roll.place(x=150, y=230, width=150, height=50)
# 2
        self.__lab_name = Label(self.__root, text="Name", font=(
            "goudy old style", 15, "bold"), bg="white", bd=2, relief=GROOVE)
        self.__lab_name.place(x=300, y=230, width=150, height=50)
# 3
        self.__lab_course = Label(self.__root, text="Course", font=(
            "goudy old style", 15, "bold"), bg="white", bd=2, relief=GROOVE)
        self.__lab_course.place(x=450, y=230, width=150, height=50)
# 4
        self.__lab_marks = Label(self.__root, text="Marks Obtained", font=(
            "goudy old style", 15, "bold"), bg="white", bd=2, relief=GROOVE)
        self.__lab_marks.place(x=600, y=230, width=150, height=50)
# 5
        self.__lab_full = Label(self.__root, text="Total Marks", font=(
            "goudy old style", 15, "bold"), bg="white", bd=2, relief=GROOVE)
        self.__lab_full.place(x=750, y=230, width=150, height=50)
# 6
        self.__lab_per = Label(self.__root, text="Percentage", font=(
            "goudy old style", 15, "bold"), bg="white", bd=2, relief=GROOVE)
        self.__lab_per.place(x=900, y=230, width=150, height=50)


# ============================ Result_Show_Labels============================ #
# 1
        self.__roll = Label(self.__root, font=(
            "goudy old style", 15, "bold"), bg="white", bd=2, relief=GROOVE)
        self.__roll.place(x=150, y=280, width=150, height=50)
# 2
        self.__name = Label(self.__root, font=(
            "goudy old style", 15, "bold"), bg="white", bd=2, relief=GROOVE)
        self.__name.place(x=300, y=280, width=150, height=50)
# 3
        self.__course = Label(self.__root, font=(
            "goudy old style", 15, "bold"), bg="white", bd=2, relief=GROOVE)
        self.__course.place(x=450, y=280, width=150, height=50)
# 4
        self.__marks = Label(self.__root, font=(
            "goudy old style", 15, "bold"), bg="white", bd=2, relief=GROOVE)
        self.__marks.place(x=600, y=280, width=150, height=50)
# 5
        self.__full = Label(self.__root, font=(
            "goudy old style", 15, "bold"), bg="white", bd=2, relief=GROOVE)
        self.__full.place(x=750, y=280, width=150, height=50)
# 6
        self.__per = Label(self.__root, font=(
            "goudy old style", 15, "bold"), bg="white", bd=2, relief=GROOVE)
        self.__per.place(x=900, y=280, width=150, height=50)

# ============================ Button Delet============================ #

        self.__btn_delete = Button(self.__root, text="Delete", font=(
            "goudy old style", 15, "bold"), bg="red", fg="white", cursor="hand2", command=self.delete)
        self.__btn_delete.place(x=545, y=350, width=120, height=28)

# ============================ Search  ============================ #

    def search(self):
        self.__connection = sqlite3.connect(database="My_DB")
        self.__cursor = self.__connection.cursor()
        try:
            if self.__var_search.get() == "":
                messagebox.showerror(
                    "Error", "Roll No. Should Be Required", parent=self.__root)

            else:
                self.__cursor.execute(
                    "select * from result where enrollmentId=?", (self.__var_search.get(),))
                self.__row = self.__cursor.fetchone()
                if self.__row != None:
                    self.__var_id = self.__row[0]
                    self.__roll.config(text=self.__row[1])
                    self.__name.config(text=self.__row[2])
                    self.__course.config(text=self.__row[3])
                    self.__marks.config(text=self.__row[4])
                    self.__full.config(text=self.__row[5])
                    self.__per.config(text=self.__row[6])
                else:
                    messagebox.showerror(
                        "Error", "No Record Found 😅", parent=self.__root)

        except Exception as ex:
            messagebox.showerror("Error", f"Error due to {str(ex)}")

# ============================ Clear ============================ #

    def clear(self):
        self.__var_id = ""
        self.__roll.config(text="")
        self.__name.config(text="")
        self.__course.config(text="")
        self.__marks.config(text="")
        self.__full.config(text="")
        self.__per.config(text="")
        self.__var_search.set("")

# ============================ Clear ============================ #

    def delete(self):

        self.__connection = sqlite3.connect(database="My_DB")
        self.__cursor = self.__connection.cursor()
        try:
            if self.__var_id == "":
                messagebox.showerror(
                    "Error", "Search Student result First", parent=self.__root)
            else:
                self.__cursor.execute(
                    "select * from result where enrollId=?", (self.__var_id,))
                self.__row = self.__cursor.fetchone()
                if self.__row == None:
                    messagebox.showerror(
                        "Error", "Invalid Student Result ", parent=self.__root)
                else:
                    self.__confirm = messagebox.askyesno(
                        "Confirm", "Do you Really Want to Delete ? 🤨🤨", parent=self.__root)
                    if self.__confirm == True:
                        self.__cursor.execute(
                            "delete from result where enrollId=?", (self.__var_id,))
                        self.__connection.commit()
                        messagebox.showinfo(
                            "Delete", "Result Deleted Successfully😃 ", parent=self.__root)
                        self.clear()
        except Exception as ex:
            messagebox.showerror("Error", f"Error dut to {str(ex)}")


'''
rid = enrollId
result = result
'''

if __name__ == "__main__":
    root = Tk()
    obj = ReportDetails(root)
    root.mainloop()   # To Stable our display window
