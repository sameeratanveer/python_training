import pandas as pd
import numpy as np
flights = pd.DataFrame({
    'flight_id': [101, 102, 103, 104, 105],
    'source': ['DEL', 'BOM', 'BLR', 'DEL', 'BOM'],
    'destination': ['BOM', 'DEL', 'DEL', 'BLR', 'BLR'],
    'delay_mins': [30, -5, 0, 120, None]
})

# print(flights)
# 1. Replace negative delay with 0 (since it means early arrival.
flights['delay_mins'] = np.where(flights['delay_mins']<0, 0, flights['delay_mins'])
# print(flights)

# 2. Fill missing values with average delay per source airport.
flights['delay_mins'] = flights['delay_mins'].transform(lambda x: x.fillna(x.mean()))
# print(flights)

''' 3.
Categorize flights into:
'On Time' if delay ≤ 15
'Delayed' if delay > 15
'''
flights['categorize_flights'] = np.where(flights['delay_mins']>15, 'Delayed', 'On Time')
# print(flights)

'''
4. 
For each source, calculate:
total number of flights
percentage of delayed flights
'''
source_details = flights.groupby('source').value_counts()
print(source_details)