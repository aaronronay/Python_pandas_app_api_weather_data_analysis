import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
import openweathermapy as owm
from citipy import citipy
import seaborn as sns

# Define API key
api_key = "YOUR_API_KEY"

# Generate random latitudes and longitudes
lat_lngs = zip(np.random.uniform(low=-90.000, high=90.000, size=1500),
               np.random.uniform(low=-180.000, high=180.000, size=1500))

# Create a list of unique cities
cities = list(set([citipy.nearest_city(lat, lng).city_name for lat, lng in lat_lngs]))

# Create a settings dictionary for API calls
settings = {"units": "imperial", "appid": api_key}

# Create an empty DataFrame to hold API call data
WeatherPy_df = pd.DataFrame(columns=["City", "Cloudiness", "Country", "Date", "Max Temp", "Wind Speed", "Lat", "Lng", "Humidity"])

# Loop through the cities and make API calls
for index, city in enumerate(cities):
    try:
        city1 = city.replace(" ", "%20")
        city_stats = owm.get_current(city, **settings)
        WeatherPy_df.loc[index] = [city_stats(key) for key in ["name", "clouds.all", "sys.country", "dt",
                                                               "main.temp_max", "wind.speed", "coord.lat",
                                                               "coord.lon", "main.humidity"]]
    except Exception as e:
        print(e)

# Export the data to a CSV file
WeatherPy_df.to_csv("WeatherPy.csv", encoding='utf-8', index=False)

# Display the DataFrame
print(WeatherPy_df.head())
print(WeatherPy_df.count())
print(WeatherPy_df.shape)

# Plotting with common figure size
fig, axes = plt.subplots(2, 2, figsize=(10, 8))
sns.set()

titles = ["City Latitude vs Max Temperature", "City Latitude vs Humidity", "City Latitude vs Cloudiness", "City Latitude vs Wind Speed"]
variables = ["Max Temp", "Humidity", "Cloudiness", "Wind Speed"]
ylabels = ["Max Temperature (F)", "Humidity (%)", "Cloudiness (%)", "Wind Speed (mph)"]
ylimits = [(None, None), (10, WeatherPy_df["Humidity"].max() + 10), (-20, WeatherPy_df["Cloudiness"].max() + 10), (WeatherPy_df["Wind Speed"].min() - 5, WeatherPy_df["Wind Speed"].max() + 5)]

for ax, variable, ylabel, title, ylimit in zip(axes.flat, variables, ylabels, titles, ylimits):
    ax.scatter(WeatherPy_df["Lat"], WeatherPy_df[variable], color='blue', alpha=0.5)
    ax.set(xlabel='Latitude', ylabel=ylabel, title=title, ylim=ylimit)

plt.tight_layout()
plt.show()
