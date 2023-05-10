from tkinter import*
from PIL import Image, ImageTk  # Pillow Libaray to use images in python code
from tkinter import ttk, messagebox
import sqlite3


class CourseDetails:

    def __init__(self, root):
        self.__root = root
        # To give a title of window
        self.__root.title("Student Management System")
        # geometry For give a width and Height
        self.__root.geometry("1200x630+40+170")
        self.__root.config(bg="white")
        self.__root.focus_force()


# ============================ Title ============================ #

        self.__title = Label(self.__root, text="Avalibale Courses For Student ", font=(
            "goudy old style", 20, "bold"), bg="#033054", fg="white").place(x=10, y=15, width=1180, height=35)

# ============================ Variables  ============================ #
        self.__var_Coursename = StringVar()
        self.__var_Duration = StringVar()
        self.__var_Charges = StringVar()


# ============================ Widgets ============================ #

        self.__lbl_Coursename = Label(self.__root, text="Course Name", font=(
            "goudy old style", 15, "bold"), bg="white").place(x=10, y=80)

        self.__lbl_Duration = Label(self.__root, text="Duration ", font=(
            "goudy old style", 15, "bold"), bg="white").place(x=10, y=120)

        self.__lbl_Charges = Label(self.__root, text="Charges", font=(
            "goudy old style", 15, "bold"), bg="white").place(x=10, y=160)

        self.__lbl_Description = Label(self.__root, text="Description", font=(
            "goudy old style", 15, "bold"), bg="white").place(x=10, y=200)

# ============================ Entry Fields   ============================ #

        self.__txt_Coursename = Entry(self.__root, textvariable=self.__var_Coursename, font=(
            "goudy old style", 15, "bold"), bg="white")
        self.__txt_Coursename.place(x=150, y=80, width=200)

        self.__txt_Duration = Entry(self.__root, textvariable=self.__var_Duration,  font=(
            "goudy old style", 15, "bold"), bg="white")
        self.__txt_Duration.place(x=150, y=120, width=200)

        self.__txt_Charges = Entry(self.__root, textvariable=self.__var_Charges,  font=(
            "goudy old style", 15, "bold"), bg="white")
        self.__txt_Charges.place(x=150, y=160, width=200)

        self.__txt_Description = Text(self.__root, font=(
            "goudy old style", 15, "bold"), bg="white")
        self.__txt_Description.place(x=150, y=200, width=450, height=200)


# ============================ Buttons ============================ #

        self.__btn_add = Button(self.__root, text="Save", font=(
            "goudy old style", 15, "bold"), borderwidth=3, bg="#2196f3", fg="white", cursor="hand2", command=self.add)
        self.__btn_add.place(x=150, y=450, width=110, height=40)

        self.__btn_update = Button(self.__root, text="Update", font=(
            "goudy old style", 15, "bold"), borderwidth=3, bg="#4caf50", fg="white", cursor="hand2", command=self.update)
        self.__btn_update.place(x=270, y=450, width=110, height=40)

        self.__btn_delete = Button(self.__root, text="Delete", font=(
            "goudy old style", 15, "bold"), borderwidth=3, bg="#f44336", fg="white", cursor="hand2", command=self.delete)
        self.__btn_delete.place(x=390, y=450, width=110, height=40)

        self.__btn_clear = Button(self.__root, text="Clear", font=(
            "goudy old style", 15, "bold"), borderwidth=3, bg="#607d8b", fg="white", cursor="hand2", command=self.clear)
        self.__btn_clear.place(x=510, y=450, width=110, height=40)


# ============================ Search Panel  ============================ #

        self.__var_search_Coursename = StringVar()

        self.__lbl_search = Label(self.__root, text="Search Here", font=(
            "goudy old style", 15, "bold"), bg="white").place(x=650, y=80)

        self.__lbl_search_Coursename = Label(self.__root, text="Course Name", font=(
            "goudy old style", 15, "bold"), bg="white").place(x=650, y=110)

        self.__txt_search_Coursename = Entry(self.__root, textvariable=self.__var_search_Coursename, font=(
            "goudy old style", 15, "bold"), bg="white").place(x=830, y=110, width=200)

        self.__btn_search = Button(self.__root, text="Search", font=(
            "goudy old style", 15, "bold"), bg="#214545", fg="white", cursor="hand2", command=self.search)
        self.__btn_search.place(x=1050, y=110, width=120, height=25)


# ============================ Content ============================ #

        self.__C_Frame = Frame(self.__root, bd=2, relief=RIDGE)
        self.__C_Frame.place(x=655, y=150, width=515, height=400)

        scrolly = Scrollbar(self.__C_Frame, orient=VERTICAL)
        scrollx = Scrollbar(self.__C_Frame, orient=HORIZONTAL)

        self.__CourseTable = ttk.Treeview(self.__C_Frame, columns=(
            "cid", "name", "duration", "charges", "description"), xscrollcommand=scrollx.set, yscrollcommand=scrolly.set)
        scrollx.pack(side=BOTTOM, fill=X)
        scrolly.pack(side=RIGHT, fill=Y)
        scrollx.config(command=self.__CourseTable.xview)
        scrolly.config(command=self.__CourseTable.yview)

        self.__CourseTable.heading("cid", text="Course ID")
        self.__CourseTable.heading("name", text="Name")
        self.__CourseTable.heading("duration", text="Duration")
        self.__CourseTable.heading("charges", text="Charges")
        self.__CourseTable.heading("description", text="Description")
        self.__CourseTable["show"] = 'headings'
        self.__CourseTable.column("cid", width=70)
        self.__CourseTable.column("name", width=100)
        self.__CourseTable.column("duration", width=100)
        self.__CourseTable.column("charges", width=100)
        self.__CourseTable.column("description", width=300)
        self.__CourseTable.pack(fill=BOTH, expand=1)
        self.__CourseTable.bind("<ButtonRelease-1>", self.get_data)
        self.show()

