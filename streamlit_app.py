import requests
import numpy as np
import pandas as pd
import streamlit as st

st.write('Hello world, hello there')

# conn = st.connection("postgresql", type="sql")
# df = conn.query('SELECT * FROM test3 LIMIT 10;', ttl="10m")   #query results is cached no longer than 10 minutes
# st.write(df)

# url = 'https://jsonplaceholder.typicode.com/users'
# data = requests.get(url).json()
# df = pd.DataFrame(data)
# st.write(df)

params = {
    "q": "London,uk",
    "APPID": st.secrets["OpenWeatherAppId"]
}
url = 'https://api.openweathermap.org/data/2.5/weather'
response = requests.get(url, params=params)
data = response.json()
st.write("Temperature:", data["main"]["temp"], "K")