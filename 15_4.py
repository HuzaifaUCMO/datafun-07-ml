import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from scipy import stats

# Load the dataset
nyc = pd.read_csv('ave_hi_nyc_jan_1895-2018.csv')

# Rename columns for clarity
nyc.columns = ['Date', 'Temperature', 'Anomaly']

# Remove '01' from the Date to make it a proper year value
nyc.Date = nyc.Date.floordiv(100)

# Display first few rows to confirm
print(nyc.head(3))

# Perform linear regression using scipy's linregress
slope, intercept, r_value, p_value, std_err = stats.linregress(nyc.Date, nyc.Temperature)

# Print out the slope, intercept, and R-squared value
print(f"Slope: {slope}")
print(f"Intercept: {intercept}")
print(f"R-squared: {r_value**2}")

# Predict temperatures based on the regression line
nyc['Predicted_Temperature'] = slope * nyc.Date + intercept

# Plot the actual data points (scatter plot)
sns.scatterplot(data=nyc, x='Date', y='Temperature', hue='Temperature', palette='coolwarm', legend=False)

# Plot the regression line
plt.plot(nyc.Date, nyc['Predicted_Temperature'], color='red')

# Set plot labels and title
plt.title('NYC January High Temperatures (1895-2018)')
plt.xlabel('Year')
plt.ylabel('Temperature (°F)')

# Show the plot
plt.show()

# Predicting future temperature for 2019
predicted_2019 = slope * 2019 + intercept
print(f"Predicted temperature for January 2019: {predicted_2019:.2f}°F")

# Estimate past temperature for 1890
predicted_1890 = slope * 1890 + intercept
print(f"Estimated temperature for January 1890: {predicted_1890:.2f}°F")