# ============================ Verification  ============================ #

    def clear(self):
        self.show()
        self.__var_Coursename.set("")
        self.__var_Duration.set("")
        self.__var_Charges.set("")
        self.__var_search_Coursename.set("")
        self.__txt_Description.delete('1.0', END)
        self.__txt_Coursename.config(state=NORMAL)

    def delete(self):

        self.__connection = sqlite3.connect(database="My_DB")
        self.__cursor = self.__connection.cursor()
        try:
            if self.__var_Coursename.get() == "":
                messagebox.showerror(
                    "Error", "Course Name Should be Required ", parent=self.__root)
            else:
                self.__cursor.execute(
                    "select *from course where name=?", (self.__var_Coursename.get(),))
                self.__row = self.__cursor.fetchone()
                if self.__row == None:
                    messagebox.showerror(
                        "Error", "Please Select Course From the list First 😒 ", parent=self.__root)
                else:
                    self.__confirm = messagebox.askyesno(
                        "Confirm", "Do you Really Want to Delete ? 🤨🤨", parent=self.__root)
                    if self.__confirm == True:
                        self.__cursor.execute(
                            "delete from course where name=?", (self.__var_Coursename.get(),))
                        self.__connection.commit()
                        messagebox.showinfo(
                            "Delete", "Course Deleted Successfully 😃 ", parent=self.__root)
                        self.clear()
        except Exception as ex:
            messagebox.showerror("Error", f"Error dut to {str(ex)}")

    def get_data(self, ev):

        self.__txt_Coursename.config(state='readonly')
        r = self.__CourseTable.focus()
        content = self.__CourseTable.item(r)
        row = content['values']
        # print(row)
        self.__var_Coursename.set(row[1])
        self.__var_Duration.set(row[2])
        self.__var_Charges.set(row[3])
        # self.__var_Coursename.set(row[1])
        self.__txt_Description.delete('1.0', END)
        self.__txt_Description.insert(END, row[4])

    def add(self):

        self.__connection = sqlite3.connect(database="My_DB")
        self.__cursor = self.__connection.cursor()
        try:
            if self.__var_Coursename.get() == "":
                messagebox.showerror(
                    "Error", "Course Name Should be Required ", parent=self.__root)
            else:
                self.__cursor.execute(
                    "select *from course where name=?", (self.__var_Coursename.get(),))
                self.__row = self.__cursor.fetchone()
                if self.__row != None:
                    messagebox.showerror(
                        "Error", "Course Is Present", parent=self.__root)
                else:
                    self.__cursor.execute(
                        "insert into course (name,duration,charges,description) values(?,?,?,?)", (
                            self.__var_Coursename.get(),
                            self.__var_Duration.get(),
                            self.__var_Charges.get(),
                            self.__txt_Description.get("1.0", END)

                        ))
                    self.__connection.commit()
                    messagebox.showinfo(
                        "Success", "Course Added Successfully", parent=self.__root)

                    self.show()
        except Exception as ex:
            messagebox.showerror("Error", f"Error dut to {str(ex)}")

    def show(self):
        self.__connection = sqlite3.connect(database="My_DB")
        self.__cursor = self.__connection.cursor()
        try:
            self.__cursor.execute(
                "select *from course ")
            self.__rows = self.__cursor.fetchall()
            self.__CourseTable.delete(*self.__CourseTable.get_children())
            for row in self.__rows:
                self.__CourseTable.insert('', END, values=row)
        except Exception as ex:
            messagebox.showerror("Error", f"Error dut to {str(ex)}")

    def search(self):
        self.__connection = sqlite3.connect(database="My_DB")
        self.__cursor = self.__connection.cursor()
        try:
            self.__cursor.execute(
                f"select *from course where name LIKE '%{self.__var_search_Coursename.get()}%'")
            self.__rows = self.__cursor.fetchall()
            self.__CourseTable.delete(*self.__CourseTable.get_children())
            for row in self.__rows:
                self.__CourseTable.insert('', END, values=row)
        except Exception as ex:
            messagebox.showerror("Error", f"Error dut to {str(ex)}")

    def update(self):

        self.__connection = sqlite3.connect(database="My_DB")
        self.__cursor = self.__connection.cursor()
        try:
            if self.__var_Coursename.get() == "":
                messagebox.showerror(
                    "Error", "Course Name Should be Required ", parent=self.__root)
            else:
                self.__cursor.execute(
                    "select *from course where name=?", (self.__var_Coursename.get(),))
                self.__row = self.__cursor.fetchone()
                if self.__row == None:
                    messagebox.showerror(
                        "Error", "Select Course Form List 😒 ", parent=self.__root)
                else:
                    self.__cursor.execute(
                        "update course set duration=?,charges=?,description=? where name=?", (
                            self.__var_Duration.get(),
                            self.__var_Charges.get(),
                            self.__txt_Description.get("1.0", END),
                            self.__var_Coursename.get()
                        ))
                    self.__connection.commit()
                    messagebox.showinfo(
                        "Success", "Course Update Successfully 😍", parent=self.__root)

                    self.show()
        except Exception as ex:
            messagebox.showerror("Error", f"Error dut to {str(ex)}")


if __name__ == "__main__":
    root = Tk()
    obj = CourseDetails(root)
    root.mainloop()   # To Stable our display window
