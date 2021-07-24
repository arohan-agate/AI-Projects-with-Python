# We are going to do the modeling for US data
US_df = temperature_df[temperature_df['Country'] == 'United States'].reset_index(drop = True)

US_df = US_df.drop(['Country', 'year'], axis = 1)

# Get the training data
US_df = prepare_data(US_df, 3)

US_df = US_df.dropna().reset_index(drop = True)

# Split the data
train = US_df[:int(0.9 * len(US_df))].drop(columns = 'dt').values

# Split the data
test = US_df[int(0.9 * len(US_df)):].drop(columns = 'dt').values

# Scale the data
scaler = MinMaxScaler(feature_range = (0, 1))
train  = scaler.fit_transform(train)
test   = scaler.transform(test)


# Split the data into input features and targets
train_x, train_y = train[:,:-1], train[:,-1]
test_x, test_y = test[:,:-1], test[:,-1]

# reshape input to be 3D [samples, timesteps, features]
train_x = train_x.reshape((train_x.shape[0], 1, train_x.shape[1]))
test_x = test_x.reshape((test_x.shape[0], 1, test_x.shape[1]))
