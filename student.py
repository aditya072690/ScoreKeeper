from tkinter import*
from PIL import Image, ImageTk  # Pillow Libaray to use images in python code
from tkinter import ttk, messagebox
import sqlite3


class StudentDetails:

    def __init__(self, root):
        self.__root = root
        # To give a title of window
        self.__root.title("Student Management System")
        # geometry For give a width and Height
        self.__root.geometry("1200x630+40+170")
        self.__root.config(bg="white")
        self.__root.focus_force()


# ============================ Title ============================ #

        self.__title = Label(self.__root, text="Student Details", font=(
            "goudy old style", 20, "bold"), bg="#033054", fg="white").place(x=10, y=15, width=1180, height=35)

# ============================ Variables  ============================ #
        self.__var_enrollmentId = StringVar()
        self.__var_name = StringVar()
        self.__var_email = StringVar()
        self.__var_gender = StringVar()
        self.__var_dob = StringVar()
        self.__var_contact = StringVar()
        self.__var_course = StringVar()
        self.__var_a_date = StringVar()
        self.__var_state = StringVar()
        self.__var_city = StringVar()
        self.__var_pin = StringVar()


# ============================ Widgets ============================ #

# ============================ Column 1 ============================ #

        self.__lbl_enrollmentId = Label(self.__root, text="Enrolment ID", font=(
            "goudy old style", 12, "bold"), bg="white").place(x=10, y=80)

        self.__lbl_student_name = Label(self.__root, text="Student Name", font=(
            "goudy old style", 12, "bold"), bg="white").place(x=10, y=120)

        self.__lbl_email = Label(self.__root, text="Email", font=(
            "goudy old style", 12, "bold"), bg="white").place(x=10, y=160)

        self.__lbl_gender = Label(self.__root, text="Gender", font=(
            "goudy old style", 12, "bold"), bg="white").place(x=10, y=200)

        self.__lbl_state = Label(self.__root, text="State", font=(
            "goudy old style", 12, "bold"), bg="white").place(x=10, y=240)

        self.__txt_state = Entry(self.__root, textvariable=self.__var_state, font=(
            "goudy old style", 12, "bold"), bg="white")
        self.__txt_state.place(x=130, y=240, width=125)

        self.__lbl_city = Label(self.__root, text="City", font=(
            "goudy old style", 12, "bold"), bg="white").place(x=270, y=240)

        self.__txt_city = Entry(self.__root, textvariable=self.__var_city, font=(
            "goudy old style", 12, "bold"), bg="white")
        self.__txt_city.place(x=310, y=240, width=120)

        self.__lbl_pin = Label(self.__root, text="Pin", font=(
            "goudy old style", 12, "bold"), bg="white").place(x=450, y=240)

        self.__txt_pin = Entry(self.__root, textvariable=self.__var_pin, font=(
            "goudy old style", 12, "bold"), bg="white")
        self.__txt_pin.place(x=490, y=240, width=120)

        self.__lbl_address = Label(self.__root, text="Address", font=(
            "goudy old style", 12, "bold"), bg="white").place(x=10, y=290)


# ============================ Entry Fields   ============================ #

        self.__txt_enrollmentId = Entry(self.__root, textvariable=self.__var_enrollmentId, font=(
            "goudy old style", 12, "bold"), bg="white")
        self.__txt_enrollmentId.place(x=130, y=80, width=165)

        self.__txt_student_name = Entry(self.__root, textvariable=self.__var_name,  font=(
            "goudy old style", 12, "bold"), bg="white")
        self.__txt_student_name.place(x=130, y=120, width=165)

        self.__txt_email = Entry(self.__root, textvariable=self.__var_email,  font=(
            "goudy old style", 12, "bold"), bg="white")
        self.__txt_email.place(x=130, y=160, width=165)

        self.__txt_gender = ttk.Combobox(self.__root, textvariable=self.__var_gender, values=("Select", "Male", "Female", "Other"), font=(
            "goudy old style", 12, "bold"), state='readonly', justify=CENTER)
        self.__txt_gender.place(x=130, y=200, width=165)
        self.__txt_gender.current(0)

        self.__txt_address = Text(self.__root, font=(
            "goudy old style", 12, "bold"), bg="white")
        self.__txt_address.place(x=130, y=300, width=450, height=170)


