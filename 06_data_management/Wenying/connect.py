# connect.py
import sqlite3
import os

from dotenv import load_dotenv
load_dotenv()

DATAPATH = os.environ.get("RESEARCH_DATA_PATH")

if not os.path.exists(DATAPATH):
    os.makedirs(DATAPATH)


databasePath = os.path.join(DATAPATH, 'database.db')

csvDataPath = os.path.join(DATAPATH, 'flights.csv')
featherDataPath = os.path.join(DATAPATH, 'tips.feather')

# connect function
def connect_DB():
    conn = sqlite3.connect(databasePath)
    cursor = conn.cursor()
    # print(f'Connect to {databasePath} Successful.')
    return cursor, conn

def main():
    connect_DB()

if __name__ == '__main__':
    main()