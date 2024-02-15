import requests
import numpy as np
import pandas as pd
import streamlit as st
# import sqlalchemy
# import psycopg_binary

# see https://docs.streamlit.io/knowledge-base/tutorials/databases/postgresql

st.write('Hello world, hello there')

conn = st.connection("postgresql", type="sql")
df = conn.query('SELECT * FROM test3 LIMIT 10;', ttl="10m")   #query results is cached no longer than 10 minutes
st.write(df)

# engine = sqlalchemy.create_engine(st.secrets["heroku_uri"], paramstyle="format")
# con = engine.raw_connection()
# curs = con.cursor()
# df_yield = pd.read_sql('SELECT * FROM test3 LIMIT 10', con=engine)
# con.close()
# st.write(df_yield)


# url = 'https://jsonplaceholder.typicode.com/users'
# data = requests.get(url).json()
# df = pd.DataFrame(data)
# st.write(df)
