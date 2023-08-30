import pandas as pd
import matplotlib.pyplot as plt
from sqlalchemy import create_engine

def create_conn():
    engine = create_engine('mysql+pymysql://root:Esoteric90@!@localhost:3377/sakila') 
    return engine.connect()

def run_query(query);
conn = create_conn()
df = pd.read_sql_query(query,conn)
conn.close()
return df
     