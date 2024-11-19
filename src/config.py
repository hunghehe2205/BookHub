import os
from dotenv import load_dotenv

# Load environment variables from a .env file
load_dotenv()


class Config:
    # Database Configuration
    DB_HOST = os.getenv('DB_HOST', 'localhost')
    DB_PORT = os.getenv('DB PORT', '3306')
    DB_USER = os.getenv('DB_USER', 'root')
    DB_PASSWORD = os.getenv('DB_PASSWORD', '0329782205')
    DB_NAME = os.getenv('DB_NAME', 'ebook')

    @staticmethod
    def get_db_config():
        return {
            'host': Config.DB_HOST,
            'port': Config.DB_PORT,
            'user': Config.DB_USER,
            'password': Config.DB_PASSWORD,
            'database': Config.DB_NAME
        }
