# Access the performance of the model
score = r2_score(test['y'], forecast[forecast['ds'] >= '2020-10-01']['trend'])

print('R-Sqaure score is {}'.format(score))

# Add the predicted values to the original dataframe for plotting purpose
US_df['predicted'] = forecast['trend']

display(US_df)


# Function to plot the forecast and the origianl values for comparison
def i_plot_forecasting(df, title):
    fig = px.line(title = title)
    for i in df.columns[1:]:
        fig.add_scatter(x = df['ds'],y = df[i], name = i)
    fig.show()
i_plot_forecasting(US_df, 'Original Vs Predicted')
