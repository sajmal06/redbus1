
import pandas as pd
# import matplotlib.pyplot as plt
# from openpyxl import Workbook
# from openpyxl import load_workbook
import numpy as npy
import busapp2 as st
import re as re
from datacleaning import bus
import streamlit as st


# import numpy as np

st.title("Bus Filtering App")


typeAc = bus['AC/Non AC'].unique().tolist()
seating = bus['Sleeper/Seater'].unique().tolist()
busname = bus['Private/Public'].unique().tolist()
pickup = bus['Pickup'].unique()
drop = bus['Drop'].unique()
pickuppoint = st.selectbox("From",pickup)
droppoint = st.selectbox("To",drop)
search = st.button("Search")
searched = bus[
    (bus['Pickup'] == pickuppoint) &
    (bus['Drop'] == droppoint)]

with st.sidebar:
    st.write("Select Filters...")
    rate = st.selectbox("Select Rating", options=[4,3,2,1])
    Filter1 = st.selectbox("Select AC/Non AC", options= ["Select an option"] + typeAc, ) 
    Filter2 = st.selectbox("Select Seating Type",["Select an option"] + seating ) 
    Filter3 = st.selectbox("Select bus Type",["Select an option"] + busname ) 
    apply = st.button("Apply")

filtered_bus = bus[
    (bus['AC/Non AC'] == Filter1) &
    (bus['Sleeper/Seater'] == Filter2) &
    (bus['Private/Public'] == Filter3) &
    (bus['Pickup'] == pickuppoint) &
    (bus['Drop'] == droppoint)&
    (bus['Rating'] >= rate)]




if apply:
  st.write("Filtered Results:")
  st.dataframe(filtered_bus)
elif search:
  st.dataframe(searched)  
else:
  st.dataframe(bus)




