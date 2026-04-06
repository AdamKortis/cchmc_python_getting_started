# import module
import pandas as pd
import matplotlib.pyplot as plt

# data file name
# data_file = 'C:\\Users\\KOR9SP\\OneDrive - cchmc\\Documents\\Personal\\ATAL\\cchmc_python_getting_started\\files\\Electric_Vehicle_Population_Data.csv'

# read in file
# df = pd.read_csv(data_file)

# print info
# print(df.shape, end='\n\n') # number of rows and columns

# print(df.columns, end='\n\n') # column names

# print(df.head(5), end='\n\n') # first five rows of data

# print(df.describe(), end='\n\n') # basic dataframe descriptions

# counts and group bys
# print(df.groupby('Make')['VIN (1-10)'].count(), end='\n\n')

# get counts by different group bys using for loop
# group_by_cols = ['Make', 'Model Year', 'Electric Vehicle Type', 'Clean Alternative Fuel Vehicle (CAFV) Eligibility']
# for col_name in group_by_cols:
#     print(df.groupby(col_name)['VIN (1-10)'].count(), end='\n\n')
#     export_file_name = f'C:\\Users\\KOR9SP\\OneDrive - cchmc\\Documents\\Personal\\ATAL\\cchmc_python_getting_started\\files\\{col_name}.csv'
#     df.groupby(col_name)['VIN (1-10)'].count().reset_index().to_csv(export_file_name, index=False)

# create chart
# year_count_df = df.groupby('Model Year')['VIN (1-10)'].count().reset_index()
# categories = year_count_df['Model Year']
# values = year_count_df['VIN (1-10)']
# plt.bar(categories, values, color='blue')
# plt.title('Count of Vehicles by Year')
# plt.xlabel('Year')
# plt.ylabel('Count of Vehicles')
# plt.show()
