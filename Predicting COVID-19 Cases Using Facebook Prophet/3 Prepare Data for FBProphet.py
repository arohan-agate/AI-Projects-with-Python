# Get the data corresponding to the United States only
US_df = covid_df[covid_df['Entity'] == 'United States']

# Only obtain the date and cases columns
US_df = US_df[['Date', 'Cases']]

# reset index
US_df.reset_index(inplace=True, drop=True)
display(US_df)

# These are the column names expected by fbprophet
US_df.columns = ['ds', 'y']

# Split the data into testing and training datasets
train , test = US_df[ US_df['ds'] <= '2020-09-30'], US_df[US_df['ds'] >=  '2020-10-01']
