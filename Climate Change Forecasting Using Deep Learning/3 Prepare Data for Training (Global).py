# Get the month of recording, to use as a feature
temperature_df['Month'] = temperature_df['dt'].apply(lambda x: int(x.split('-')[1]))

# To get the global average tempeature over years
df_global_monthly = temperature_df.groupby(['dt']).mean().reset_index()

# Function that creates the data for training the time series model
def prepare_data(df, feature_range):
    # Get the columns
    columns = df.columns
    # For the given range, create lagged input feature for the given columns
    for i in range(1, (feature_range + 1)):
        for j in columns[1:]:
            name = j + '_t-' + str(i)
            df[name] = df[j].shift((i))
    # Create the target by using next value as the target
    df['Target'] = df['AverageTemperature'].shift(-1)
    return df

# Get the training data
df_global_monthly = prepare_data(df_global_monthly, 3)

df_global_monthly = df_global_monthly.dropna().reset_index(drop = True)

# Split the data
train = df_global_monthly[:int(0.9 * len(df_global_monthly))].drop(columns = 'dt').values

# Split the data
test = df_global_monthly[int(0.9 * len(df_global_monthly)):].drop(columns = 'dt').values

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
