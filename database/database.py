import sqlite3


def recording_data_of_users_who_launched_the_bot(user_id, username, first_name, last_name, join_date):
    """Запись данных пользователей запустивших бота"""
    conn = sqlite3.connect("your_database.db")  # Замените "your_database.db" на имя вашей базы данных
    cursor = conn.cursor()
    cursor.execute('''CREATE TABLE IF NOT EXISTS users_start (
                        user_id INTEGER PRIMARY KEY,
                        username TEXT,
                        first_name TEXT,
                        last_name TEXT,
                        join_date TEXT)''')
    cursor.execute("INSERT OR REPLACE INTO users_start (user_id, username, first_name, last_name, join_date) "
                   "VALUES (?, ?, ?, ?, ?)", (user_id, username, first_name, last_name, join_date))
    conn.commit()
    conn.close()


if __name__ == '__main__':
    recording_data_of_users_who_launched_the_bot()
