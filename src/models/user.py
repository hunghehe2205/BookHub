import mysql.connector
from mysql.connector import Error
from pydantic import EmailStr


class UserModel:
    def __init__(self, db_config):
        self.db_config = db_config

    def get_db_connection(self):
        try:
            connection = mysql.connector.connect(**self.db_config)
            if connection.is_connected():
                return connection
        except Error as e:
            print(f"Error connecting to database: {e}")
        return None

    def create_user(self, username: str, email: str, password: str):
        connection = self.get_db_connection()
        if connection:
            try:
                cursor = connection.cursor()
                insert_query = "INSERT INTO User (UserName, Email, Password) VALUES (%s, %s, %s)"
                cursor.execute(insert_query, (username, email, password))
                connection.commit()
                return cursor.lastrowid
            except Error as e:
                print(f"Error creating user: {e}")
                connection.rollback()
            finally:
                cursor.close()
                connection.close()
        return None

    def get_user_by_id(self, user_id: int):
        connection = self.get_db_connection()
        if connection:
            try:
                cursor = connection.cursor(dictionary=True)
                select_query = "SELECT * FROM User WHERE UserID = %s"
                cursor.execute(select_query, (user_id,))
                return cursor.fetchone()
            except Error as e:
                print(f"Error fetching user by ID: {e}")
            finally:
                cursor.close()
                connection.close()
        return None

    def get_user_by_email(self, email: EmailStr):
        connection = self.get_db_connection()
        if connection:
            try:
                cursor = connection.cursor(dictionary=True)
                select_query = "SELECT * FROM User WHERE Email = %s"
                cursor.execute(select_query, (email,))
                return cursor.fetchone()
            except Error as e:
                print(f"Error fetching user by ID: {e}")
            finally:
                cursor.close()
                connection.close()
        return None

    def get_user_by_username(self, username: str):
        connection = self.get_db_connection()
        if connection:
            try:
                cursor = connection.cursor(dictionary=True)
                select_query = "SELECT * FROM User WHERE Username = %s"
                cursor.execute(select_query, (username,))
                return cursor.fetchone()
            except Error as e:
                print(f"Error fetching user by ID: {e}")
            finally:
                cursor.close()
                connection.close()
        return None

    def update_user(self, user_id: int, username: str = None, email: str = None, password: str = None, streak: int = None):
        connection = self.get_db_connection()
        if connection:
            try:
                cursor = connection.cursor()
                update_query = "UPDATE User SET "
                fields = []
                values = []
                if username:
                    fields.append("UserName = %s")
                    values.append(username)
                if email:
                    fields.append("Email = %s")
                    values.append(email)
                if password:
                    fields.append("Password = %s")
                    values.append(password)
                if streak is not None:
                    fields.append("Streak = %s")
                    values.append(streak)
                values.append(user_id)
                if fields:
                    update_query += ", ".join(fields) + " WHERE UserID = %s"
                    print(update_query)
                    cursor.execute(update_query, tuple(values))
                    connection.commit()
                    return cursor.rowcount > 0
            except Error as e:
                print(f"Error updating user: {e}")
                connection.rollback()
            finally:
                cursor.close()
                connection.close()
        return False

    def delete_user(self, user_id: int):
        connection = self.get_db_connection()
        if connection:
            try:
                cursor = connection.cursor()
                delete_query = "DELETE FROM User WHERE UserID = %s"
                cursor.execute(delete_query, (user_id,))
                connection.commit()
                return cursor.rowcount > 0
            except Error as e:
                print(f"Error deleting user: {e}")
                connection.rollback()
            finally:
                cursor.close()
                connection.close()
        return False