# ============================ Column 2 ============================ #

        self.__lbl_dob = Label(self.__root, text="D.O.B", font=(
            "goudy old style", 12, "bold"), bg="white").place(x=310, y=80)

        self.__lbl_contact = Label(self.__root, text="Contact", font=(
            "goudy old style", 12, "bold"), bg="white").place(x=310, y=120)

        self.__lbl_addmission = Label(self.__root, text="Addmission", font=(
            "goudy old style", 12, "bold"), bg="white").place(x=310, y=160)

        self.__lbl_course = Label(self.__root, text="Course", font=(
            "goudy old style", 12, "bold"), bg="white").place(x=310, y=200)

 #============================ Entry Fields   ============================ #

#============================ List  ============================ #

        self.__course_list = ["Select"]  # Call Funcation
        self.fetch_course()

#============================ List  ============================ #

        self.__txt_dob = Entry(self.__root, textvariable=self.__var_dob, font=(
            "goudy old style", 12, "bold"), bg="white")
        self.__txt_dob.place(x=450, y=80, width=165)

        self.__txt_contact = Entry(self.__root, textvariable=self.__var_contact,  font=(
            "goudy old style", 12, "bold"), bg="white")
        self.__txt_contact.place(x=450, y=120, width=165)

        self.__txt_addmission = Entry(self.__root, textvariable=self.__var_a_date,  font=(
            "goudy old style", 12, "bold"), bg="white")
        self.__txt_addmission.place(x=450, y=160, width=165)

        self.__txt_course = ttk.Combobox(self.__root, textvariable=self.__var_course, values=self.__course_list, font=(
            "goudy old style", 12, "bold"), state='readonly', justify=CENTER)
        self.__txt_course.place(x=450, y=200, width=165)
        self.__txt_course.current(0)


# ============================ Buttons ============================ #

        self.__btn_add = Button(self.__root, text="Save", font=(
            "goudy old style", 15, "bold"), borderwidth=3, bg="#2196f3", fg="white", cursor="hand2", command=self.add)
        self.__btn_add.place(x=130, y=500, width=110, height=40)

        self.__btn_update = Button(self.__root, text="Update", font=(
            "goudy old style", 15, "bold"), borderwidth=3, bg="#4caf50", fg="white", cursor="hand2", command=self.update)
        self.__btn_update.place(x=250, y=500, width=110, height=40)

        self.__btn_delete = Button(self.__root, text="Delete", font=(
            "goudy old style", 15, "bold"), borderwidth=3, bg="#f44336", fg="white", cursor="hand2", command=self.delete)
        self.__btn_delete.place(x=370, y=500, width=110, height=40)

        self.__btn_clear = Button(self.__root, text="Clear", font=(
            "goudy old style", 15, "bold"), borderwidth=3, bg="#607d8b", fg="white", cursor="hand2", command=self.clear)
        self.__btn_clear.place(x=490, y=500, width=110, height=40)


# ============================ Search Panel  ============================ #

        self.__var_search_enrollmentId = StringVar()

        self.__lbl_search = Label(self.__root, text="  Search Student Here ", font=(
            "goudy old style", 15, "bold"), bg="#078054", fg="white").place(x=655, y=70, height=30, width=515)

        self.__lbl_search_EnrollmentId = Label(self.__root, text="Enrollment ID", font=(
            "goudy old style", 15, "bold"), bg="white").place(x=650, y=110)

        self.__txt_search_EnrollmentId = Entry(self.__root, textvariable=self.__var_search_enrollmentId, font=(
            "goudy old style", 15, "bold"), bg="white").place(x=830, y=110, width=200)

        self.__btn_search = Button(self.__root, text="Search 🔍", font=(
            "goudy old style", 15, "bold"), bg="#214545", fg="white", cursor="hand2", command=self.search)
        self.__btn_search.place(x=1050, y=110, width=120, height=25)


