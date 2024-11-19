import mysql.connector
from mysql.connector import Error
from datetime import date


class BookModel:
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

    def create_book(self, title: str,
                    author: str,
                    publication_date: date,
                    release_date: date,
                    rating: float = 0):
        connection = self.get_db_connection()
        if connection:
            try:
                cursor = connection.cursor()
                # Corrected the number of placeholders in the query to match the provided values
                insert_query = "INSERT INTO Book (Title, Author, PublicationDate, Rating, ReleaseDate) VALUES (%s, %s, %s, %s, %s)"
                cursor.execute(insert_query, (title, author,
                               publication_date, rating, release_date))
                connection.commit()
                return cursor.lastrowid
            except Error as e:
                print(f"Error creating book: {e}")
                connection.rollback()
            finally:
                cursor.close()
                connection.close()
        return None

    def get_book_by_id(self, book_id: int):
        connection = self.get_db_connection()
        if connection:
            try:
                cursor = connection.cursor(dictionary=True)
                select_query = "SELECT * FROM Book WHERE BookID = %s"
                cursor.execute(select_query, (book_id,))
                return cursor.fetchone()
            except Error as e:
                print(f"Error fetching book by ID: {e}")
            finally:
                cursor.close()
                connection.close()
        return None

    def get_book_by_title(self, book_title: str):
        connection = self.get_db_connection()
        if connection:
            try:
                cursor = connection.cursor(dictionary=True)
                select_query = "SELECT * FROM Book WHERE Title = %s"
                cursor.execute(select_query, (book_title,))
                return cursor.fetchone()
            except Error as e:
                print(f"Error fetching Book by title: {e}")
            finally:
                cursor.close()
                connection.close()
        return None

    def update_book(self, book_id: int,
                    title: str = None,
                    author: str = None,
                    publication_date: date = None,
                    rating: float = None,
                    release_date: date = None):
        connection = self.get_db_connection()
        if connection:
            try:
                cursor = connection.cursor()
                update_query = "UPDATE Book SET "
                fields = []
                values = []
                if title:
                    fields.append("Title = %s")
                    values.append(title)
                if author:
                    fields.append("Author = %s")
                    values.append(author)
                if publication_date:
                    fields.append("PublicationDate = %s")
                    values.append(publication_date)
                if rating is not None:
                    fields.append("Rating = %s")
                    values.append(rating)
                if release_date:
                    fields.append("ReleaseDate = %s")
                    values.append(release_date)
                values.append(book_id)
                if fields:
                    update_query += ", ".join(fields) + " WHERE BookID = %s"
                    cursor.execute(update_query, tuple(values))
                    connection.commit()
                    return cursor.rowcount > 0
            except Error as e:
                print(f"Error updating Book: {e}")
                connection.rollback()
            finally:
                cursor.close()
                connection.close()
        return False

    def delete_book(self, book_id: int):
        connection = self.get_db_connection()
        if connection:
            try:
                cursor = connection.cursor()
                delete_query = "DELETE FROM Book WHERE BookID = %s"
                cursor.execute(delete_query, (book_id,))
                connection.commit()
                return cursor.rowcount > 0
            except Error as e:
                print(f"Error deleting Book: {e}")
                connection.rollback()
            finally:
                cursor.close()
                connection.close()
        return False


if __name__ == "__main__":
    db_config = {
        'host': 'localhost',
        'user': 'root',
        'password': '0329782205',
        'database': 'ebook'
    }
    test = BookModel(db_config)
    result = test.update_book(13, rating=1.7)
    print(result)
