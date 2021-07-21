# Getting dataframe info
instaTrain.info()

# Get the statistical summary of the dataframe
instaTrain.describe()

# Get the number of unique values in "fake" (Target column) for instaTrain
instaTrain['fake'].value_counts()


# Getting DF info with instaTest
instaTest.info()

# Get the statistical summary of instaTest
instaTest.describe()

# Get the number of unique values in "fake" (Target column) for instaTest
instaTest['fake'].value_counts()
