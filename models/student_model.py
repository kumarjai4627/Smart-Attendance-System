from database.db import mysql


class StudentModel:

    @staticmethod
    def add_student(student_data):
        try:
            cursor = mysql.connection.cursor()

            query = """
            INSERT INTO students
            (
                student_id,
                name,
                email,
                phone,
                course,
                branch,
                semester,
                section,
                gender,
                dob,
                address,
                photo_sample
            )
            VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)
            """

            values = (
                student_data["student_id"],
                student_data["name"],
                student_data["email"],
                student_data["phone"],
                student_data["course"],
                student_data["branch"],
                student_data["semester"],
                student_data["section"],
                student_data["gender"],
                student_data["dob"],
                student_data["address"],
                student_data["photo_sample"]
            )

            cursor.execute(query, values)
            mysql.connection.commit()
            cursor.close()

            return True
        

        except Exception as e:
            print(e)
            return False
            from database.db import mysql


class StudentModel:

    @staticmethod
    def add_student(student_data):
        try:
            cursor = mysql.connection.cursor()

            query = """
            INSERT INTO students
            (
                student_id,
                name,
                email,
                phone,
                course,
                branch,
                semester,
                section,
                gender,
                dob,
                address,
                photo_sample
            )
            VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)
            """

            values = (
                student_data["student_id"],
                student_data["name"],
                student_data["email"],
                student_data["phone"],
                student_data["course"],
                student_data["branch"],
                student_data["semester"],
                student_data["section"],
                student_data["gender"],
                student_data["dob"],
                student_data["address"],
                student_data["photo_sample"]
            )

            cursor.execute(query, values)
            mysql.connection.commit()
            cursor.close()

            return True

        except Exception as e:
            print(e)
            return False


    @staticmethod
    def get_all_students():
        try:
            cursor = mysql.connection.cursor()

            query = "SELECT * FROM students ORDER BY id DESC"

            cursor.execute(query)

            students = cursor.fetchall()

            cursor.close()

            return students

        except Exception as e:
            print(e)
            return []