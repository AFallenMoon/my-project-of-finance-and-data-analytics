import pandas as pd
from pandas_datareader.data import DataReader

# Step 1: Read Data
sp500_list = pd.read_csv('sp500_df.csv')

pe = pd.read_excel('pe_ratios_df.xlsx')

#Step 2: Data Processing & Report Output
data_comb = sp500_list.merge(pe, left_on = 'Symbol', right_on = 'Ticker')

mean_pe_sp500 = data_comb['Trailing PE Ratio'].mean()

print('Average PE ratio for the entire S&P 500 index: ')
print(mean_pe_sp500)

data_group = data_comb.groupby('GICS Sector')

mean_pe_by_sector = data_group['Trailing PE Ratio'].mean()

print('\nAverage PE ratio for each industry: ')
print(mean_pe_by_sector)

top_3_highest_industries = mean_pe_by_sector.nlargest(3)

print('\nTop 3 highest industries by average PE ratio: ')
print(top_3_highest_industries)

top_3_lowest_industries = mean_pe_by_sector.nsmallest(3)

print('\nTop 3 lowest industries by average PE ratio: ')
print(top_3_lowest_industries)

top_3_highest_firms_by_sector = data_group.apply(lambda x: x.nlargest(3, 'Trailing PE Ratio')[['Symbol', 'Trailing PE Ratio']]).reset_index(level=1, drop=True)

print('\nTop 3 firms with highest PE ratios within each industry: ')
print(top_3_highest_firms_by_sector)

top_3_lowest_firms_by_sector = data_group.apply(lambda x: x.nsmallest(3, 'Trailing PE Ratio')[['Symbol', 'Trailing PE Ratio']]).reset_index(level=1, drop=True)

print('\nTop 3 firms with lowest PE ratios within each industry: ')
print(top_3_lowest_firms_by_sector)