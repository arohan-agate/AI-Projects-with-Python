model = create_model(train_x)

# fit the network
history = model.fit(train_x, train_y, epochs = 50, batch_size = 72, validation_data = (test_x, test_y), shuffle = False)

plot_history(history)
