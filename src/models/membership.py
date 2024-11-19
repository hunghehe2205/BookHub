import mysql.connector
from mysql.connector import Error
from datetime import date


class MembershipModel:
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

    def create_membership(self, user_id: int, type: str, expired_day: date, remaining_books: int):
        connection = self.get_db_connection()
        if connection:
            try:
                cursor = connection.cursor(dictionary=True)
                insert_query = "INSERT INTO Membership (UserID, Type, ExpiredDay, RemainingBooks) VALUES (%s, %s, %s, %s)"
                cursor.execute(insert_query, (user_id, type,
                               expired_day, remaining_books))
                connection.commit()
                return cursor.rowcount
            except Error as e:
                print(f"Error creating membership: {e}")
                connection.rollback()
            finally:
                cursor.close()
                connection.close()
        return None

    def update_membership(self, user_id: int,
                          type: str = None,
                          expired_day: date = None,
                          remaining_books: int = None):
        connection = self.get_db_connection()
        if connection:
            try:
                cursor = connection.cursor()
                update_query = "UPDATE Membership SET "
                fields = []
                values = []
                if type:
                    fields.append("Type = %s")
                    values.append(type)
                if expired_day:
                    fields.append("ExpiredDay = %s")
                    values.append(expired_day)
                if remaining_books is not None:
                    fields.append("RemainingBooks = %s")
                    values.append(remaining_books)
                values.append(user_id)
                if fields:
                    update_query += ", ".join(fields) + " WHERE UserID = %s"
                    cursor.execute(update_query, tuple(values))
                    connection.commit()
                    return cursor.rowcount > 0
            except Error as e:
                print(f"Error updating Membership: {e}")
                connection.rollback()
            finally:
                cursor.close()
                connection.close()
        return False

    def delete_membership(self, user_id: int):
        connection = self.get_db_connection()
        if connection:
            try:
                cursor = connection.cursor()
                delete_query = "DELETE FROM Membership WHERE UserID = %s"
                cursor.execute(delete_query, (user_id,))
                connection.commit()
                return cursor.rowcount > 0
            except Error as e:
                print(f"Error deleting Membership: {e}")
                connection.rollback()
            finally:
                cursor.close()
                connection.close()
        return False

    def get_membership_by_user_id(self, user_id: int):
        connection = self.get_db_connection()
        if connection:
            try:
                cursor = connection.cursor(dictionary=True)
                select_query = "SELECT * FROM Membership WHERE UserID = %s"
                cursor.execute(select_query, (user_id,))
                return cursor.fetchone()
            except Error as e:
                print(f"Error fetching Membership by UserID: {e}")
            finally:
                cursor.close()
                connection.close()
        return None


if __name__ == "__main__":
    db_config = {
        'host': 'localhost',
        'user': 'root',
        'password': '0329782205',
        'database': 'ebook'
    }
    test = MembershipModel(db_config)
    result = test.create_membership(7, 'Gold', '2024-05-22', 10)
    print(result)
