# Import Libraries
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import statistics as sts

# Making data frame from csv file
df = pd.read_csv('Dev1Hotfire_60lpf_1.csv')

# Dropping Digital Read on/off
df.drop(['Digital_Read_on/off'], axis=1, inplace=True)

# Calculated Values
df['Chamber_Pressure_psia'] = df['Chamber_Pressure_psia']*125/8*10-62.78
df['Feed_Pressure_psia'] = df['Feed_Pressure_psia']*-37717+12.715

# Plot Data
df.plot(figsize=(12, 6), x='Time_s')
y2 = df.secondary_yaxis('Chamber_Temperature_C')
plt.show()

# Removing Outliers
values = np.array(df['Chamber_Pressure_psia'].describe())
meanCP = values[1]
q1CP = values[4]
min = meanCP-q1CP
df.loc[df['Chamber_Pressure_psia'] <= min, 'Chamber_Pressure_psia'] = ''
x = df['Chamber_Pressure_psia']


# Mean of New Chamber Pressure Data
newmeanCP = sts.mean(x)
print(newmeanCP)