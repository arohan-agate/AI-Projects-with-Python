m = Prophet()

# Create and fit the prophet model to the training data
m.fit(train)

# get the dataframe containing dates which includes our training dates as well as 31 days into the future, for forecasting.
future = m.make_future_dataframe(periods = 31)

# Make prediction 
forecast = m.predict(future)

# 'yhat' is the mean predicted values and the 'yhat_lower' and 'yhat_upper' represent the lower and upper predicted boundaries
forecast[['ds', 'yhat', 'yhat_lower', 'yhat_upper']].tail()



from fbprophet.plot import plot_plotly, plot_components_plotly

# Ploting the forecasted data. The black line indicates the training data (the past), the blue line indicates the testing data (the prediction for the future)
plot_plotly(m, forecast)


from fbprophet.plot import add_changepoints_to_plot

# This particular feature helps us identify trend changes that are infered by the model
fig = m.plot(forecast)
a = add_changepoints_to_plot(fig.gca(), m, forecast)
