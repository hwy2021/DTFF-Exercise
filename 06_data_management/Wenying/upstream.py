# upstream.py
import pandas as pd
import connect
import feather

databasePath = connect.databasePath
csvDataPath = connect.csvDataPath
featherDataPath = connect.featherDataPath


def get_rows_number(tableName):
    cursor, conn = connect.connect_DB()
    cursor.execute(f'SELECT COUNT(*) FROM {tableName}')
    rowsNumber = cursor.fetchone()[0]
    conn.close()
    return rowsNumber

# Read data from csv file
def read_from_CSV(filePath):
    df = pd.read_csv(filePath)
    return df

# Read data from Feather file
def read_from_feather(filePath):
    df = pd.read_feather(filePath)
    return df

def upstream_CSV_to_sqlite():
    rowsNumber = get_rows_number('flights')
    if rowsNumber > 0:
        print(f'{rowsNumber} rows in flights table.')
        return

    cursor, conn = connect.connect_DB()
    df = read_from_CSV(csvDataPath)
    for row in df.itertuples():
        cursor.execute('''
            INSERT INTO flights(year, month, passengers)
            VALUES(?, ?, ?)''', (row.year, row.month, row.passengers))
    conn.commit()
    conn.close()

def upstream_feather_to_sqlite():
    rowsNumber = get_rows_number('tips')
    if rowsNumber > 0:
        print(f'{rowsNumber} rows in tips table.')
        return
    
    cursor, conn = connect.connect_DB()
    df = read_from_feather(featherDataPath)
    for row in df.itertuples():
        cursor.execute('''
            INSERT INTO tips(total_bill, tip, sex, smoker, day, time, size)
            VALUES(?, ?, ?, ?, ?, ?, ?)''', (row.total_bill, row.tip, row.sex, row.smoker, row.day, row.time, row.size))
    conn.commit()
    conn.close()


def main():
    upstream_CSV_to_sqlite()
    upstream_feather_to_sqlite()

if __name__ == '__main__':
    main()