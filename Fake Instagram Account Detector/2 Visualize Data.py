# Visualize the number of real and fake accounts
sns.countplot(instaTrain['fake'])

# Display the relationship between every attribute (zoom in to view more clearly), with the instaTrain data
plt.figure(figsize = (20, 20))
sns.pairplot(instaTrain)

# Plot a heatmap showing the correlation between different attributes, with the instaTrain data
plt.figure(figsize=(20, 20))
cm = instaTrain.corr()
ax = plt.subplot()
sns.heatmap(cm, annot = True, ax = ax)
