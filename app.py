import streamlit as st
from sensor_simulation import read_sensor

st.title("Smart & Sustainable Agriculture System")

soil, temp, hum = read_sensor()

st.write("Soil Moisture:", soil)
st.write("Temperature:", temp)
st.write("Humidity:", hum)

if soil < 30:
    st.warning("Irrigation Required")
else:
    st.success("Soil Moisture OK")