import pandas as pd
from sqlalchemy import create_engine

engine = create_engine("sqlite:///database.db", pool_recycle=3600, echo=True)

with engine.connect() as conn:
    data = pd.read_sql_table("kline_data", conn, columns=["timestamp", "volume", "open", "high", "low", "close"])
    data = data.drop_duplicates(subset=['timestamp'], keep='first')
    data.to_csv("SZ000625_10year.csv")