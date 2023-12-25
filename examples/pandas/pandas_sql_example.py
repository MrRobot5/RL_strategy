"""
使用 pandas 操作数据库
pip install pandas==1.2.5

Database abstraction is provided by SQLAlchemy if installed.
pip install sqlalchemy==1.4.46

MySQL client library for Python
pip install PyMySQL==1.0.1

@see https://pandas.pydata.org/docs/user_guide/io.html#io-sql
@since 2023年12月7日11:00:59
"""
import pandas as pd
import datetime
import sqlalchemy as sa
from sqlalchemy import create_engine

# Create your engine.
# To connect with SQLAlchemy you use the create_engine() function to create an engine object from database URI.
engine = create_engine("mysql+pymysql://root:mysql@localhost/test", pool_recycle=3600, echo=True)


def read_table():
    """
    Once established, the newly resulting Engine will request a connection from the underlying Pool once Engine.connect() is called
    :return:
    """
    with engine.connect() as conn:
        data = pd.read_sql_table("data", conn, columns=["Col_1", "Col_2"])
        print(data)


def query_table():
    """
    query using raw SQL

    :return:
    """
    with engine.connect() as conn:
        data = pd.read_sql_query("select * from data where id = 26", conn)
        print(data)

    # or
    data = pd.read_sql_query("SELECT * FROM data where id = 26", engine)
    print(data)

    #or
    data = pd.read_sql(
        sa.text("SELECT * FROM data where Col_1=:col1"), engine, params={"col1": "X"}
    )
    print(data)


def insert_data():
    """
    Write records stored in a DataFrame to a SQL database.
    如果 table 不存在，则 create table.🎈
    """
    c = ["id", "Date", "Col_1", "Col_2", "Col_3"]
    d = [
        (26, datetime.datetime(2010, 10, 18), "X", 27.5, True),
        (42, datetime.datetime(2010, 10, 19), "Y", -12.5, False),
        (63, datetime.datetime(2010, 10, 20), "Z", 5.73, True),
    ]
    data = pd.DataFrame(d, columns=c)
    # if_exists{‘fail’, ‘replace’, ‘append’}, default ‘fail’
    data.to_sql("data", con=engine, if_exists="append")


if __name__ == '__main__':
    # insert_data()
    # read_table()
    query_table()
