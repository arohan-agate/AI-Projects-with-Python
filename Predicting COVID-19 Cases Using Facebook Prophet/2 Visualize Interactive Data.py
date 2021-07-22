# Function to plot interative plot plot
def i_plot(df, column_name, title):
    fig = px.line(title = title)
    for i in df['Entity'].unique():
        d = df[df['Entity'] == i]
        fig.add_scatter(x = d['Date'], y = d[column_name], name = i)
    fig.show()

    
# Covid cases animation from January 2020 to November 2020
fig = px.choropleth(covid_df, locations = 'iso_alpha', color = 'Cases', animation_frame = 'month', title = 'COVID-19 cases animation from January 2020 to November 2020')
fig.show()


# Covid deaths animation from January 2020 to November 2020
fig = px.choropleth(covid_df, locations = "iso_alpha", # locations iso code
                    color = 'Deaths', # column representing the color itensity
                    hover_name = "Entity", # column to add to hover information
                    animation_frame = 'month', # timeframe for animation
                    title = 'COVID-19 deaths animation from January 2020 to November 2020')
fig.show()


# Covid testing animation from January 2020 to November 2020
fig = px.choropleth(covid_df, locations = "iso_alpha", # locations iso code
                    color = 'Daily tests', # column representing the color itensity
                    hover_name = "Entity", # column to add to hover information
                    animation_frame = 'month', # timeframe for animation
                    title = 'COVID-19 testing animation from January 2020 to November 2020')
fig.show()
