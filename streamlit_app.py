import requests
import numpy as np
import pandas as pd
import streamlit as st
import sqlalchemy
import psycopg2_binary



st.write('Hello world, hello there')

engine = sqlalchemy.create_engine(st.secrets["heroku_uri"], paramstyle="format")
con = engine.raw_connection()
curs = con.cursor()
df_yield = pd.read_sql('SELECT * FROM yield_geo_pred LIMIT 100', con=engine)
st.write(df_yield)


# url = 'https://jsonplaceholder.typicode.com/users'
# data = requests.get(url).json()
# df = pd.DataFrame(data)
# st.write(df)
