countries = temperature_df['Country'].unique().tolist()

# Get the mean temperature for each country
mean_temperature = []
for i in countries:
    mean_temperature.append(temperature_df[temperature_df['Country'] == i]['AverageTemperature'].mean())

# Plot the mean teamperature of countries
data = [ dict(type = 'choropleth', # type of map
              locations = countries, # location names
              z = mean_temperature, # temperature of countries
              locationmode = 'country names')
       ]

layout = dict(title = 'Average Global Land Temperatures',
              geo = dict(showframe = False,
                         showocean = True, # to show the ocean
                         oceancolor = 'aqua',
                         projection = dict(type = 'orthographic'))) # to get the globe view),

fig = dict(data = data, layout = layout)
py.iplot(fig, validate = False, filename = 'worldmap')

# Get the year of recorded data, for visualization purpose
temperature_df['year'] = temperature_df['dt'].apply(lambda x: x.split('-')[0])

# To create the animation to see the global temperature change
fig = px.choropleth(temperature_df, locations = 'Country',
                    locationmode = 'country names', # locations 
                    color = 'AverageTemperature', # column representing the temperature
                    hover_name = "Country", # column to add to hover information
                    animation_frame = 'year', # timeframe for animation
                    color_continuous_scale = px.colors.sequential.deep_r)
# py.plot(fig)
fig.show()

# To get the global average tempeature over years
df_global = temperature_df.groupby('year').mean().reset_index()

# Convert the year to int type and use the data above 1850 for visualization (Before this most of the countries do not have recorded reading)
df_global['year'] = df_global['year'].apply(lambda x: int(x))
df_global = df_global[df_global['year'] > 1850]

# Uncertainity upper bound 
trace1 = go.Scatter(
    x = df_global['year'], 
    y = np.array(df_global['AverageTemperature']) + np.array(df_global['AverageTemperatureUncertainty']), # Adding uncertinity
    name = 'Uncertainty top',
    line = dict(color = 'green'))

# Uncertainity lower bound
trace2 = go.Scatter(
    x = df_global['year'] , 
    y = np.array(df_global['AverageTemperature']) - np.array(df_global['AverageTemperatureUncertainty']), # Subtracting uncertinity
    fill = 'tonexty',
    name = 'Uncertainty bottom',
    line = dict(color = 'green'))

# Recorded temperature
trace3 = go.Scatter(
    x = df_global['year'] , 
    y = df_global['AverageTemperature'],
    name = 'Average Temperature',
    line = dict(color='red'))
data = [trace1, trace2, trace3]

layout = go.Layout(
    xaxis = dict(title = 'year'),
    yaxis = dict(title = 'Average Temperature, °C'),
    title = 'Average Land Temperatures Globally',
    showlegend = False)

fig = go.Figure(data = data, layout = layout)
py.iplot(fig)

# Model for US data
US_df = temperature_df[temperature_df['Country'] == 'United States'].reset_index(drop = True)
fig = px.line(title = 'US Temperature Data')
US_df_updated = US_df[US_df['year'] > '1813']
fig.add_scatter(x = US_df_updated['dt'], y = US_df_updated['AverageTemperature'], name = 'US Temperature')
fig.show()
