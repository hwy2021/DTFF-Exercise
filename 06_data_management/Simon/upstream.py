# upstream.py




from connect import DATAPATH



def put_data():
  """Store data to the DB."""

  data = "upstream test"

  filename = DATAPATH + "upstream.csv"

  data.to_csv(filename)
