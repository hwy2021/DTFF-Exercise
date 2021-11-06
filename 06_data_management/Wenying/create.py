# create.py
import sqlite3
import connect
import feather
import seaborn as sns

databasePath = connect.databasePath
csvDataPath = connect.csvDataPath
featherDataPath = connect.featherDataPath

def init_dataset():
    init_CSV_dataset()
    init_feather_dataset()

def init_CSV_dataset():
    df = sns.load_dataset('flights')
    df.to_csv(csvDataPath, index=False)
    # print('Init CSV File Successful.')

def init_feather_dataset():
    df = sns.load_dataset('tips')
    df.to_feather(featherDataPath)
    # print('Init Feather File Successful.')


# create tables
def create_table():
    cursor, conn = connect.connect_DB()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS flights(
            id INTEGER PRIMARY KEY,
            year INTEGER,
            month INTEGER,
            passengers INTEGER);''')
    # print(f'Create Flight Table Successful at {databasePath}')

    cursor.execute('''
        CREATE TABLE IF NOT EXISTS tips(
            id INTEGER PRIMARY KEY,
            total_bill REAL,
            tip REAL,
            sex VARCHAR(10),
            smoker VARCHAR(6),
            day VARCHAR(5),
            time VARCHAR(10),
            size INTEGER);''')
    # print(f'Create Tips Table Successful at {databasePath}')
    conn.commit()
    conn.close()

def show_database_info():
    cursor, conn = connect.connect_DB()
    print(f'Show tables in: {databasePath}')
    cursor.execute("SELECT name FROM sqlite_master WHERE type='table';")
    print(cursor.fetchall())

    print(f'Show columns in flights table')
    cursor = conn.execute("SELECT * FROM flights")
    columns = list(map(lambda x: x[0], cursor.description))
    print(columns)

    print(f'Show columns in tips table')
    cursor = conn.execute('SELECT * FROM tips')
    columns = list(map(lambda x: x[0], cursor.description))
    print(columns)

    conn.close()


def main():
    init_dataset()
    create_table()
    show_database_info()

if __name__ == '__main__':
    main()