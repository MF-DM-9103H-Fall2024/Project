# Milestone 5: Final Code, Documentation, and Reflection

## Introduction  
This project focuses on predicting NYC weather using historical data and building an interactive interface to engage users. Inspired by the movie **Weathering With You**, the goal was to model precipitation, a complex and highly variable weather phenomenon, while delivering an engaging experience for users. Machine learning techniques such as **Random Forest** were applied, and a **"fun" interface** was developed to enable dynamic interaction.

---

## Data Preparation  

The **NOAA NYC Weather Dataset (2022-2024)** was used, containing daily weather summaries:  
- **Variables**: Precipitation, Snowfall, Max/Min Temperatures, Wind Speed, Snow Depth.  
- **Missing Data**: Humidity and other key weather indicators were unavailable.

Key steps in preparing the data included:  
1. Selecting relevant features: `TMAX, TMIN, AWND, WDF2, WESF, WESD, PRCP`.  
2. Scaling numerical features using **StandardScaler**.  
3. Creating derived features (`TEMP_RANGE`, `DAY_OF_YEAR`, `WIND_EFFECT`) for better model performance.  
4. Splitting data into training (before 2024) and testing (2024 onwards).  

---

## Modeling Process  

1. **Binary Classification**:  
   A **Random Forest Classifier** was used to predict whether a day would be "Rainy" or "Non-Rainy." The model achieved **72.3% accuracy**, despite the limited dataset.  

2. **Regression for Rainy Days**:  
   For days predicted as rainy, a **Random Forest Regressor** estimated precipitation amounts:  
   - RMSE for rainy days: **1.98**.  
   - Combined classification + regression RMSE: **1.16**.  

3. **PCA Experiment**:  
   Dimensionality reduction using **PCA** was applied, reducing features to 3 components while maintaining prediction accuracy.

---

## Interactive Interface  

The interactive interface was designed to combine prediction capabilities with an engaging user experience. Users can:  
1. **Input Weather Features**: Adjust key parameters such as temperature, wind speed, and snowfall.  
2. **Predict Precipitation**: Results are displayed in **mm** alongside dynamic animations inspired by *Weathering With You*.  
3. **Sunny Scenario**: If precipitation is predicted to be zero, the interface switches to a sunny animation.

### User Experience Highlights  

- **Rainy Forecast**:  
   Displays precipitation predictions with a rain-themed animation.  
   Example output:  
   **"Don't forget your umbrella: it's gonna be 0.3 mm of Precipitation 🌧️."**  

![Rainy Forecast](./imgs/rainy.png.png)

- **Sunny Forecast**:  
   When precipitation is zero, a bright and cheerful animation greets the user.  
   Example output:  
   **"A beautiful sunny day!☀️."**  

![Sunny Forecast](./imgs/sunny.png.png)

---

## Challenges Faced  

Several challenges were encountered throughout the project:  
1. **Limited Features**:  
   The dataset lacked critical variables like humidity, which are crucial for predicting precipitation. This limited the model's accuracy.  

2. **Precipitation Complexity**:  
   Precipitation data is highly imbalanced, with many days recording zero rainfall. This imbalance made accurate predictions more difficult, especially for smaller precipitation amounts.  

3. **Designing the Interface**:  
   Integrating fun animations and ensuring a clean, responsive layout required multiple adjustments.

4. **Combining Classification and Regression**:  
   Predicting "rainy" days first and then estimating rainfall amounts added complexity but ultimately improved the final results.

---

## Conclusion and Reflections  

This project implemented a machine learning pipeline for predicting precipitation while engaging users through an interactive interface. The integration of **Random Forest models** enabled robust predictions, while user inputs allowed for dynamic forecasts.  

### Key Takeaways:  
- Combining **classification** and **regression** effectively improved the overall prediction pipeline.  
- Despite the challenges, the project demonstrated the value of derived features and **PCA** for reducing noise and dimensionality.  
- The interactive design, inspired by *Weathering With You*, provided an engaging experience that made weather predictions more accessible and enjoyable.  

### Future Improvements:  
- **Incorporating Real-Time Data**: Integrating real-time weather updates for a more dynamic prediction experience.  
- **Adding More Features**: Including variables like humidity, cloud cover, and pressure for improved accuracy.  
- **Exploring Deep Learning Models**: Leveraging neural networks to model the complex relationships within weather data.  

This project aims to apply the techniques learned from class in a fun and engaging way.

---