import matplotlib.pyplot as plt
from pandas_datareader.data import DataReader
from datetime import date, timedelta

# Step 1: Download Data 
start = date.today() - timedelta(weeks = 1)

series = ['DGS1MO', 'DGS3MO', 'DGS6MO', 'DGS1', 'DGS2', 'DGS3', 'DGS5', 'DGS7', 'DGS10', 'DGS20', 'DGS30']

df = DataReader(series, 'fred', start)

# Step 2: Data Processing
df = df.dropna()

labels = {
    'DGS1MO': '1 Month',
    'DGS3MO': '3 Months',
    'DGS6MO': '6 Months',
    'DGS1': '1 Year',
    'DGS2': '2 Years',
    'DGS3': '3 Years',
    'DGS5': '5 Years',
    'DGS7': '7 Years',
    'DGS10': '10 Years',
    'DGS20': '20 Years',
    'DGS30': '30 Years'
}

most_recent = df.iloc[-1]

most_recent.index = [labels[label] for label in most_recent.index]

# Step 3: Plotting the Yield Curve
plt.figure(figsize=(10, 6))
plt.plot(most_recent, marker='o')
plt.title('U.S. Treasury Yield Curve')
plt.xlabel('Maturity')
plt.ylabel('Yield (%)')
plt.grid(True)
plt.show()