# ============================ Content ============================ #

        self.__C_Frame = Frame(self.__root, bd=2, relief=RIDGE)
        self.__C_Frame.place(x=655, y=150, width=515, height=400)

        scrolly = Scrollbar(self.__C_Frame, orient=VERTICAL)
        scrollx = Scrollbar(self.__C_Frame, orient=HORIZONTAL)

        self.__CourseTable = ttk.Treeview(self.__C_Frame, columns=(
            "enrollId", "name", "email", "gender", "dob", "contact", "addmission", "course", "state", "city", "pin", "address"), xscrollcommand=scrollx.set, yscrollcommand=scrolly.set)
        scrollx.pack(side=BOTTOM, fill=X)
        scrolly.pack(side=RIGHT, fill=Y)
        scrollx.config(command=self.__CourseTable.xview)
        scrolly.config(command=self.__CourseTable.yview)

        self.__CourseTable.heading("enrollId", text="Enrollment ID")
        self.__CourseTable.heading("name", text="Name")
        self.__CourseTable.heading("email", text="Email")
        self.__CourseTable.heading("gender", text="Gender")
        self.__CourseTable.heading("dob", text="D.O.B")
        self.__CourseTable.heading("contact", text="Contact")
        self.__CourseTable.heading("addmission", text="Admission")
        self.__CourseTable.heading("course", text="course")
        self.__CourseTable.heading("state", text="State")
        self.__CourseTable.heading("city", text="City")
        self.__CourseTable.heading("pin", text="City Pin")
        self.__CourseTable.heading("address", text="Address")

        self.__CourseTable["show"] = 'headings'
        self.__CourseTable.column("enrollId", width=100)
        self.__CourseTable.column("name", width=100)
        self.__CourseTable.column("email", width=100)
        self.__CourseTable.column("gender", width=100)
        self.__CourseTable.column("dob", width=100)
        self.__CourseTable.column("contact", width=100)
        self.__CourseTable.column("addmission", width=100)
        self.__CourseTable.column("course", width=100)
        self.__CourseTable.column("state", width=100)
        self.__CourseTable.column("city", width=100)
        self.__CourseTable.column("pin", width=100)
        self.__CourseTable.column("address", width=100)
        self.__CourseTable.pack(fill=BOTH, expand=1)

        self.__CourseTable.bind("<ButtonRelease-1>", self.get_data)
        self.show()

