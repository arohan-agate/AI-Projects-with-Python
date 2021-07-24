# import key libraries
import pandas as pd
import plotly.express as px
from copy import copy
import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns
from sklearn.model_selection import train_test_split
from sklearn.metrics import r2_score
from sklearn.preprocessing import MinMaxScaler
import tensorflow as tf
from tensorflow import keras
import plotly.offline as py
import plotly.express as px
import plotly.graph_objects as go
import warnings
warnings.filterwarnings('ignore')

# Read the files
temperature_df = pd.read_csv('GlobalLandTemperaturesByCountry.csv')
# dt: Date on which records were observed
# AverageTemperature : Mean temperature of the country 
# AverageTemperatureUncertinity: Uncertainty associated with recorded temperature 
# Country: Country name

display(temperature_df)
