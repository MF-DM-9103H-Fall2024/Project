# Final Project

## Milestone 1: Ideation and High-Level Description
### Idea 1: Interactive Weather Prediction Tool
#### Concept
Design an interactive weather prediction tool that allows users to adjust different meteorological variables (such as temperature, humidity, and wind speed) and observe how these changes impact weather outcomes. The tool will use a predictive model to simulate different scenarios, helping users understand how various factors influence weather patterns.

#### Data and Datasets
- **Primary Sources**: Weather data from sources like OpenWeatherMap API or NOAA Climate Data.
- **Data Requirements**: Historical weather records, including variables like temperature, precipitation, wind speed, and humidity. Data preprocessing will involve cleaning and normalizing the inputs.

#### ML Techniques
- **Modeling**: Regression models (such as linear regression or decision trees) to predict weather outcomes based on input variables. A user-friendly interface will allow for interactive parameter adjustments.

### Idea 2: Student Sleep Patterns Analysis and Visualization

#### Concept
Analyze and visualize the sleep patterns of students, exploring correlations with factors like academic performance, stress levels, and extracurricular activities. The goal is to present insights that could help improve student well-being and academic outcomes.

#### Data and Datasets
- **Primary Sources**: Kaggle
- **Data Requirements**: Information on sleep duration, quality, and contributing factors (like study habits and physical activity). The data may require normalization and feature engineering.

#### ML Techniques
- **Modeling**: Use clustering algorithms to identify common sleep patterns and regression analysis to explore correlations. Visualization techniques (e.g., heatmaps, time series graphs) will make the data easier to understand.

### Idea 3: Electric Vehicle Population Analysis and Visualization

#### Concept
Create an analysis and visualization tool that explores the growth of electric vehicle (EV) populations across different regions or one region. The tool could highlight trends, identify hotspots of EV adoption, and explore the impact of policies and infrastructure on EV growth.

#### Data and Datasets
- **Primary Sources**: Kaggle, open datasets from government agencies (e.g., Department of Energy), EV registration databases, and industry reports.
- **Data Requirements**: Data on EV registrations, charging infrastructure, and demographic information. Data preprocessing will involve aggregating information from various sources.

#### ML Techniques
- **Modeling**: Use time series analysis to track growth trends and geospatial visualization techniques to map EV distribution. Regression models could explore factors influencing EV adoption.

## Milestone 2:  Data and a Plan
Proceeding with Idea 1, this project draws inspiration from the Japanese animated movie Weathering with You, where the protagonist has the ability to control the weather, transforming rainy days into sunny ones in Japan—a region known for frequent rainfall. Similarly, New York City experiences significant precipitation, with an average of 148 days of rain or snow annually, according to Google. This project aims to design an interactive interface that simulates transforming rainy and snowy days into more favorable weather conditions, offering users an engaging way to explore the impact of weather changes.

<p align="center">
  <img width="300" src="https://github.com/user-attachments/assets/3e5529f1-d540-4984-9e27-0d05a56c8b6a">
</p>

The dataset obtained from NOAA provides daily weather summaries for the period between December 1, 2022, and December 1, 2024. For this phase of the project, I focused on conducting initial data exploration and cleaning. This process included examining the dataset’s structure, identifying missing values, and selecting key features relevant to the project. The data is collected from multiple stations across NYC, resulting in variations in the number of variables recorded at each station.

<p align="center">
  <img width="900" src="https://github.com/user-attachments/assets/f8fa78c7-8d8c-41c6-8521-8d11e1055dc4">
</p>

<p align="center">
  <img width="900" src="https://github.com/user-attachments/assets/cc719d80-4ec1-430a-b11a-72798e700869">
</p>

## Milestone 3:  Initial Modeling/Programming
### Data Preprocessing
	•	Selected Relevant Features: DATE, PRCP, SNOW, SNWD, TMAX, TMIN, AWND, WDF2, WESF, WESD.
	•	Handling Missing Data: Missing values were filled with the median of each column to ensure consistency.
	•	Normalization: All numerical features were normalized using StandardScaler to facilitate better modeling and visualization.

### Data Visualization
 	•	Scatter plot: Temperature vs. Precipitation
	•	Line Plot: Temperature Trends Over Time
	•	Bar Plot: Average Monthly Precipitation
  	•	Heatmap: Correlation Between Variables
  	•	Scatter Plot: Wind Speed vs. Precipitation

### Preliminary Modeling
	- Baseline Model:
	• 	A Linear Regression model was trained to predict TMAX (maximum temperature) using PRCP, TMIN, and SNOW.
	•	Achieved a Mean Squared Error (MSE) of 0.1583.
	- Refined Model:
	•	A Random Forest Regressor was implemented, capturing non-linear relationships between features.

## Milestone 4:  Tuning and Adjusting

## Milestone 5:  Final Presentation and Discussion
