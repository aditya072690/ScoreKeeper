import sqlite3


class My_database:

    def create_db(self):
        self.__connection = sqlite3.connect(database="My_DB")
        self.__cursor = self.__connection.cursor()
        self.__cursor.execute(
            "CREATE TABLE IF NOT EXISTS course(cid INTEGER PRIMARY KEY AUTOINCREMENT , name text , duration text ,charges text , description)")

        self.__connection.commit()

        self.__cursor.execute(
            "CREATE TABLE IF NOT EXISTS student(enrollId INTEGER PRIMARY KEY AUTOINCREMENT , name text, email text, gender text, dob text, contact text, addmission text, course text, state text ,city text, pin text, address text)")

        self.__connection.commit()

        self.__cursor.execute(
            "CREATE TABLE IF NOT EXISTS result(enrollId INTEGER PRIMARY KEY AUTOINCREMENT ,enrollmentId text,name text, course text,marks_ob text , full_marks ,per text)")

        self.__connection.commit()

        self.__connection.close()


run = My_database()
run.create_db()
