# Statistical data of the dataframe
covid_df.describe()

# Sort the dataframe by Date
covid_df = covid_df.sort_values(by = 'Date')


# Print the name of Countries
print('Countries on which have data are:\n')

for i in covid_df['Entity'].unique():
      print(i)