# ============================ Verification  ============================ #

    def clear(self):
        self.show()
        self.__var_enrollmentId.set("")
        self.__var_name.set("")
        self.__var_email.set("")
        self.__var_gender.set("Select")
        self.__var_dob.set("")
        self.__var_contact.set("")
        self.__var_a_date.set("")
        self.__var_course.set("Select")
        self.__var_state.set("")
        self.__var_city.set("")
        self.__var_pin.set("")
        self.__txt_address.delete("1.0", END)
        self.__txt_enrollmentId.config(state=NORMAL)
        self.__var_search_enrollmentId.set("")

    def delete(self):

        self.__connection = sqlite3.connect(database="My_DB")
        self.__cursor = self.__connection.cursor()
        try:
            if self.__var_enrollmentId.get() == "":
                messagebox.showerror(
                    "Error", "Course Name Should be Required ", parent=self.__root)
            else:
                self.__cursor.execute(
                    "select *from student where enrollId=?", (self.__var_enrollmentId.get(),))
                self.__row = self.__cursor.fetchone()
                if self.__row == None:
                    messagebox.showerror(
                        "Error", "Please Select Course From the list First 😒 ", parent=self.__root)
                else:
                    self.__confirm = messagebox.askyesno(
                        "Confirm", "Do you Really Want to Delete ? 🤨🤨", parent=self.__root)
                    if self.__confirm == True:
                        self.__cursor.execute(
                            "delete from student where enrollId=?", (self.__var_enrollmentId.get(),))
                        self.__connection.commit()
                        messagebox.showinfo(
                            "Delete", "Course Deleted Successfully 😃 ", parent=self.__root)
                        self.clear()
        except Exception as ex:
            messagebox.showerror("Error", f"Error dut to {str(ex)}")

    def get_data(self, ev):

        self.__txt_enrollmentId.config(state='readonly')
        r = self.__CourseTable.focus()
        content = self.__CourseTable.item(r)
        self.__row = content['values']
        print(self.__row)
        self.__var_enrollmentId.set(self.__row[0])
        self.__var_name.set(self.__row[1])
        self.__var_email.set(self.__row[2])
        self.__var_gender.set(self.__row[3])
        self.__var_dob.set(self.__row[4])
        self.__var_contact.set(self.__row[5])
        self.__var_a_date.set(self.__row[6])
        self.__var_course.set(self.__row[7])
        self.__var_state.set(self.__row[8])
        self.__var_city.set(self.__row[9])
        self.__var_pin.set(self.__row[10])
        self.__txt_address.delete("1.0", END)
        self.__txt_address.insert(END, self.__row[11])

    def add(self):

        self.__connection = sqlite3.connect(database="My_DB")
        self.__cursor = self.__connection.cursor()
        try:
            if self.__var_enrollmentId.get() == "":

                messagebox.showerror(
                    "Error", "All Student Details Should be Required ", parent=self.__root)
            else:
                self.__cursor.execute(
                    "select *from student where enrollId=?", (self.__var_enrollmentId.get(),))
                self.__row = self.__cursor.fetchone()
                if self.__row != None:
                    messagebox.showerror(
                        "Error", "Enrollment Id Already Present", parent=self.__root)
                else:
                    self.__cursor.execute(
                        "insert into student(enrollId,name ,email, gender, dob, contact,addmission, course, state, city,pin, address) values(?,?,?,?,?,?,?,?,?,?,?,?)", (
                            self.__var_enrollmentId.get(),
                            self.__var_name.get(),
                            self.__var_email.get(),
                            self.__var_gender.get(),
                            self.__var_dob.get(),
                            self.__var_contact.get(),
                            self.__var_a_date.get(),
                            self.__var_course.get(),
                            self.__var_state.get(),
                            self.__var_city.get(),
                            self.__var_pin.get(),
                            self.__txt_address.get("1.0", END)

                        ))
                    self.__connection.commit()
                    messagebox.showinfo(
                        "Success", "Student Added Successfully 😎", parent=self.__root)

                    self.show()
        except Exception as ex:
            messagebox.showerror("Error", f"Error due to {str(ex)}")

    def show(self):
        self.__connection = sqlite3.connect(database="My_DB")
        self.__cursor = self.__connection.cursor()
        try:
            self.__cursor.execute(
                "select *from student ")
            self.__rows = self.__cursor.fetchall()
            self.__CourseTable.delete(*self.__CourseTable.get_children())
            for row in self.__rows:
                self.__CourseTable.insert('', END, values=row)
        except Exception as ex:
            messagebox.showerror("Error", f"Error dut to {str(ex)}")

    def fetch_course(self):
        self.__connection = sqlite3.connect(database="My_DB")
        self.__cursor = self.__connection.cursor()
        try:
            self.__cursor.execute(
                "select name from course ")
            self.__rows = self.__cursor.fetchall()
            if len(self.__rows) > 0:
                for self.__row in self.__rows:
                    self.__course_list.append(self.__row[0])

        except Exception as ex:
            messagebox.showerror("Error", f"Error dut to {str(ex)}")

    def search(self):
        self.__connection = sqlite3.connect(database="My_DB")
        self.__cursor = self.__connection.cursor()
        try:
            self.__cursor.execute(
                "select *from student where enrollId=?", (self.__var_search_enrollmentId.get(),))
            self.__row = self.__cursor.fetchone()
            if self.__row != None:
                self.__CourseTable.delete(*self.__CourseTable.get_children())
                self.__CourseTable.insert('', END, values=self.__row)
            else:
                messagebox.showerror(
                    "Error", "No Record Found 😅", parent=self.__root)

        except Exception as ex:
            messagebox.showerror("Error", f"Error due to {str(ex)}")

    def update(self):

        self.__connection = sqlite3.connect(database="My_DB")
        self.__cursor = self.__connection.cursor()
        try:
            if self.__var_enrollmentId.get() == "":
                messagebox.showerror(
                    "Error", "Enrollment Id Should be Required ", parent=self.__root)
            else:
                self.__cursor.execute(
                    "select *from student where enrollId=?", (self.__var_enrollmentId.get(),))
                self.__row = self.__cursor.fetchone()
                if self.__row == None:
                    messagebox.showerror(
                        "Error", "Select Student Form List 😒 ", parent=self.__root)
                else:
                    self.__cursor.execute(
                        "update student set name=? ,email=?, gender=?, dob=?, contact=?,addmission=?, course=?, state=?, city=?,pin=?, address=? where enrollId=?", (
                            self.__var_name.get(),
                            self.__var_email.get(),
                            self.__var_gender.get(),
                            self.__var_dob.get(),
                            self.__var_contact.get(),
                            self.__var_a_date.get(),
                            self.__var_course.get(),
                            self.__var_state.get(),
                            self.__var_city.get(),
                            self.__var_pin.get(),
                            self.__txt_address.get("1.0", END),
                            self.__var_enrollmentId.get()
                        ))
                    self.__connection.commit()
                    messagebox.showinfo(
                        "Success", "Student Deatails Update Successfully 😍", parent=self.__root)

                    self.show()
        except Exception as ex:
            messagebox.showerror("Error", f"Error dut to {str(ex)}")


if __name__ == "__main__":
    root = Tk()
    obj = StudentDetails(root)
    root.mainloop()   # To Stable our display window
