pred, original = prediction(model, test_x, train_x, US_df )

plot(original)

plot_error(pred)
