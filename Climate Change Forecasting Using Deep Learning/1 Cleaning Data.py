# Do groupby country to see the count of values available for each country
country_group_df = temperature_df.groupby(by = 'Country').count().reset_index('Country').rename(columns={'AverageTemperature':'AverageTemperatureCount','AverageTemperatureUncertainty' : 'AverageTemperatureUncertaintyCount'})

country_group_df['Country']

import plotly.express as px
fig = px.bar(country_group_df, x = 'Country', y = 'AverageTemperatureCount')
fig.show()

fig = px.bar(country_group_df, x = 'Country', y = 'AverageTemperatureUncertaintyCount')
fig.show()

country_group_df[(country_group_df['AverageTemperatureCount'] < 1500) | (country_group_df['AverageTemperatureUncertaintyCount'] < 1500)]

# Find the countries that have less than 1500 data points
countries_with_less_data = country_group_df[(country_group_df['AverageTemperatureCount'] < 1500) | (country_group_df['AverageTemperatureUncertaintyCount'] < 1500)]['Country'].tolist()

# Remove the countries with less data points
temperature_df = temperature_df[~temperature_df['Country'].isin(countries_with_less_data)]

# Reset the index
temperature_df.reset_index(inplace = True, drop = True)

# Fill the missing values by doing rolling average on past 730 days
temperature_df['AverageTemperature'] = temperature_df['AverageTemperature'].fillna(temperature_df['AverageTemperature'].rolling(730, min_periods = 1).mean())

# Fill the missing values by doing rolling average on past 730 days
temperature_df['AverageTemperatureUncertainty']= temperature_df['AverageTemperatureUncertainty'].fillna(temperature_df['AverageTemperatureUncertainty'].rolling(730, min_periods=1).mean())

# Check for the presence of other version of same country
duplicates = []
for i in temperature_df['Country'].unique():
    if '(' in i:
        duplicates.append(i)

# replace the duplicates
temperature_df = temperature_df.replace(duplicates, ['Congo', 'Denmark','Falkland Islands','France','Netherlands','United Kingdom'])
