import pandas as pd
import matplotlib.pyplot as plt
from sqlalchemy import create_engine

def create_conn():
    engine = create_engine('mysql+pymysql://root:Esoteric90@!@localhost/sakila') 
    return engine.connect()
     