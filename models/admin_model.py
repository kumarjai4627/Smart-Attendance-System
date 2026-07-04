from database.db import mysql


class AdminModel:

    @staticmethod
    def login(username, password):

        try:

            cursor = mysql.connection.cursor()

            query = """
            SELECT * FROM admin
            WHERE username=%s AND password=%s
            """

            cursor.execute(query, (username, password))

            admin = cursor.fetchone()

            cursor.close()

            return admin

        except Exception as e:
            print(e)
            return None