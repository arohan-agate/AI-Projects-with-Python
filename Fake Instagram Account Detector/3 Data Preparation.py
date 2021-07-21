# Training and testing dataset (inputs)
X_train = instaTrain.drop(columns = ['fake'])
X_test = instaTest.drop(columns = ['fake'])

# Training and testing dataset (Outputs)
y_train = instaTrain['fake']
y_test = instaTest['fake']


# Scale the data before training the model
from sklearn.preprocessing import StandardScaler, MinMaxScaler

scaler_x = StandardScaler()
X_train = scaler_x.fit_transform(X_train)
X_test = scaler_x.transform(X_test)

y_train = tf.keras.utils.to_categorical(y_train, num_classes = 2)
y_test = tf.keras.utils.to_categorical(y_test, num_classes = 2)
