
import numpy as npy

import re as re
import pandas as pd


#gathered all the route details from each link under a state and concatenated into a single file kerala1.csv and made some cleaning to deeply categorize the ac/nonac, seater/sleeper, private/public in separate columns so that filter can be made easily in streamlit

details = pd.read_csv('kerala1.csv')

bus = pd.DataFrame(details)

unique_bustype = bus['route'].unique()

bus['seats'] = bus['Seats_avail'].str.strip(" Seats available")

bus.rename(columns={'Start':'Departure','End':'Arrival'},inplace=True)

bus['AC/Non AC'] = bus['Type'].apply(
    lambda x: 'AC' if 'A/C' in x.upper() or 'AC' in x.upper() else 'Non AC'
)

# Extract "Sleeper/Seater"
bus['Sleeper/Seater'] = bus['Type'].apply(
    lambda x: 'Sleeper' if 'SLEEPER' in x.upper() else 'Seater'
)

bus['Private/Public'] = bus['Name'].apply(
    lambda x: 'Public' if 'KSRTC' in x.upper() or 'ksrtc' in x.upper() else 'Private'
)

bus[['Pickup', 'Drop']] = bus['route'].str.split('_to_', expand=True)

