### Setup

Please first create a .env file in this folder with the following contents: 

```env
RESEARCH_DATA_PATH = "Your Research Data Path"
```

### Excute
```
$ python3 create.py
$ python3 upstream.py
$ python3 downstream.py
```

### Explanation
1. The `create.py` file will read some pre-defined dataset from seaborn library, create a `.csv` data file and a `.ftr` data file. It will also create a sqlite database `database.db`
2. The `upstream.py` file will read the `.csv`/`.ftr` file, and upstream the data into the sqlite database.
3. The `downstream.py` file will retrive the data from sqlite database, and print some interesting statistical information.

