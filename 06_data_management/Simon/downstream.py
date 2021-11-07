# downstream.py
import pandas as pd
from connect import DATAPATH

def get_data():

  filename = DATAPATH + "toybase.csv"

  data = pd.read_csv(filename)

  return data