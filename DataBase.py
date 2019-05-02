import sqlite3

class DB:
    def __init__(self):
        self.conn =  sqlite3.connect('exchange.db')
        self.cur = self.conn.cursor()
        self.cur.execute( '''CREATE TABLE IF NOT EXISTS exchange (id integer primary key, Currency text, Buy real, Sell real, High real)''')
        self.conn.commit()

    def insert_data(self, currency, buy, sell, high):
        self.cur.execute('''INSERT INTO exchange (currency, buy, sell, high) VALUES (?, ?, ?, ?)''', (currency, buy, sell, high))
        self.conn.commit()
