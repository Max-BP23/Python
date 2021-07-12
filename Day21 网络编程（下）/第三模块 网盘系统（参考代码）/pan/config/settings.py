import os

base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

HOST = "127.0.0.1"
PORT = 9000

DB_FILE_PATH = os.path.join(base_dir, 'db', 'users.xlsx')
USER_FOLDER_PATH = os.path.join(base_dir, 'files')
