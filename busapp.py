
import pandas as pd
# import matplotlib.pyplot as plt
# from openpyxl import Workbook
# from openpyxl import load_workbook
import numpy as npy
import streamlit as st
import re as re
from datacleaning import bus

# import numpy as np

st.title("Bus Filtering App")

 


with st.sidebar:
# Sidebar filters
 
 filter1 = st.radio("Select AC/Non AC",   options=bus['AC/Non AC'].unique())
 filter2 = st.radio("Select Sleeper/Seater", options=bus['Sleeper/Seater'].unique())
 filter3 = st.radio("Select Private/Public", options=bus['Private/Public'].unique())
 pickuppoint = st.selectbox("Select Pickup Point", options=bus['Pickup'].unique())
 droppoint = st.selectbox("Select Drop Point", options=bus['Drop'].unique())
 rate = st.selectbox("Select Rating", options=[1,2,3,4])
 apply = st.button("Apply")
 filtered_bus = bus[
    (bus['AC/Non AC'] == filter1) &
    (bus['Sleeper/Seater'] == filter2) &
    (bus['Private/Public'] == filter3) &
    (bus['Pickup'] == pickuppoint) &
    (bus['Drop'] == droppoint) &
    (bus['Rating'] >= rate)]
# Apply filtering
if apply:
  st.write("Filtered Results:")
  st.dataframe(filtered_bus)
else:
  st.dataframe(bus)
  

# Display the filtered DataFrame






