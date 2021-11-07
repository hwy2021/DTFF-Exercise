# downstream.py
import pandas as pd
import connect

databasePath = connect.databasePath
csvDataPath = connect.csvDataPath
featherDataPath = connect.featherDataPath

'''
Flight data:
    ID: int
    year: int
    month: int
    passengers: int
'''
def get_flight_info(year):
    cursor, conn = connect.connect_DB()
    cursor = conn.execute("SELECT * FROM flights WHERE year = ?", (year,))
    rows = cursor.fetchall()
    flightsNumber = len(rows)
    passangersNumber = sum(map(lambda x: x[3], rows))
    print(f'In year {year}, there are {flightsNumber} of flights and {passangersNumber} of passangers.')
    conn.close()

'''
Tip data:
    ID: int
    total_bill: float
    tip: float
    sex: str
    smoker: str
    day: str
    time: str
    size: int
'''
def get_tips(slot):
    assert(slot == 'Dinner' or slot == 'Lunch')
    cursor, conn = connect.connect_DB()
    cursor = conn.execute(f"SELECT * FROM tips WHERE time = ?", (slot,))
    rows = cursor.fetchall()
    customersNumber = len(rows)
    totalBill = sum(map(lambda x: x[1], rows))
    totalTip = sum(map(lambda x: x[2], rows))
    tipRate = totalTip / totalBill
    print(f'There are {customersNumber} customers in {slot}, with total bill of {totalBill:.2f}, total tip of {totalTip:.2f}, average tip rate {tipRate*100:.2f}%.')
    conn.close()

# API for flight data
def get_flight_data():
    cursor, conn = connect.connect_DB()
    cursor = conn.execute("SELECT * FROM flights")
    rows = cursor.fetchall()
    conn.close()
    return rows

def main():
    get_flight_info(1955)
    get_flight_info(1956)
    get_tips('Lunch')
    get_tips('Dinner')

if __name__ == '__main__':
    main()