import sqlite3
import pandas as pd

class DatabaseManager:
    def __init__(self, db_name):
        self.db_name = db_name

    def has_data(self):
        cursor = self.connect().cursor()
        cursor.execute("SELECT COUNT(*) FROM test_data")
        count = cursor.fetchone()[0]
        return count > 0

    def connect(self):
        return sqlite3.connect(self.db_name)

    def load_data(self):
        conn = self.connect()
        df = pd.read_sql_query('SELECT * FROM test_data', conn)
        df['test_date'] = pd.to_datetime(df['test_date'])
        df = df.sort_values(by='test_date')
        conn.close()
        return df

    def create_table(self):
        conn = self.connect()
        c = conn.cursor()
        c.execute('''
            CREATE TABLE IF NOT EXISTS test_data (
                test_id INTEGER PRIMARY KEY,
                test_date TEXT,
                vehicle_id TEXT,
                average_speed REAL,
                following_distance REAL,
                lane_keeping_accuracy REAL,
                human_inputs INTEGER,
                distance_travelled REAL,
                result TEXT
            )
        ''')
        conn.commit()
        conn.close()

    def insert_data(self, data):
        conn = self.connect()
        c = conn.cursor()
        c.executemany('''
            INSERT INTO test_data (test_date, vehicle_id, average_speed, following_distance, lane_keeping_accuracy, human_inputs, distance_travelled, result)
            VALUES (?, ?, ?, ?, ?, ?, ?, ?)
        ''', data)
        conn.commit()
        conn.close()