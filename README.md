# WeatherPy

This Python script generates random latitudes and longitudes, retrieves weather data for corresponding cities using the OpenWeatherMap API, and performs visual analysis on the data.

## Prerequisites

To run this script, you need to have the following libraries installed:

- matplotlib
- pandas
- numpy
- openweathermapy
- citipy
- seaborn

You also need to obtain an API key from OpenWeatherMap. Replace "YOUR_API_KEY" with your actual API key in the code.

## Installation

1. Clone the repository:

git clone https://github.com/your_username/WeatherPy.git


2. Navigate to the project directory:

cd WeatherPy


3. Install the required libraries:

pip install -r requirements.txt


4. Run the script:
python WeatherPy.py


## Output

The script generates a CSV file named "WeatherPy.csv" that contains weather data for the retrieved cities.

It also displays a 2x2 grid of scatter plots, each representing the relationship between city latitude and a weather variable. The variables plotted are:
- Max Temperature
- Humidity
- Cloudiness
- Wind Speed

The figure size is set to (10, 8), and the plots are displayed using the matplotlib library.

## Contributing

Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

Please make sure to update tests as appropriate.

## License

This project is licensed under the [MIT License](https://opensource.org/licenses/MIT).
